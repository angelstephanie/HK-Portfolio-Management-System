import React, { useEffect, useState } from 'react';
import { ListGroup } from 'react-bootstrap';
import transactionsData from '../../assets/transactions.json';

const RecentActivityFeed = () => {
    const [transactions, setTransactions] = useState(transactionsData || []);

    return (
        <div className="recent-activity-feed">
            <ListGroup variant="flush">git
                {transactions.length > 0 ? (
                    transactions.map((transaction, index) => {
                        // Calculate the total value manually
                        const totalValue = (transaction.quantity * transaction.price_per_unit) + transaction.fee;
                        
                        // Format the timestamp into a human-readable format
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
                                    <span className="asset-name">{transaction.symbol}</span>
                                    <span className="transaction-amount">
                                        {transaction.quantity} @ ${transaction.price_per_unit.toFixed(2)}
                                    </span>
                                    <div className="transaction-total">
                                        <strong>Total Value: </strong>${totalValue.toFixed(2)}
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
