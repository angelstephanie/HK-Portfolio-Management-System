import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import gainersData from '../assets/top5_gainers.json';
import losersData from '../assets/top5_losers.json';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const TopMovers = () => {
  const [activeTab, setActiveTab] = useState('gainers');
  const [moversData, setMoversData] = useState({
    gainers: [],
    losers: []
  });

  useEffect(() => {
    setMoversData({
      gainers: gainersData,
      losers: losersData
    });
  }, []);

  const chartData = {
    labels: moversData[activeTab].map(item => item.symbol),
    datasets: [{
      label: 'Price Change (%)',
      data: moversData[activeTab].map(item => item.price_change_percentage),
      backgroundColor: moversData[activeTab].map(item => 
        item.price_change_percentage >= 0 ? 'rgba(75, 192, 192, 0.6)' : 'rgba(255, 99, 132, 0.6)'
      ),
      borderColor: moversData[activeTab].map(item => 
        item.price_change_percentage >= 0 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)'
      ),
      borderWidth: 1,
    }]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      title: { display: false }
    },
    scales: {
      y: {
        beginAtZero: false,
        title: { display: true, text: 'Change (%)' },
        grid: { display: false }
      },
      x: {
        grid: { display: false }
      }
    }
  };

  return (
    <div className="top-movers-inner">
      <div className="text-muted mb-2">Live Performance (Since 9:30 AM GMT+8)</div>
      
      <ul className="nav nav-tabs mb-3">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'gainers' ? 'active' : ''}`}
            onClick={() => setActiveTab('gainers')}
          >
            Gainers
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'losers' ? 'active' : ''}`}
            onClick={() => setActiveTab('losers')}
          >
            Losers
          </button>
        </li>
      </ul>

      <div className="chart-container" style={{ height: '200px' }}>
        <Bar data={chartData} options={options} />
      </div>

      <div className="movers-list mt-3">
        {moversData[activeTab].map((item, index) => (
          <div key={index} className="d-flex justify-content-between align-items-center py-2">
            <div>
              <strong>{item.symbol}</strong>
              <div className="text-muted small">{item.name}</div>
            </div>
            <div className={`fw-medium ${item.price_change_percentage >= 0 ? 'text-success' : 'text-danger'}`}>
              {item.price_change_percentage >= 0 ? '+' : ''}
              {item.price_change_percentage.toFixed(2)}%
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TopMovers;