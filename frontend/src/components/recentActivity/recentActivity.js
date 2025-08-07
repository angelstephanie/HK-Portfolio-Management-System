import React, { useEffect, useState } from 'react';
import { Card, ListGroup } from 'react-bootstrap';
import transactionsData from '../../assets/transactions.json';

const RecentActivityFeed = () => {
    const [transactions, setTransactions] = useState(transactionsData || []);

    return (
        <div className="recent-activity-feed">
            {transactions.length > 0 ? (
                transactions.map((transaction, index) => {
                    // Calculate the total value manually
                    const totalValue = (transaction.quantity * transaction.price_per_unit) + transaction.fee;
                    
                    // Format the timestamp into a human-readable format
                    const transactionDate = new Date(transaction.timestamp).toLocaleDateString();

                    return (
                        <Card key={index} className="transaction-card mb-3 shadow-sm">
                            <Card.Body>
                                <div className="d-flex justify-content-between">
                                    <span className="transaction-date text-muted">{transactionDate}</span>
                                    <span className={`transaction-type ${transaction.type === 'buy' ? 'buy' : 'sell'}`}>
                                        {transaction.type.charAt(0).toUpperCase() + transaction.type.slice(1)}
                                    </span>
                                </div>
                                <div className="transaction-details mt-3">
                                    <h5 className="asset-name">{transaction.symbol}</h5>
                                    <span className="transaction-amount">
                                        {transaction.quantity} @ ${transaction.price_per_unit.toFixed(2)}
                                    </span>
                                    <div className="transaction-total mt-2">
                                        <strong>Total Value: </strong>${totalValue.toFixed(2)}
                                    </div>
                                </div>
                            </Card.Body>
                        </Card>
                    );
                })
            ) : (
                <Card className="no-transaction-card">
                    <Card.Body>No recent transactions.</Card.Body>
                </Card>
            )}
        </div>
    );
};

export default RecentActivityFeed;
