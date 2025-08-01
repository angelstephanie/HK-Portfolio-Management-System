import React from 'react';
import DataTable from './dataTable';
import transactionsData from '../assets/transactions.json';

const transactionsColumns = [
  { header: 'Transaction ID', accessor: 'transaction_id' },
  { header: 'Asset', accessor: 'symbol' },
  { header: 'Date', accessor: 'timestamp' },
  { header: 'Quantity', accessor: 'quantity' },
  { header: 'Price/Unit', accessor: 'price_per_unit' },
  { header: 'Fee', accessor: 'fee' },
  { header: 'Type', accessor: 'type' },
  { header: 'Notes', accessor: 'notes' }
];

function TransactionsPage() {
  return <DataTable columns={transactionsColumns} data={transactionsData} />
}

export default TransactionsPage;