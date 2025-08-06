import Col from 'react-bootstrap/Col';
import "../../styles/watchlist.css";

const WatchlistItem = ({item}) => {
    const difference = item.current_price - item.open_price;
    const percentageChange = ((difference / item.open_price) * 100).toFixed(2);
    return (
    <Col xs={12} className="mb-4">
        <div style={{
            padding: '15px',
            backgroundColor: '#f5f5f5ff',
            borderRadius: '12px',
            boxShadow: '0 4px 8px rgba(240, 240, 240, 0.05)',
            marginTop: '3px'
        }}>
            <p className="text text-header" style={{ color: "#3E5EBD", fontWeight: 'bold', fontSize: '1.2rem', marginBottom: '12px' }}>
                {item.name}
            </p>
            <p className="text text-price" style={{ fontSize: '1.1rem', fontWeight: '500', color: '#333' }}>
                ${item.current_price.toFixed(2)}
            </p>
            <p className="text text-diff" style={{ color: difference >= 0 ? "green" : "red", fontSize: '1.1rem' }}>
                {difference.toFixed(2)} ({percentageChange}%)
            </p>
        </div>
    </Col>
    );
};

export default WatchlistItem;