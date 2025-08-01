import './App.css';
import PortfolioDashboard from './components/dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import ArgonNavbar from './components/navBar';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import HoldingsPage from './components/holdingsPage';
import TransactionsPage from './components/transactionsPage';

function App() {
  return (
      <Router>
        <ArgonNavbar />
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/holdings" element={<HoldingsPage />} />
          <Route path="/transactions" element={<TransactionsPage />} />
          <Route path="/dashboard" element={<PortfolioDashboard />} />
        </Routes>
      </Router>
  );
}

export default App;
