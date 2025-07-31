import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';

const PerformanceChart = () => {
    const [data, setData] = useState({
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [
            {
                label: 'Portfolio Performance',
                data: [65, 59, 80, 81, 56, 55],
                fill: false,
                borderColor: '#742774',
            },
        ],
    });

    return (
        <div className="performance-chart">
            <Line data={data} />
        </div>
    );
}

export default PerformanceChart;