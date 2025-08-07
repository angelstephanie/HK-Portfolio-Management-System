import React from 'react';
import Watchlist from './watchlist/Watchlist';
import PerformanceChart from './performance-chart/PerformanceChart';
import PortfolioPieChart from './portfolioPieChart';
import TopMovers from './topMovers';
import RecentActivityFeed from './recentActivity/recentActivity';
import { useState, useEffect } from 'react';
import { Form, Spinner, Alert } from 'react-bootstrap';

export default function PortfolioDashboard() {

  const [portfolios, setPortfolios] = useState([]);
  const [holdings, setHoldings] = useState([]);
  const [selectedPortfolioId, setSelectedPortfolioId] = useState(null);
  const [portfolioSnaps, setPortfolioSnaps] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const portfolioRes = await fetch('http://127.0.0.1:5000/portfolios');
        const holdingsRes = await fetch('http://127.0.0.1:5000/holdings');
        const portfolioSnapsRes = await fetch('http://127.0.0.1:5000/portfolio_snaps');

        if (!portfolioRes.ok || !holdingsRes.ok) {
          throw new Error('Failed to fetch portfolio or holdings data.');
        }

        const portfoliosData = await portfolioRes.json();
        const holdingsData = await holdingsRes.json();
        const portfolioSnapsData = await portfolioSnapsRes.json();

        setPortfolios(portfoliosData);
        setHoldings(holdingsData);
        setPortfolioSnaps(portfolioSnapsData);

        if (portfoliosData.length > 0) {
          setSelectedPortfolioId(portfoliosData[0].portfolio_id);
        }

        setLoading(false);
      } catch (err) {
        setError('Something went wrong while loading data.');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handlePortfolioChange = (e) => {
    setSelectedPortfolioId(Number(e.target.value));
  };

  return (
    <div className="container py-4">
      {/* Summary */}
      <div className="row mb-4">
        <div className="col-12">
          <div className="d-flex align-items-center bg-white p-4 rounded shadow-sm border">
            {loading ? (
              <Spinner animation="border" />
            ) : error ? (
              <Alert variant="danger" className="w-100 mb-0">
                {error}
              </Alert>
            ) : (
              <>
                <div className="d-flex align-items-center gap-5">
                  <div>
                    <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                      Total Portfolio Value
                    </h6>
                    <h2 className="fw-semibold mb-0 text-dark">
                      18000000
                    </h2>
                  </div>

                  <div>
                    <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                      P&L
                    </h6>
                    <h5 className={`mb-0 ${20 >= 0 ? 'text-success' : 'text-danger'}`}>
                      {20 >= 0 ? '+' : ''}
                      20%
                    </h5>
                  </div>
                </div>

                 <div className="ms-auto">
                  <Form.Label>Select Portfolio</Form.Label>
                  <Form.Select
                    value={selectedPortfolioId}
                    onChange={handlePortfolioChange}
                    style={{ width: '250px' }}
                  >
                    {portfolios.map(p => (
                      <option key={p.portfolio_id} value={p.portfolio_id}>
                        {p.portfolio_id}
                      </option>
                    ))}
                  </Form.Select>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      {!loading && !error && (
      <>
      <div className="row mb-4">
        <div className="col-md-6 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Asset Allocation</h5>
              <PortfolioPieChart 
                portfolioId={selectedPortfolioId}
                holdings={holdings} 
              />
            </div>
          </div>
        </div>
        <div className="col-md-6 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Performance Chart</h5>
              <PerformanceChart portfolioSnaps={portfolioSnaps} />
            </div>
          </div>
        </div>
      </div>

      {/* Second Row: Portfolio Top Movers, Watchlist, Recent Activity Feed */}
      <div className="row">
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Portfolio Top Movers</h5>
              <TopMovers />
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Your Watchlist</h5>
              <p style={{ fontSize: '1rem', color: '#555', marginBottom: '20px' }}>
                Add to your watchlist to track their performance.
              </p>
              <Watchlist />
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Recent Activity Feed</h5>
              {/* <RecentActivityFeed /> */}
              <p> </p>
            </div>
          </div>
        </div>
      </div>
      </>
      )}
    </div>
  );
}
