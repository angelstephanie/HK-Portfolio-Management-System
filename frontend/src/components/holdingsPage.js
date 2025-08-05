import { useState } from 'react';
import { Card, Container } from 'react-bootstrap';
import DataTable from './dataTable';
import DataFilterBar from './dataFilter';
import holdingsData from '../assets/holdings.json';

const HoldingsPage = () => {
  const [filterInput, setFilterInput] = useState('');

  const columns = [
    { header: 'Portfolio ID', accessor: 'portfolio_id' },
    { header: 'Asset', accessor: 'symbol' },
    { header: 'Quantity', accessor: 'quantity' },
    { header: 'Avg Buy Price', accessor: 'avg_buy_price' },
  ];

  return (
    <Container className="py-4">
      <Card className="shadow-sm">
        <Card.Body>
          <h4 className="mb-4">Holdings</h4>
          <DataFilterBar filterInput={filterInput} setFilterInput={setFilterInput} />
          <DataTable columns={columns} data={holdingsData} globalFilter={filterInput} />
        </Card.Body>
      </Card>
    </Container>
  );
};

export default HoldingsPage;
