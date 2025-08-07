import Col from 'react-bootstrap/Col';
import "../../styles/watchlist.css";
import LineChart from '../performance-chart/lineChart';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const WatchlistItem = ({item}) => {
    const navigate = useNavigate();
    const difference = parseFloat(item.current_price) - parseFloat(item.opening_price);
    const percentageChange = ((difference / parseFloat(item.opening_price)) * 100).toFixed(2);

    const [hourlyPrice, setHourlyPrice] = useState([]);
    useEffect(() => {
            fetch(`http://127.0.0.1:5000/assets/${item.symbol}/historicprice/1`)
            .then(response => response.json())
            .then(data => { 
                const priceData = [];
                Object.entries(data).forEach(([key, value]) => {
                    priceData.push({
                        date: key,
                        price: value
                    });
                });
                setHourlyPrice(priceData);
            })
            .catch(error => {
                console.log('Error fetching hourly price data:', error.message);
            });
    }, [item]);

    const handleClick = () => {
        const path = `/asset/${item.symbol}`;
        navigate(path);
    }


    return (
    <Col xs={12} className="mb-1 row" onClick={handleClick} style={{ cursor: 'pointer' }}>
        <div className="col-6" style={{
            padding: '15px',
            boxShadow: '0 4px 8px rgba(249, 249, 249, 0.01)',
            marginTop: '3px'
        }}>
            <p className="text text-header" style={{ color: "#3E5EBD", fontWeight: 'bold', fontSize: '1.1rem', marginBottom: '5px' }}>
                {item.symbol}
            </p>
            <p className="text text-price" style={{ fontSize: '1.1rem', fontWeight: '500', color: '#333' }}>
                ${parseFloat(item.current_price).toFixed(2)}
            </p>
            <p className="text text-diff fw-medium" style={{ color: difference >= 0 ? "green" : "red", fontSize: '0.9rem' }}>
                {difference.toFixed(2)} ({percentageChange}%)
            </p>
        </div>
        <LineChart timeSelection={false} hourlyData={hourlyPrice} className="col-6"/>
    </Col>
    );
};

export default WatchlistItem;