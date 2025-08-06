import React, { useEffect, useState } from 'react';
import { format } from 'date-fns';

const BuySellAsset = ({ asset, totalHoldings }) => {
    const endpoint = `http://127.0.0.1:5000`;
    const [activeTab, setActiveTab] = useState('Buy');
    const [limitPrice, setLimitPrice] = useState(asset.current_price || '');
    const [quantity, setQuantity] = useState(1);
    const [dateTime, setDateTime] = useState(format(new Date(), "yyyy-MM-dd'T'HH:mm"));
    const [notes, setNotes] = useState('');

    useEffect(() => {
        setLimitPrice(asset.current_price);
    }, [asset.current_price]);

    const handleInputChange = (setter) => (event) => {
        setter(event.target.value);
    };

    const handleSubmission = (event) => {
        event.preventDefault();
        submitTransaction();
        console.log(`Submitting ${activeTab} with Price: ${limitPrice}, Quantity: ${quantity}, DateTime: ${dateTime}`);
    };

    const submitTransaction = async () => {
        const holdingsData = {
            holding_id: null, //need to modify
            portfolio_id: 1,
            symbol: asset.symbol,
            quantity: quantity,
            avg_buy_price: limitPrice,
        };
        const transactionData = {
            portfolio_id: 1,
            symbol: asset.symbol,
            type: activeTab.toLowerCase(),
            quantity: quantity,
            price_per_unit: limitPrice,
            fee: 0.01,
            notes: '',
            timestamp: format(new Date(dateTime), "yyyy-MM-dd HH:mm:ss"),
        };

        console.log(`Transaction Data:`, transactionData);
        console.log(`Holdings Data:`, holdingsData);   

        try {
            const responseTransaction = await fetch(`${endpoint}/transactions`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(transactionData),
            });

            if (!responseTransaction.ok) {
                throw new Error(`Error: ${responseTransaction.statusText}`);
            }

            try {
                // Check ig we sell or buy assets
                const responseHoldings = await fetch(`${endpoint}/holdings`, {
                    method: totalHoldings > 0 ? 'PUT' : 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(holdingsData),
                });
    
                if (!responseHoldings.ok) {
                    throw new Error(`Error: ${responseHoldings.statusText}`);
                }
    
                const result = await responseHoldings.json();
                alert('Transaction submitted successfully:', result);
            } catch (error) {
                alert('Failed to submit transaction:', error);
            }
        } catch (error) {
            alert('Failed to submit transaction:', error);
        }
    };
        
    return (
        <div className="buy-sell-asset-container">
            <div className="top-movers-inner">
                <ul className="nav nav-tabs mb-3 mt-2">
                    {['Buy', 'Sell'].map((tab) => (
                        <li className="nav-item" key={tab}>
                            <button
                                className={`nav-link ${activeTab === tab ? 'active' : ''}`}
                                onClick={() => setActiveTab(tab)}
                            >
                                {tab}
                            </button>
                        </li>
                    ))}
                </ul>
                <div className="chart-container" style={{ padding: '10px' }}>
                    <form onSubmit={handleSubmission}>
                        {[
                            { label: 'Limit Price (US$)', id: 'limitPrice', type: 'number', value: limitPrice, setter: setLimitPrice, step: '0.01', min: '0' },
                            { label: 'Quantity', id: 'quantity', type: 'number', value: quantity, setter: setQuantity, step: '1', min: '0', max: activeTab === 'Sell' ? totalHoldings : undefined },
                            { label: 'Date Time', id: 'dateTime', type: 'datetime-local', value: dateTime, setter: setDateTime },
                            { label: 'Notes', id: 'notes', type: 'text', value: notes, setter: setNotes, placeholder: '...' }
                        ].map(({ label, id, type, value, setter, ...rest }) => (
                            <div className="form-group mb-3 d-flex justify-content-between" key={id}>
                                <label className="me-2" htmlFor={id} style={{ whiteSpace: 'nowrap', width: '45%' }}>{label}</label>
                                <input
                                    type={type}
                                    className="form-control"
                                    style={{ width: '55%' }}
                                    id={id}
                                    value={value}
                                    onChange={handleInputChange(setter)}
                                    {...rest}
                                />
                            </div>
                        ))}
                        <div style={{ color: 'gray', fontSize: '1em' }}>
                            <div className='d-flex justify-content-between'>
                                <p>Estimated Fee: </p>
                                <p>${quantity > 0 ? 0.01 : 0}</p>
                            </div>
                            <div className='d-flex justify-content-between'>
                                <p>Estimated Total: </p>
                                <p>${((limitPrice * quantity) + (quantity > 0 ? 0.01 : 0)).toFixed(2)}</p>
                            </div>
                            {activeTab === 'Sell' && (
                                <div className='d-flex justify-content-between'>
                                    <p>Position (Shares): </p>
                                    <p>{totalHoldings}</p>
                                </div>
                            )}
                        </div>
                        <button type="submit" className="btn btn-primary" style={{ width: '100%', marginTop: '15px' }}>
                            {activeTab}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default BuySellAsset;