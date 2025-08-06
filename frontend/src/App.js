import './App.css';
import PortfolioDashboard from './components/dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import ArgonNavbar from './components/navBar';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import HoldingsPage from './components/holdingsPage';
import TransactionsPage from './components/transactionsPage';
import Asset from './components/navbar-components/Asset';

function App() {
  return (
      <Router>
        <ArgonNavbar />
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<PortfolioDashboard />} />
          <Route path="/holdings" element={<HoldingsPage />} />
          <Route path="/transactions" element={<TransactionsPage />} />
          <Route path="/asset/:symbol" element={<Asset />} />
          {/* Define other routes here as needed */}
        </Routes>
      </Router>
  );
}

export default App;
