import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PortfolioDashboard from './components/dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import ArgonNavbar from './components/navBar';
import MyComponent from './components/testing-endpoint/MyComponent';

function App() {
  return (
    <BrowserRouter>
      <div>
        <ArgonNavbar />
        <PortfolioDashboard />
        {/* Additional components can be added here */}
      </div>
      <Routes>
        <Route path="/mycomponent" element={<MyComponent/>} />
        {/* Define other routes here as needed */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
