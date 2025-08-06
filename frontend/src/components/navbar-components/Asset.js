import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import portfolioPerformanceData from '../../assets/portfolio_performance.json';
import LineChart from '../performance-chart/lineChart';
import BuySellAsset from './BuySellAsset';

const Asset = () => {
    const {symbol} = useParams();
    const endpoint = `http://127.0.0.1:5000`;

    const [assetData, setAssetData] = useState({
        "current_price": null, 
        "last_updated": null, 
        "name": null, 
        "opening_price": null, 
        "symbol": null, 
        "type": null,
        "holding_id": null});
    
    const [totalHoldings, setTotalHoldings] = useState(0);

    useEffect(() => {
        // Fetch asset data based on the symbol
        fetch(`${endpoint}/assets/${symbol}`)
            .then(response => {
                if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                setAssetData(data);
            })
            .catch(error => {
                console.log('Error fetching asset data:', error.message);
            });
        }, [symbol, endpoint]);

    useEffect(() => {
        // Fetch total holdings data
        fetch(`${endpoint}/holdings/1`)
            .then(response => {
                if (response.ok && totalHoldings === 0) {
                    return response.json();
                }
                if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
                }
            })
            .then(data => {
                if (totalHoldings === 0) {
                    console.log('Holdings Data:', data);
                    let noHoldings = 0;
                    data.forEach(holding => {
                        if (holding.symbol === symbol) {

                            noHoldings += parseInt(holding.quantity);
                            console.log(`Holdings for ${symbol}:`, noHoldings);
                        }
                    });
                    setTotalHoldings(noHoldings);
                }
                console.log('Total Holdings:', totalHoldings);
            })
            .catch(error => {
                console.log('Error fetching asset data:', error.message);
            });
        }, [symbol, endpoint, totalHoldings]);

        // useEffect(() => {
        //     // Fetch total holdings data
        //     fetch(`${endpoint}/assets/${symbol}/historicprice/${}`)
        //         .then(response => {
        //             if (response.ok && totalHoldings === 0) {
        //                 return response.json();
        //             }
        //             if (!response.ok) {
        //             throw new Error(`HTTP error! status: ${response.status}`);
        //             }
        //         })
        //         .then(data => {
        //             if (totalHoldings === 0) {
        //                 console.log('Holdings Data:', data);
        //                 let noHoldings = 0;
        //                 data.forEach(holding => {
        //                     if (holding.symbol === symbol) {
        //                         noHoldings += parseInt(holding.quantity);
        //                         console.log(`Holdings for ${symbol}:`, noHoldings);
        //                     }
        //                 });
        //                 setTotalHoldings(noHoldings);
        //             }
        //             console.log('Total Holdings:', totalHoldings);
        //         })
        //         .catch(error => {
        //             console.log('Error fetching asset data:', error.message);
        //         });
        //     }, [symbol, endpoint]);

    return (
        <div className="container py-4">
            {/* Header */}
            <div className="row mb-4">
                <div className="col-12">
                <div className="d-flex justify-content-between align-items-center bg-white">
                    <div>
                    <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                        {assetData.name}
                    </h6>
                    {/* ADD A SAVE TO WATCHLIST BTN */}
                    <h2 className="fw-semibold mb-0 text-dark">{assetData.symbol}</h2>
                    </div>
                    <div className="text-end">
                    <h3 className="text-uppercase text-success mb-1" style={{ letterSpacing: '1px' }}>
                        US$ {assetData.current_price}
                    </h3>
                    <h6 className="mb-0 text-success">+4.2%</h6>
                    </div>
                </div>
                </div>
            </div>
            {/* Render asset data here */}
            <div className="row mt-4">
                <div className="col-md-7 mb-4">
                <div className="card shadow-sm">
                    <div className="card-body">
                    <h6 className="card-title">Performance Chart</h6>
                    <LineChart chartData={portfolioPerformanceData} />
                    </div>
                </div>
                </div>
                <div className="col-md-5 mb-4">
                <div className="card shadow-sm">
                    <div className="card-body">
                    <h6 className="card-title">Trade</h6>
                    <BuySellAsset className="card-text" asset={assetData} totalHoldings={totalHoldings}/>
                    </div>
                </div>
                </div>
            </div>
        </div>
    );
}

export default Asset;