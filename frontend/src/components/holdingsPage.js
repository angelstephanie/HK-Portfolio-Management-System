import { useState, useEffect } from 'react';
import { Card, Container, Spinner, Alert } from 'react-bootstrap';
import DataTable from './dataTable';
import DataFilterBar from './dataFilter';
import holdingsDataJSON from '../assets/holdings.json';

const HoldingsPage = () => {
  const [filterInput, setFilterInput] = useState('');
  const [holdingsData, setTransactionsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const columns = [
    { header: 'Portfolio ID', accessor: 'portfolio_id' },
    { header: 'Asset', accessor: 'symbol' },
    { header: 'Quantity', accessor: 'quantity' },
    { header: 'Avg Buy Price', accessor: 'avg_buy_price' },
  ];

  useEffect(() => {
      const fetchHoldings = async () => {
        try {
          const response = await fetch('http://127.0.0.1:5000/holdings');
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();
          setTransactionsData(data);
        } catch (err) {
          setError(err.message);
        } finally {
          setLoading(false);
        }
      };
      fetchHoldings();
    }, []);

  return (
    <Container className="py-4">
      <Card className="shadow-sm">
        <Card.Body>
          <h4 className="mb-4">Holdings</h4>

          {loading && (
            <div className="text-center">
              <Spinner animation="border" role="status" />
              <p className="mt-2">Loading holdings...</p>
            </div>
          )}

          {!loading && error && (
            <Alert variant="danger">
              <strong>Error:</strong> {error}
            </Alert>
          )}

          {!loading && !error && (
            <>
              <DataFilterBar filterInput={filterInput} setFilterInput={setFilterInput} />
              <DataTable columns={columns} data={holdingsData} globalFilter={filterInput} />
            </>
          )}
        </Card.Body>
      </Card>
    </Container>
  );
};

export default HoldingsPage;
