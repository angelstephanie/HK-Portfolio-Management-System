import React from 'react';
import Watchlist from './watchlist/Watchlist';
import PortfolioPieChart from './portfolioPieChart';
import TopMovers from './topMovers';

export default function PortfolioDashboard() {
  return (
    <div className="container py-4">
      {/* Summary */}
      <div className="row mb-4">
        <div className="col-12">
          <div className="d-flex justify-content-between align-items-center bg-white p-4 rounded shadow-sm border">
            <div>
              <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                Total Portfolio Value
              </h6>
              <h2 className="fw-semibold mb-0 text-dark">$1,800,000</h2>
            </div>
            <div className="text-end">
              <h6 className="text-uppercase text-muted mb-1" style={{ letterSpacing: '1px' }}>
                P&L
              </h6>
              <h5 className="mb-0 text-success">+4.2%</h5>
            </div>
          </div>
        </div>
      </div>

      {/* Main Cards */}
      <div className="row">
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Asset Allocation</h5>
              <PortfolioPieChart/>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Market Top Movers</h5>
              <TopMovers/>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Watchlist Performance</h5>
              <Watchlist/>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Row */}
      <div className="row">
        <div className="col-md-6 mb-4">
          <div className="card shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Recent Activity Feed</h5>
              <p className="text-muted">[Table Placeholder]</p>
            </div>
          </div>
        </div>
        <div className="col-md-6 mb-4">
          <div className="card shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Performance Chart</h5>
              <p className="text-muted">[Line Chart Placeholder]</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
