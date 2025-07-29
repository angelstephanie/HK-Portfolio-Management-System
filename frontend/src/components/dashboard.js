import React from 'react';

export default function PortfolioDashboard() {
  return (
    <div className="min-h-screen p-4 bg-gray-100">
      {/* Top Navigation Bar */}
      <div className="flex justify-between items-center bg-white p-4 rounded shadow">
        <div className="space-x-4">
          <button>Dashboard</button>
          <button>Holdings</button>
          <button>Transactions</button>
          <button>Settings</button>
        </div>
        <input
          type="text"
          placeholder="Search for investments..."
          className="border px-3 py-1 rounded"
        />
        <div className="border rounded-full px-4 py-1">User</div>
      </div>

      {/* Portfolio Summary */}
      <div className="text-center text-lg font-semibold my-4">
        Total Portfolio Value: $1.8M | P&amp;L: +4.2%
      </div>

      {/* Middle Section */}
      <div className="grid grid-cols-3 gap-4 mb-4">
        {/* Pie Chart and Filter */}
        <div className="bg-white p-4 rounded shadow col-span-1">
          <div className="flex justify-between items-center mb-2">
            <span>List</span> | <span>Pie</span>
          </div>
          <div className="h-40 flex items-center justify-center border rounded">
            Pie chart for total portfolio by {'<filter>'}
          </div>
          <div className="mt-4 text-center text-sm text-gray-600">
            ⇦ Filter by: (asset type, gain, asset amount, etc.) ⇨
          </div>
        </div>

        {/* Top Movers Section */}
        <div className="bg-white p-4 rounded shadow col-span-1">
          <div className="mb-2">Top Movers | Top Gainers | Top Losers</div>
          <div className="h-40 flex items-center justify-center text-sm text-gray-600">
            From Sumer and Lareb
          </div>
        </div>

        {/* Watchlists Performance */}
        <div className="bg-white p-4 rounded shadow col-span-1">
          <div className="text-lg font-medium mb-2">Watchlists Performance</div>
          <ul className="list-disc list-inside text-gray-700">
            <li>one</li>
            <li>two</li>
            <li>three</li>
          </ul>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="grid grid-cols-2 gap-4">
        {/* Recent Activity Feed */}
        <div className="bg-white p-4 rounded shadow">
          <div className="text-lg font-medium mb-2">Recent Activity Feed</div>
          <div className="text-sm text-gray-600">Date | Action | Ticker | Qty | Price</div>
          {/* Add dynamic rows later */}
        </div>

        {/* Performance Line Chart */}
        <div className="bg-white p-4 rounded shadow">
          <div className="text-lg font-medium mb-2">Performance Line Chart</div>
          <ul className="text-sm text-gray-600">
            <li>Portfolio vs Benchmark over selected period</li>
            <li>Toggle: 1W, 1M, 3M, YTD, 1Y, 5Y</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
