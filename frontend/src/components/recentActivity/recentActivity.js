import React, { useEffect, useState } from 'react';
import { ListGroup } from 'react-bootstrap';
import '../recentActivity/style.css'; // Assuming you have a CSS file for styling

const RecentActivityFeed = () => {
    const [transactions, setTransactions] = useState([]);

    // Fetch transactions from the JSON file
    debugger;
    useEffect(() => {
        // Assuming transactions.json is in the 'src/assets' folder
        fetch('./assets/transactions.json')
            .then((response) => response.json())
            .then((data) => setTransactions(data))
            .catch((error) => console.error("Error fetching transactions:", error));
    }, []);

    return (
        <div className="recent-activity-feed">
            <ListGroup variant="flush">
                {transactions.length > 0 ? (
                    transactions.map((transaction, index) => (
                        <ListGroup.Item key={index} className="transaction-item">
                            <div className="d-flex justify-content-between">
                                <span className="transaction-date">{transaction.date}</span>
                                <span className={`transaction-type ${transaction.transaction_type === 'Buy' ? 'buy' : 'sell'}`}>
                                    {transaction.transaction_type}
                                </span>
                            </div>
                            <div className="transaction-details">
                                <span className="asset-name">{transaction.asset}</span>
                                <span className="transaction-amount">
                                    {transaction.amount} @ ${transaction.price_per_unit.toFixed(2)}
                                </span>
                                <div className="transaction-total">
                                    <strong>Total Value: </strong>${transaction.total_value.toFixed(2)}
                                </div>
                            </div>
                        </ListGroup.Item>
                    ))
                ) : (
                    <ListGroup.Item>No recent transactions.</ListGroup.Item>
                )}
            </ListGroup>
        </div>
    );
};

export default RecentActivityFeed;
