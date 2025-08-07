import React, { useState, useMemo } from 'react';
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

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const timeOptions = ['1D', '5D', '1M', '3M', '1Y', 'Max'];

// Helper to format DD/MM
const formatDayMonth = (dateStr) => {
    const date = new Date(dateStr);
    return `${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')}`;
};
// Helper to format hour:minute
const formatHourMinute = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};

const getFilteredData = (selectedTime, hourlyData, dailyData) => {
    if (selectedTime === '1D') return hourlyData.slice(-13);
    if (selectedTime === '5D') return hourlyData.slice(-45);
    if (selectedTime === '1M') return dailyData.slice(-30);
    if (selectedTime === '3M') return dailyData.slice(-90);
    if (selectedTime === '1Y') return dailyData.slice(-365);
    if (selectedTime === 'Max') return dailyData;
    return dailyData;
};

const LineChart = ({ hourlyData, dailyData, timeSelection }) => {
    const [selectedTime, setSelectedTime] = useState('1D');

    const filteredData = useMemo(
        () => getFilteredData(selectedTime, hourlyData, dailyData),
        [selectedTime, hourlyData, dailyData]
    );

    // Neat, non-overlapping labels formatting
    const labels = useMemo(() => {
        const arrLen = filteredData.length;
        // For 1D: show all hour:minute
        if (selectedTime === '1D') {
            return filteredData.map(entry => formatHourMinute(entry.date));
        }
        // For 5D: show day/month for first, last, and every 10th
        if (selectedTime === '5D') {
            return filteredData.map((entry, i) =>
                (i === 0 || i % 10 === 0)
                    ? formatDayMonth(entry.date)
                    : ''
            );
        }
        // For >= 1M: show DD/MM for first, last, and every Nth to reduce clutter
        let interval = 7; // default every 7th for 1M, 3M
        if (selectedTime === '1Y') interval = 31;
        if (selectedTime === 'Max') interval = Math.ceil(arrLen / 12); // max 12 labels for Max

        return filteredData.map((entry, i) =>
            (i === 0 || i % interval === 0)
                ? formatDayMonth(entry.date)
                : ''
        );
    }, [filteredData, selectedTime]);

    const data = {
        labels,
        datasets: [
            {
                label: 'Total Asset Value',
                data: filteredData.map(entry => entry.price),
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
                    display: timeSelection,
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
                    display: timeSelection,
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
        <div className="performance-chart" style={timeSelection ? {} : {display: 'flex', alignItems: 'center', justifyContent: 'end', width: '50%'}}>
            <div className="time-options" style={{ marginBottom: '10px' }}>
                { timeSelection ? timeOptions.map(option => (
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
                            minWidth: '48px'
                        }}
                    >
                        {option}
                    </button>
                )) : null}
            </div>
            <Line data={data} options={options}/>
        </div>
    );
};

export default LineChart;