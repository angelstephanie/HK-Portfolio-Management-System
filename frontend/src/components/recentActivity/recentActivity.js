import { useEffect, useState } from 'react';
import { ListGroup, Spinner, Alert } from 'react-bootstrap';
import './style.css';

const RecentActivityFeed = () => {
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/transactions');
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                setTransactions(data || []);
            } catch (err) {
                setError(err.message || 'Failed to fetch transactions.');
            } finally {
                setLoading(false);
            }
        };

        fetchTransactions();
    }, []);

    if (loading) {
        return <Spinner animation="border" role="status"><span className="visually-hidden">Loading...</span></Spinner>;
    }

    if (error) {
        return <Alert variant="danger">{error}</Alert>;
    }

    return (
        <div className="recent-activity-feed">
            <ListGroup variant="flush">
                {transactions.length > 0 ? (
                    [...transactions]
                        .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp)) // Newest first
                        .slice(0, 4) // Only show the 4 most recent
                        .map((transaction, index) => {
                            const totalValue = (transaction.quantity * transaction.price_per_unit) + transaction.fee;
                            const transactionDate = new Date(transaction.timestamp).toLocaleDateString();

                            return (
                                <ListGroup.Item key={index} className="transaction-item">
                                    <div className="d-flex justify-content-between">
                                        <span className="transaction-date">{transactionDate}</span>
                                        <span className={`transaction-type ${transaction.type === 'buy' ? 'buy' : 'sell'}`}>
                                            {transaction.type.charAt(0).toUpperCase() + transaction.type.slice(1)}
                                        </span>
                                    </div>
                                    <div className="transaction-details">
                                        <span className="asset-name">{transaction.symbol} </span>
                                        <span className="transaction-amount">
                                            {transaction.quantity} @ ${transaction.price_per_unit}
                                        </span>
                                        <div className="transaction-total">
                                            <strong>Total Value: </strong>${totalValue}
                                        </div>
                                    </div>
                                </ListGroup.Item>
                            );
                        })
                ) : (
                    <ListGroup.Item>No recent transactions.</ListGroup.Item>
                )}
            </ListGroup>
        </div>
    );

};

export default RecentActivityFeed;
