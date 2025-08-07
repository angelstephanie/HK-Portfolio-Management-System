import React, { useMemo, useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
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
        "type": null
    });
    
    const [holdings, setHoldings] = useState({
        "holding_id": null, 
        "totalHoldings": 0
    });

    const [hourlyPrice, setHourlyPrice] = useState([]);
    const [dailyPrice, setDailyPrice] = useState([]);
    const threeYearsAgo = useMemo(() => {
        const today = new Date();
        const date = new Date();
        date.setFullYear(today.getFullYear() - 3);
        return date;
    }, []);

    const formatDate = (date) => {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    };

    const [saved, setSaved] = useState(false);

    // Fetch asset data based on the symbol
    useEffect(() => {
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

    // Fetch total holdings data
    useEffect(() => {
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
            })
            .catch(error => {
                console.log('Error fetching asset data:', error.message);
            });
        }, [symbol, endpoint, holdings]);

    // Fetch asset price for linechart
    useEffect(() => {
        fetch(`${endpoint}/assets/${symbol}/historicprice/5`)
        .then(response => response.json())
        .then(data => { 
            const priceData = [];
            Object.entries(data).forEach(([key, value]) => {
                priceData.push({
                    date: key,
                    price: value
                });
            });
            setHourlyPrice(priceData);
        })
        .catch(error => {
            console.log('Error fetching hourly price data:', error.message);
        });

        fetch(`${endpoint}/assets/${symbol}/historicprice/${formatDate(threeYearsAgo)}`)
        .then(response => response.json())
        .then(data => {
            const priceData = [];
            Object.entries(data).forEach(([key, value]) => {
                priceData.push({
                    date: key,
                    price: value
                });
            });
            setDailyPrice(priceData);
        })
        .catch(error => {
            console.log('Error fetching daily price data:', error.message);
        });
    }, [endpoint, symbol, threeYearsAgo]);


    // Check if the asset is already saved in bookmarks
    useEffect(() => {
        fetch(`${endpoint}/watchlist`)
            .then(response => response.json())
            .then(data => {
                const isSaved = data.some(bookmark => bookmark.symbol === symbol);
                setSaved(isSaved);
            })
            .catch(error => {
                console.log('Error fetching bookmarks:', error.message);
            });
    }, [endpoint, symbol]);

    
    const handleSaveToWatchlist = () => {
        if (saved) {
            //Remove from watchlist
            fetch(`${endpoint}/watchlist/${symbol}`, {
                method: 'DELETE',
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
            })
        } else {
            //Add to watchlist
            fetch(`${endpoint}/watchlist`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({symbol: symbol}),
            }).then(response => {
                if (!response.ok) { 
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
            })
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
                    {(hourlyPrice.length === 0 || dailyPrice.length === 0)
                        ? <p className="card-text">Loading chart data...</p>
                        : <LineChart hourlyData={hourlyPrice} dailyData={dailyPrice} timeSelection={true}/>
                    }
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