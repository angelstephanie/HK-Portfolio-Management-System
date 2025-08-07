import { useState, useEffect } from 'react';
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
import { useNavigate } from 'react-router-dom';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const TopMovers = ({holdings}) => {
  const [activeTab, setActiveTab] = useState('gainers');
  const [moversData, setMoversData] = useState({
    gainers: [],
    losers: []
  });

  const navigate = useNavigate();

  const handleRowClick = (row) => {
    if (row.symbol) {
      navigate(`/asset/${row.symbol}`);
    }
  };

  useEffect(() => {
    if (Array.isArray(holdings) && holdings.length > 0) {
      const enrichedData = holdings.map(item => {
      const price_change_percentage = item.opening_price !== 0 ? ((item.current_price - item.opening_price)/item.opening_price) * 100: 0;
        return {
          ...item,
          price_change_percentage: price_change_percentage.toFixed(2),
        };
      });

      if (enrichedData && enrichedData.length > 0) {
        const sortedHoldings = [...enrichedData].sort(
          (a, b) => b.price_change_percentage - a.price_change_percentage
        );

        const gainersData = sortedHoldings.slice(0, 5);
        const losersData = sortedHoldings.slice(-5).reverse();

        setMoversData({
          gainers: gainersData,
          losers: losersData
        });
      }
    }
  }, [holdings]);

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
          <div
          key={index}
          className="d-flex justify-content-between align-items-center py-2"
          style={{ cursor: 'pointer' }}
          onClick={() => handleRowClick(item)}>
            <div>
              <strong>{item.symbol}</strong>
              <div className="text-muted small">{item.name}</div>
            </div>${item.price_change_percentage >= 0 ? 'text-success' : 'text-danger'}
            <div className={`fw-medium `}>
              {item.price_change_percentage >= 0 ? '+' : ''}
              {item.price_change_percentage}%
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TopMovers;