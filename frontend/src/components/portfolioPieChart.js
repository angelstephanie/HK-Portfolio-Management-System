import React, { useEffect, useState, useRef } from 'react';
import { Form, Spinner } from 'react-bootstrap';
import { Pie } from 'react-chartjs-2';
import 'chart.js/auto';
import '../styles/portfolioPieChart.css';

const FILTER_OPTIONS = [
    { value: 'assetType', label: 'Asset Type' },
    { value: 'asset', label: 'Asset' }
];

const fetchPortfolioData = async () => {
    return [
        { asset: 'AAPL', assetType: 'Stock', amount: 5000 },
        { asset: 'GOOGL', assetType: 'Stock', amount: 3000 },
        { asset: 'US Treasury', assetType: 'Bond', amount: 2000 },
        { asset: 'BTC', assetType: 'Crypto', amount: 1000 },
        { asset: 'ETH', assetType: 'Crypto', amount: 500 },
        { asset: 'AMD', assetType: 'Stock', amount: 1500 }
    ];
};

const getPieChartData = (portfolio, filter, activeIndex) => {
    const dataMap = {};
    if (filter === 'assetType') {
        portfolio.forEach(item => {
            dataMap[item.assetType] = (dataMap[item.assetType] || 0) + item.amount;
        });
    } else if (filter === 'asset') {
        portfolio.forEach(item => {
            dataMap[item.asset] = (dataMap[item.asset] || 0) + item.amount;
        });
    }

    const labels = Object.keys(dataMap);
    const data = Object.values(dataMap);

    const backgroundColor = labels.map((_, index) => {
        if (activeIndex === null || activeIndex === index) {
            return COLORS[index % COLORS.length]; // Full color
        } else {
            return COLORS[index % COLORS.length] + '55'; // Dull (add alpha 0.33)
        }
    });

    return { labels, data, backgroundColor };
};

const COLORS = [
    '#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f',
    '#edc949', '#af7aa1', '#ff9da7', '#9c755f', '#bab0ab'
];

function PortfolioPieChart() {
    const [filter, setFilter] = useState('assetType');
    const [portfolio, setPortfolio] = useState([]);
    const [loading, setLoading] = useState(true);
    const [activeIndex, setActiveIndex] = useState(null);
    const chartRef = useRef(null);

    useEffect(() => {
        fetchPortfolioData().then(data => {
            setPortfolio(data);
            setLoading(false);
        });
    }, []);

    const { labels, data, backgroundColor } = getPieChartData(portfolio, filter, activeIndex);

    const chartData = {
        labels,
        datasets: [
            {
                data,
                backgroundColor,
                borderColor: '#fff',
                borderWidth: 2
            }
        ]
    };

    return (
        <>
            <Form.Group className="mb-3">
                <Form.Label>Filter By</Form.Label>
                <Form.Select value={filter} onChange={e => setFilter(e.target.value)}>
                    {FILTER_OPTIONS.map(opt => (
                        <option key={opt.value} value={opt.value}>{opt.label}</option>
                    ))}
                </Form.Select>
            </Form.Group>
            <br />
            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" variant="primary" />
                </div>
            ) : (
                <Pie
                    ref={chartRef}
                    className="pie-chart-container"
                    data={chartData}
                    options={{
                        onHover: (event, chartElement) => {
                            if (chartElement.length > 0) {
                                setActiveIndex(chartElement[0].index);
                            } else {
                                setActiveIndex(null);
                            }
                        },
                        animation: {
                            animateScale: true,
                            animateRotate: true,
                            duration: 800,
                            easing: 'easeOutQuart'
                        },
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    color: '#333',
                                    font: { size: 14 },
                                    usePointStyle: true,
                                    pointStyle: 'circle'
                                }
                            },
                            tooltip: {
                                backgroundColor: '#ffffff',
                                titleColor: '#333',
                                bodyColor: '#333',
                                borderColor: '#ccc',
                                borderWidth: 1,
                                padding: 10,
                                cornerRadius: 8,
                                callbacks: {
                                    label: function (context) {
                                        const value = context.parsed;
                                        return `${context.label}: $${value.toLocaleString()}`;
                                    }
                                }
                            }
                        },
                        layout: {
                            padding: 20
                        },
                        cutout: '50%',
                        hoverOffset: 30
                    }}

                />
            )}
        </>
    );
}

export default PortfolioPieChart;
