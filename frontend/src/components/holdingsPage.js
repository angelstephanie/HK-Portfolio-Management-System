import React from 'react';
import DataTable from './dataTable';
import holdingsData from '../assets/holdings.json';

const holdingsColumns = [
  { header: 'Holding ID', accessor: 'holding_id' },
  { header: 'Portfolio ID', accessor: 'portfolio_id' },
  { header: 'Asset', accessor: 'symbol' },
  { header: 'Quantity', accessor: 'quantity' },
  { header: 'Avg Buy Price', accessor: 'avg_buy_price' }
];

function HoldingsPage() {
  return <DataTable columns={holdingsColumns} data={holdingsData} />;
}

export default HoldingsPage;
