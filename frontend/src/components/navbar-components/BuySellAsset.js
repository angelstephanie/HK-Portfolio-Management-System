import React, { useEffect, useState } from 'react';
import { format } from 'date-fns';

const BuySellAsset = ({price}) => {
    const dateObject = new Date();
    const [activeTab, setActiveTab] = useState('Buy');
    const [limitPrice, setLimitPrice] = useState('');
    const [quantity, setQuantity] = useState(1);
    const [dateTime, setDateTime] = useState(format(dateObject, "yyyy-MM-dd'T'HH:mm"));

    const handlePriceChange = (event) => {
        setLimitPrice(event.target.value);
    };
    const handleQuantityChange = (event) => {
        setQuantity(event.target.value);    
    };
    const handleDateTimeChange = (event) => {
        setDateTime(event.target.value);
    };
    const handleSubmission = (event) => {
        event.preventDefault();
        console.log(`Submitting ${activeTab} with Price: ${limitPrice}, Quantity: ${quantity}, DateTime: ${dateTime}`);
    };

    useEffect(() => {   
        setLimitPrice(price);
    }, [price]);

    return (
    <div className="top-movers-inner">
        <ul className="nav nav-tabs mb-3 mt-2">
            <li className="nav-item">
            <button
                className={`nav-link ${activeTab === 'Buy' ? 'active' : ''}`}
                onClick={() => setActiveTab('Buy')}
            >
                Buy
            </button>
            </li>
            <li className="nav-item">
            <button
                className={`nav-link ${activeTab === 'Sell' ? 'active' : ''}`}
                onClick={() => setActiveTab('Sell')}
            >
                Sell
            </button>
            </li>
        </ul>
        <div className="chart-container" style={{ height: '200px', padding: '10px' }}>
            <form onSubmit={handleSubmission}>
                <div className="form-group mb-3">
                    <label className="mb-1">Limit Price (US$)</label>
                    <input type="number" className="form-control" id="limitPrice" step="0.01" min="0" value={limitPrice} onChange={handlePriceChange}/>
                </div>
                    <div className="form-group mb-3">
                        <label className="mb-1">Quantity</label>
                        <input type="number" className="form-control" id="quantity" step="1" min="0" value={quantity} onChange={handleQuantityChange}/>
                    </div>
                    <div className="form-group mb-3">
                        <label className="mb-1">Date Time</label>
                        <br/>
                        <input
                            type="datetime-local"
                            className="form-control"
                            id="dateTime"
                            name="datetime-local-input"
                            value={dateTime}
                            onChange={handleDateTimeChange}
                            style={{ width: '100%' }}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary" style={{width: '100%', marginTop: '15px'}}>{activeTab}</button>
            </form>
        </div>
    </div>
    );
};

export default BuySellAsset;