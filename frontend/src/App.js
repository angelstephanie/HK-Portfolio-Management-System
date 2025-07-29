import './App.css';
import PortfolioDashboard from './components/dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import ArgonNavbar from './components/navBar';

function App() {
  return (
    <div>
      <ArgonNavbar />
      <PortfolioDashboard />
      {/* Additional components can be added here */}
    </div>
  );
}

export default App;
