import { Row, Col, Form } from 'react-bootstrap';

function editProfile() {
  return (
    <Form>
      <Row>
        <Col md={6}>
          <Form.Group controlId="formInput1">
            <Form.Label>Input 1</Form.Label>
            <Form.Control type="text" placeholder="Enter first value" />
          </Form.Group>
        </Col>
        <Col md={6}>
          <Form.Group controlId="formInput2">
            <Form.Label>Input 2</Form.Label>
            <Form.Control type="text" placeholder="Enter second value" />
          </Form.Group>
        </Col>
      </Row>
    </Form>
  );
}

export default editProfile;
