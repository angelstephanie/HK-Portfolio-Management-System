import { Navbar, Nav, Form, FormControl, Dropdown } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const ArgonNavbar = () => {
  return (
    <Navbar expand="md" variant="dark" className="bg-dark py-3 px-4 shadow" id="navbar-main">
      <div className="container-fluid">
        {/* Left-side Nav Links */}
        <Navbar.Brand href="#">
          Portfolio Pro
        </Navbar.Brand>

        <Nav className="me-auto">
          <Nav.Link as={Link} to="/dashboard">Dashboard</Nav.Link>
          <Nav.Link as={Link} to="/holdings">Holdings</Nav.Link>
          <Nav.Link as={Link} to="/transactions">Transactions</Nav.Link>
        </Nav>

        {/* Search form */}
        <Form className="d-none d-md-flex me-3 w-auto" role="search">
        <div className="input-group">
          <span className="input-group-text bg-white border-end-0">
            <i className="fas fa-search text-muted"></i>
          </span>
          <FormControl
            type="search"
            placeholder="Search"
            className="form-control border-start-0"
          />
        </div>
      </Form>


        {/* User Dropdown */}
        <Nav className="d-none d-md-flex align-items-center">
          <Dropdown align="end">
            <Dropdown.Toggle variant="link" className="nav-link pr-0 text-white">
              <div className="media align-items-center">
                <img
                  alt="avatar"
                  src="https://demos.creative-tim.com/argon-dashboard/assets-old/img/theme/team-4.jpg"
                  className="avatar avatar-sm rounded-circle"
                  width="36"
                  height="36"
                />
                <div className="media-body ml-2 d-none d-lg-block">
                  <span className="mb-0 text-sm font-weight-bold">Jessica Jones</span>
                </div>
              </div>
            </Dropdown.Toggle>
            <Dropdown.Menu className="dropdown-menu-right shadow">
              <Dropdown.Header>Welcome!</Dropdown.Header>
              <Dropdown.Item href="#profile">
                <i className="ni ni-single-02 mr-2"></i> My profile
              </Dropdown.Item>
              <Dropdown.Item href="#settings">
                <i className="ni ni-settings-gear-65 mr-2"></i> Settings
              </Dropdown.Item>
              <Dropdown.Item href="#activity">
                <i className="ni ni-calendar-grid-58 mr-2"></i> Activity
              </Dropdown.Item>
              <Dropdown.Item href="#support">
                <i className="ni ni-support-16 mr-2"></i> Support
              </Dropdown.Item>
              <Dropdown.Divider />
              <Dropdown.Item href="#logout">
                <i className="ni ni-user-run mr-2"></i> Logout
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </Nav>
      </div>
    </Navbar>
  );
};

export default ArgonNavbar;
