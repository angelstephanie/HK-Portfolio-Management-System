import { useState, useRef, useEffect } from 'react';
import { Form } from 'react-bootstrap';
import { Pie } from 'react-chartjs-2';
import 'chart.js/auto';
import '../styles/portfolioPieChart.css';

const FILTER_OPTIONS = [
    { value: 'type', label: 'Asset Type' },
    { value: 'symbol', label: 'Asset' }
];

const getPieChartData = (holdingsData, filter, activeIndex) => {
    const dataMap = {};
    if (filter === 'type') {
        holdingsData.forEach(item => {
            dataMap[item.type] = (dataMap[item.type] || 0) + item.avg_buy_price * item.quantity;
        });
    } else if (filter === 'symbol') {
        holdingsData.forEach(item => {
            dataMap[item.symbol] = (dataMap[item.symbol] || 0) + item.avg_buy_price * item.quantity;
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

function PortfolioPieChart({portfolioId, holdings}) {
    const [filter, setFilter] = useState('type');
    const [portfolioHoldings, setPortfolioHoldings] = useState([]);
    const [activeIndex, setActiveIndex] = useState(null);
    const chartRef = useRef(null);

    useEffect(() => {
        setPortfolioHoldings(holdings.filter(h => h.portfolio_id === portfolioId));
    }, [portfolioId, holdings]);

    const { labels, data, backgroundColor } = getPieChartData(portfolioHoldings, filter, activeIndex);
    
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

            {portfolioHoldings.length === 0 ? (
                <p className="text-center text-muted">No holdings for this portfolio.</p>
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
                                        const total = context.chart._metasets[context.datasetIndex].total;
                                        const percentage = ((value/total)*100).toFixed(2);
                                        return `${context.label}: $${value.toLocaleString()} (${percentage}%)`; 
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
