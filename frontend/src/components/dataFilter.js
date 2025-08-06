import { Form, Row, Col, Button } from 'react-bootstrap';

function DataFilterBar({ filterInput, setFilterInput }) {
  const handleInputChange = (e) => setFilterInput(e.target.value);

  return (
    <Form className="mb-3" onSubmit={(e) => e.preventDefault()}>
        <Row className="align-items-center">
            <Col xs={8}>
            <Form.Control
                type="text"
                placeholder="Search..."
                value={filterInput}
                onChange={handleInputChange}
            />
            </Col>
            <Col>
            <Button variant="secondary" onClick={() => setFilterInput('')}>
                Clear
            </Button>
            </Col>
        </Row>
    </Form>
  );
}

export default DataFilterBar;
