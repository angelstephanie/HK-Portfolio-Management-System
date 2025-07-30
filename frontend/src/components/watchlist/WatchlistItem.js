import Col from 'react-bootstrap/Col';
import "../../styles/watchlist.css";

const WatchlistItem = ({item}) => {
    const difference = item.current_price - item.open_price;
    const percentageChange = ((difference / item.open_price) * 100).toFixed(2);
    return (
        <Col xs={6}  className="border border-dashed" >
            <p className="text text-header" style={{color: "#3E5EBD"}}>{item.name}</p>
            <p className="text text-price">{item.current_price}</p>
            <p className="text text-diff" style={{color: difference >= 0 ? "green" : "red" }}>{difference.toFixed(2)}</p>
            <p className="text text-diff" style={{color: difference >= 0 ? "green" : "red" }}>({percentageChange}%)</p>
        </Col>
    );
};

export default WatchlistItem;