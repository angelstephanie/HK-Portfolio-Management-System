import { useState, useEffect } from 'react';
import { Card, Container, Spinner, Alert } from 'react-bootstrap';
import DataTable from './dataTable';
import DataFilterBar from './dataFilter';
import holdingsDataJSON from '../assets/holdings.json';
import { useNavigate } from 'react-router-dom';

const HoldingsPage = () => {

  const navigate = useNavigate();

  const handleRowClick = (row) => {
  if (row.symbol) {
    navigate(`/asset/${row.symbol}`);
  }
  };

  const [filterInput, setFilterInput] = useState('');
  const [holdingsData, setHoldingsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const columns = [
    { header: 'Asset', accessor: 'symbol' },
    { header: 'Name', accessor: 'name' },
    { header: 'Asset Type', accessor: 'type' },
    { header: 'Quantity', accessor: 'quantity' },
    { header: 'Avg Buy Price', accessor: 'avg_buy_price' },
    { header: 'Current Price', accessor: 'current_price' },
    { header: 'P&L (Absolute)', accessor: 'pl_absolute' },
    { header: 'P&L (%)', accessor: 'pl_percentage' },
  ];

  useEffect(() => {
      const fetchHoldings = async () => {
        try {
          const response = await fetch('http://127.0.0.1:5000/holdings');
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();

          const enrichedData = data.map(item => {
            const absolutePL = (item.current_price - item.avg_buy_price) * item.quantity;
            const percentagePL = item.avg_buy_price !== 0 
              ? ((item.current_price - item.avg_buy_price) / item.avg_buy_price) * 100 
              : 0;
            return {
              ...item,
              pl_absolute: absolutePL.toFixed(2),  
              quantity: item.quantity.toFixed(2),  
              pl_percentage: `${percentagePL.toFixed(2)}%`
            };
          });
          setHoldingsData(enrichedData);
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
              <DataTable columns={columns} data={holdingsData} globalFilter={filterInput} onRowClick={handleRowClick} />
            </>
          )}
        </Card.Body>
      </Card>
    </Container>
  );
};

export default HoldingsPage;
