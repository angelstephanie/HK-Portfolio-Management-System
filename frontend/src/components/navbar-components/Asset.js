import React, { useMemo, useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import LineChart from '../performance-chart/lineChart';
import BuySellAsset from './BuySellAsset';

const Asset = () => {
    const { symbol } = useParams();
    const endpoint = `http://127.0.0.1:5000`;

    const [assetData, setAssetData] = useState({
        current_price: null,
        last_updated: null,
        name: null,
        opening_price: null,
        symbol: null,
        type: null,
    });

    const [holdings, setHoldings] = useState({
        holding_id: null,
        totalHoldings: 0,
    });

    const [hourlyPrice, setHourlyPrice] = useState([]);
    const [dailyPrice, setDailyPrice] = useState([]);
    const [saved, setSaved] = useState(false);

    const [loading, setLoading] = useState({
        asset: true,
        holdings: true,
        prices: true,
        watchlist: true,
    });

    const [error, setError] = useState({
        asset: null,
        holdings: null,
        prices: null,
        watchlist: null,
    });

    const threeYearsAgo = useMemo(() => {
        const date = new Date();
        date.setFullYear(date.getFullYear() - 3);
        return date;
    }, []);

    const formatDate = (date) => {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    };

    useEffect(() => {
        setLoading(prev => ({ ...prev, asset: true }));
        fetch(`${endpoint}/assets/${symbol}`)
            .then(response => {
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                return response.json();
            })
            .then(data => {
                setAssetData(data);
                setError(prev => ({ ...prev, asset: null }));
            })
            .catch(err => {
                setError(prev => ({ ...prev, asset: err.message }));
            })
            .finally(() => {
                setLoading(prev => ({ ...prev, asset: false }));
            });
    }, [symbol, endpoint]);

    useEffect(() => {
        setLoading(prev => ({ ...prev, holdings: true }));
        fetch(`${endpoint}/holdings/1`)
            .then(response => {
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                return response.json();
            })
            .then(data => {
                const found = data.find(h => h.symbol === symbol);
                if (found) {
                    setHoldings({
                        holding_id: found.holding_id,
                        totalHoldings: parseInt(found.quantity),
                    });
                }
                setError(prev => ({ ...prev, holdings: null }));
            })
            .catch(err => {
                setError(prev => ({ ...prev, holdings: err.message }));
            })
            .finally(() => {
                setLoading(prev => ({ ...prev, holdings: false }));
            });
    }, [symbol, endpoint]);

    useEffect(() => {
        setLoading(prev => ({ ...prev, prices: true }));
        Promise.all([
            fetch(`${endpoint}/assets/${symbol}/historicprice/5`).then(res => res.json()),
            fetch(`${endpoint}/assets/${symbol}/historicprice/${formatDate(threeYearsAgo)}`).then(res => res.json())
        ])
        .then(([hourData, dayData]) => {
            const formatPriceData = (data) => Object.entries(data).map(([key, val]) => ({ date: key, price: val }));
            setHourlyPrice(formatPriceData(hourData));
            setDailyPrice(formatPriceData(dayData));
            setError(prev => ({ ...prev, prices: null }));
        })
        .catch(err => {
            setError(prev => ({ ...prev, prices: err.message }));
        })
        .finally(() => {
            setLoading(prev => ({ ...prev, prices: false }));
        });
    }, [endpoint, symbol, threeYearsAgo]);

    useEffect(() => {
        setLoading(prev => ({ ...prev, watchlist: true }));
        fetch(`${endpoint}/watchlist`)
            .then(response => response.json())
            .then(data => {
                const isSaved = data.some(bookmark => bookmark.symbol === symbol);
                setSaved(isSaved);
                setError(prev => ({ ...prev, watchlist: null }));
            })
            .catch(err => {
                setError(prev => ({ ...prev, watchlist: err.message }));
            })
            .finally(() => {
                setLoading(prev => ({ ...prev, watchlist: false }));
            });
    }, [endpoint, symbol]);

    const handleSaveToWatchlist = () => {
        const method = saved ? 'DELETE' : 'POST';
        const url = saved ? `${endpoint}/watchlist/${symbol}` : `${endpoint}/watchlist`;
        const body = saved ? null : JSON.stringify({ symbol });

        fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body,
        })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            setSaved(!saved);
        })
        .catch(err => {
            alert(`Error updating watchlist: ${err.message}`);
        });
    };

    return (
        <div className="container py-4">
            {/* Header */}
            <div className="row mb-4">
                <div className="col-12">
                    <div className="d-flex justify-content-between align-items-center bg-white">
                        <div>
                            <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                                {loading.asset ? "Loading..." : assetData.name}
                            </h6>
                            <h2 className="fw-semibold mb-0 text-dark">{assetData.symbol}</h2>
                        </div>
                        <div className="d-flex align-items-center">
                            <div className="text-end me-2">
                                <h3 className={`text-uppercase ${assetData.current_price >= assetData.opening_price ? 'text-success' : 'text-danger'} mb-1`}>
                                    {loading.asset ? "..." : `US$ ${assetData.current_price}`}
                                </h3>
                                <h6 className={assetData.current_price >= assetData.opening_price ? 'text-success' : 'text-danger'}>
                                    {loading.asset ? "" :
                                        `${assetData.opening_price !== 0 ? (((assetData.current_price - assetData.opening_price)/assetData.opening_price) * 100).toFixed(2) : 0}%`}
                                </h6>
                            </div>
                            <button onClick={handleSaveToWatchlist} style={{ background: 'none', border: 'none', cursor: 'pointer' }}>
                                <img
                                    src={saved ? require("../../assets/icons/solid_bookmark.svg").default : require("../../assets/icons/regular_bookmark.svg").default}
                                    alt="Watchlist Icon"
                                    style={{ width: '2.5em' }}
                                />
                            </button>
                        </div>
                    </div>
                    {error.asset && <p className="text-danger mt-2">Error loading asset: {error.asset}</p>}
                </div>
            </div>

            {/* Main content */}
            <div className="row mt-4">
                <div className="col-md-7 mb-4">
                    <div className="card shadow-sm">
                        <div className="card-body">
                            <h6 className="card-title">Performance Chart</h6>
                            {loading.prices
                                ? <p className="text-muted">Loading chart data...</p>
                                : error.prices
                                    ? <p className="text-danger">Error loading chart: {error.prices}</p>
                                    : <LineChart hourlyData={hourlyPrice} dailyData={dailyPrice} timeSelection={true} />
                            }
                        </div>
                    </div>
                </div>

                <div className="col-md-5 mb-4">
                    <div className="card shadow-sm">
                        <div className="card-body">
                            <h6 className="card-title">Trade</h6>
                            {loading.holdings
                                ? <p className="text-muted">Loading holdings...</p>
                                : error.holdings
                                    ? <p className="text-danger">Error loading holdings: {error.holdings}</p>
                                    : <BuySellAsset className="card-text" asset={assetData} holdings={holdings} />
                            }
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Asset;
