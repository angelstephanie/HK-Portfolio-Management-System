import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import portfolioPerformanceData from '../../assets/portfolio_performance.json';
import LineChart from '../performance-chart/lineChart';
import BuySellAsset from './BuySellAsset';
import bookmarks from '../../assets/bookmark.json';

const Asset = () => {
    const {symbol} = useParams();
    const endpoint = `http://127.0.0.1:5000`;

    const [assetData, setAssetData] = useState({
        "current_price": null, 
        "last_updated": null, 
        "name": null, 
        "opening_price": null, 
        "symbol": null, 
        "type": null
    });
    
    const [holdings, setHoldings] = useState({
        "holding_id": null, 
        "totalHoldings": 0
    });

    const [saved, setSaved] = useState(false);

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
                if (response.ok && holdings.totalHoldings === 0) {
                    return response.json();
                }
                if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
                }
            })
            .then(data => {
                if (holdings.totalHoldings === 0) {
                    data.forEach(holding => {
                        if (holding.symbol === symbol) {
                            setHoldings({
                                holding_id: holding.holding_id,
                                totalHoldings: parseInt(holding.quantity)
                            });
                        }
                    });
                }
                console.log('Asset Data:', assetData);
                console.log('Holdings Data:', holdings);
            })
            .catch(error => {
                console.log('Error fetching asset data:', error.message);
            });
        }, [symbol, endpoint, holdings]);

        useEffect(() => {
            // Check if the asset is already saved in bookmarks
            fetch('../../assets/bookmark.json')
                .then(response => response.json())
                .then(data => {
                    const isSaved = data.some(bookmark => bookmark.symbol === symbol);
                    setSaved(isSaved);
                })
                .catch(error => {
                    console.log('Error fetching bookmarks:', error.message);
                });
        }, [symbol]);

        const handleSaveToWatchlist = () => {
            if (saved) {
                // Remove from bookmarks
                fetch(`${endpoint}/bookmarks/${symbol}`, {
                    method: 'DELETE',
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    console.log('Bookmark removed successfully');
                })
                .catch(error => {
                    console.log('Error removing bookmark:', error.message);
                });
            }
            setSaved(!saved);

        }
    

    return (
        <div className="container py-4">
            {/* Header */}
            <div className="row mb-4">
                <div className="col-12">
                <div className="d-flex justify-content-between align-items-center bg-white">
                    <div>
                    <h6 className="text-uppercase text-muted mb-1" style={{width: 'max-content', letterSpacing: '1px' }}>
                        {assetData.name}
                    </h6>
                    <h2 className="fw-semibold mb-0 text-dark">{assetData.symbol}</h2>
                    </div>
                    <div className='container d-flex justify-content-end align-items-center' style={{paddingRight: '0'}}>
                        <div className="text-end">
                            <h3 className="text-uppercase text-success mb-1" style={{ letterSpacing: '1px' }}>
                                US$ {assetData.current_price}
                            </h3>
                            <h6 className="mb-0 text-success">+4.2%</h6>
                        </div>
                        <div>
                            {/* ADD A SAVE TO WATCHLIST BTN */}
                            <button onClick={handleSaveToWatchlist} style={{ background: 'none', border: 'none', cursor: 'pointer', marginRight: '0'}}>
                                <img src={saved ? require("../../assets/icons/solid_bookmark.svg").default : require("../../assets/icons/regular_bookmark.svg").default} alt="Watchlist Icon" className="ms-2" style={{width: '2.5em'}}/>
                            </button>
                        </div>
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
                    <LineChart chartData={portfolioPerformanceData}/>
                    </div>
                </div>
                </div>
                <div className="col-md-5 mb-4">
                <div className="card shadow-sm">
                    <div className="card-body">
                    <h6 className="card-title">Trade</h6>
                    <BuySellAsset className="card-text" asset={assetData} holdings={holdings}/>
                    </div>
                </div>
                </div>
            </div>
        </div>
    );
}

export default Asset;