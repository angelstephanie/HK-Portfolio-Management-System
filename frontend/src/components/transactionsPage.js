import DataTable from './dataTable';
import transactionsDataJSON from '../assets/transactions.json';
import { Card, Container, Spinner, Alert } from 'react-bootstrap';
import DataFilterBar from './dataFilter';
import { useState, useEffect } from 'react';

const TransactionsPage = () => {
  const [filterInput, setFilterInput] = useState('');
  const [transactionsData, setTransactionsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const columns = [
    { header: 'Asset', accessor: 'symbol' },
    { header: 'Name', accessor: 'name' },
    { header: 'Date', accessor: 'timestamp' },
    { header: 'Quantity', accessor: 'quantity' },
    { header: 'Price/Unit', accessor: 'price_per_unit' },
    { header: 'Fee', accessor: 'fee' },
    { header: 'Type', accessor: 'type' },
    { header: 'Notes', accessor: 'notes' }
  ];

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/transactions');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        const enrichedData = data.map(item => {
            return {
              ...item,  
              quantity: item.quantity.toFixed(2),  
            };
          });
          setTransactionsData(enrichedData);

      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchTransactions();
  }, []);

  return (
    <Container className="py-4">
      <Card className="shadow-sm">
        <Card.Body>
          <h4 className="mb-4">Transactions</h4>

          {loading && (
            <div className="text-center">
              <Spinner animation="border" role="status" />
              <p className="mt-2">Loading transactions...</p>
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
              <DataTable columns={columns} data={transactionsData} globalFilter={filterInput} />
            </>
          )}
        </Card.Body>
      </Card>
    </Container>
  );
};

export default TransactionsPage;
