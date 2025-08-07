import React, { useState, useEffect, useMemo } from 'react';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
import { Line } from 'react-chartjs-2';
import portfolioPerformanceData from '../../assets/portfolio_performance.json';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

export const options = {
responsive: true,
plugins: {
    legend: {
    position: 'top',
    display: false,
    },
    title: {
    display: false,
    },
},
};

// Timeline options
const timeOptions = ['5D', '1M', '3M', '1Y', 'Max'];

// Helper to format DD/MM
const formatDayMonth = (dateStr) => {
    const date = new Date(dateStr);
    return `${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')}`;
};

const getFilteredData = (selectedTime, portfolioSnaps) => {
    if (selectedTime === '5D') return portfolioSnaps.slice(-5);
    if (selectedTime === '1M') return portfolioSnaps.slice(-30);
    if (selectedTime === '3M') return portfolioSnaps.slice(-90);
    if (selectedTime === '1Y') return portfolioSnaps.slice(-365);
    if (selectedTime === 'Max') return portfolioSnaps;
    return portfolioSnaps;
};

const PerformanceChart = ({portfolioSnaps}) => {
    
    const [selectedTime, setSelectedTime] = useState('5D');
   
    const filteredData = useMemo(
        () => getFilteredData(selectedTime, portfolioSnaps),
        [selectedTime, portfolioSnaps]
    );

    // Neat, non-overlapping labels formatting
    const labels = useMemo(() => {
        const arrLen = filteredData.length;
        // For 5D: show day/month for first, last, and every 10th
        if (selectedTime === '5D') {
            return filteredData.map((entry, i) => formatDayMonth(entry.snapshot_date));
        }
        // For >= 1M: show DD/MM for first, last, and every Nth to reduce clutter
        let interval = 7; // default every 7th for 1M, 3M
        if (selectedTime === '1Y') interval = 31;
        if (selectedTime === 'Max') interval = Math.ceil(arrLen / 12); // max 12 labels for Max

        return filteredData.map((entry, i) =>
            (i === 0 || i % interval === 0)
                ? formatDayMonth(entry.snapshot_date)
                : ''
        );
    }, [filteredData, selectedTime]);

    const data = {
        labels,
        datasets: [
            {
                label: 'Total Asset Value',
                data: filteredData.map(entry => (entry.cash_value - entry.invested_value)/entry.invested_value * 100),
                borderColor: '#3E5EBD',
                backgroundColor: 'rgba(83, 120, 199, 0.2)',
                radius: 0
            },
        ],
    };

    // Chart options with dynamic ticks and reduced overlapping
    const options = useMemo(() => ({
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
                display: false,
            },
            title: {
                display: false,
            },
        },
        scales: {
            x: {
                ticks: {
                    autoSkip: false,
                    callback: function(value, index) {
                        return labels[index] || '';
                    },
                    color: '#666',
                    font: {
                        size: 10,
                        weight: 'bold'
                    },
                    maxRotation: 0,
                    minRotation: 0,
                },
                grid: {
                    display: false,
                    drawBorder: false
                }
            },
            y: {
                ticks: {
                    color: '#666',
                    font: {
                        size: 11,
                    }
                },
                grid: {
                    color: '#eee'
                }
            }
        }
    }), [labels]);

    return (
        <div className="performance-chart">
            <div className="text-muted mb-3">Last Updated: 9:30 AM GMT+8</div>
            <div className="time-options mb-3">
                {timeOptions.map(option => (
                    <button
                        key={option}
                        onClick={() => setSelectedTime(option)}
                        style={{
                            margin: '0 5px 10px 0',
                            padding: '5px 10px',
                            backgroundColor: selectedTime === option ? '#3E5EBD' : '#f8f9fa',
                            color: selectedTime === option ? '#fff' : '#000',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                            fontWeight: selectedTime === option ? 500 : 'normal',
                            fontSize: '0.9rem',
                        }}
                    >
                        {option}
                    </button>
                ))}
            </div>
            <Line data={data} options={options} />
        </div>
    );
};

export default PerformanceChart;