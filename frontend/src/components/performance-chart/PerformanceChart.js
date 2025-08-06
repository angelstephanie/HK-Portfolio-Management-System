import React, { useState } from 'react';
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
    text: 'Portfolio Performance Chart',
    },
},
};

// Timeline options
const timeOptions = ['5D', '1M', '3M', '1Y', 'Max'];

const PerformanceChart = () => {
    const [selectedTime, setSelectedTime] = useState('1Y');

    // Filter data based on the selected time range
    const filteredData = portfolioPerformanceData.slice(
        selectedTime === '5D' ? -5 :
        selectedTime === '1M' ? -30 :
        selectedTime === '3M' ? -90 :
        selectedTime === '1Y' ? -365 : 0
    );

    const labels = filteredData.map(entry => entry.date);
    const data = {
        labels,
        datasets: [
            {
                label: 'Total Asset Value',
                data: filteredData.map(entry => entry.totalAssetValue),
                borderColor: '#3E5EBD',
                backgroundColor: 'rgba(83, 120, 199, 0.2)',
                radius: 0
            },
        ],
    };

    return (
        <div className="performance-chart">
            <div className="time-options">
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