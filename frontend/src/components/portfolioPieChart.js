import React, { useEffect, useState } from 'react';
import { Form, Spinner } from 'react-bootstrap';
import { Pie } from 'react-chartjs-2';
import 'chart.js/auto';

const FILTER_OPTIONS = [
    { value: 'assetType', label: 'Asset Type' },
    { value: 'asset', label: 'Asset' }
];

// Dummy fetch function, replace with actual API call
const fetchPortfolioData = async () => {
    // Example data structure
    return [
        { asset: 'AAPL', assetType: 'Stock', amount: 5000 },
        { asset: 'GOOGL', assetType: 'Stock', amount: 3000 },
        { asset: 'US Treasury', assetType: 'Bond', amount: 2000 },
        { asset: 'BTC', assetType: 'Crypto', amount: 1000 },
        { asset: 'ETH', assetType: 'Crypto', amount: 500 },
        { asset: 'AMD', assetType: 'Stock', amount: 1500 }
    ];
};

const getPieChartData = (portfolio, filter) => {
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
    return { labels, data };
};

const COLORS = [
    '#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f',
    '#edc949', '#af7aa1', '#ff9da7', '#9c755f', '#bab0ab'
];

function PortfolioPieChart() {
    const [filter, setFilter] = useState('assetType');
    const [portfolio, setPortfolio] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // setLoading(true);
        fetchPortfolioData().then(data => {
            setPortfolio(data);
            setLoading(false);
        });
    }, []);

    const { labels, data } = getPieChartData(portfolio, filter);

    const chartData = {
        labels,
        datasets: [
            {
                data,
                backgroundColor: COLORS.slice(0, labels.length),
                borderColor: '#fff',
                borderWidth: 2
            }
        ]
    };

// function getTopNLabels(num, data, labels){
//     const topValues = [...data].sort((a, b) => b - a).slice(0, num);
//     const selectedIndexes = data
//     .map((value, index) => ({ value, index }))
//     .filter(item => topValues.includes(item.value))
//     .map(item => item.index);
//     const selectedLabels = labels.filter((_, index) => selectedIndexes.includes(index));
//     return selectedLabels.slice(0, num);
// }

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
            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" variant="primary" />
                </div>
            ) : (
                <Pie
                    data={chartData}
                    options={{
                        plugins: {
                            legend: {
                                display: true,
                                position: 'bottom',
                                labels: { color: '#333', font: { size: 14 },
                                    generateLabels: function(chart) {
                                        const labels = chart.data.labels || [];
                                        const dataset = chart.data.datasets[0] || {};
                                        const backgroundColors = dataset.backgroundColor || [];
                                        const data = dataset.data || [];

                                        // Get topN indexes by value
                                        const topN = 5;
                                        const topIndexes = data
                                            .map((value, index) => ({ value, index }))
                                            .sort((a, b) => b.value - a.value)
                                            .slice(0, topN)
                                            .map(item => item.index);

                                        // Build all legend labels manually
                                        const allLabels = labels.map((label, index) => ({
                                            text: label,
                                            fillStyle: backgroundColors[index] || 'gray',
                                            strokeStyle: '#fff',
                                            lineWidth: 2,
                                            hidden: false,
                                            index: index
                                        }));

                                        // Filter to only top N indexes
                                        return allLabels.filter(label => topIndexes.includes(label.index));
                                        }
                            }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        const value = context.parsed;
                                        return `${context.label}: $${value.toLocaleString()}`;
                                    }
                                }
                            }
                        }
                    }}
                    style={{ maxHeight: 350 }}
                />
            )}
        </>
    );
}

export default PortfolioPieChart;