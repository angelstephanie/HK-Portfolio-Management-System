import DataTable from './dataTable';
import transactionsData from '../assets/transactions.json';
import { Card, Container } from 'react-bootstrap';
import DataFilterBar from './dataFilter';
import { useState } from 'react';

const TransactionsPage = () => {
   const [filterInput, setFilterInput] = useState('');
  
    const columns = [
      { header: 'Portfolio ID', accessor: 'portfolio_id' },
      { header: 'Asset', accessor: 'symbol' },
      { header: 'Date', accessor: 'timestamp' },
      { header: 'Quantity', accessor: 'quantity' },
      { header: 'Price/Unit', accessor: 'price_per_unit' },
      { header: 'Fee', accessor: 'fee' },
      { header: 'Type', accessor: 'type' },
      { header: 'Notes', accessor: 'notes' }
    ];
  
  return (
    <Container className="py-4">
      <Card className="shadow-sm">
        <Card.Body>
          <h4 className="mb-4">Transactions</h4>
          <DataFilterBar filterInput={filterInput} setFilterInput={setFilterInput} />
          <DataTable columns={columns} data={transactionsData} globalFilter={filterInput} />
        </Card.Body>
      </Card>
    </Container>
  );
}

export default TransactionsPage;