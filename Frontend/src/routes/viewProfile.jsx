import { Row, Col, Form } from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css";

export default function ViewProfile() {
  return (
    <>
    <Form style={{marginTop:"9%"}}>
      <Row>
        <Col md={6}>
          <Form.Group controlId="formFirstName">
            <Form.Label>First Name</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter first name"/>
          </Form.Group>
        </Col>
        <Col md={6}>
          <Form.Group controlId="formLastName">
            <Form.Label>Last Name</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter last name" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={6}>
          <Form.Group controlId="formEmail">
            <Form.Label>Email</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter email" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Interest One</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Interest Two</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Interest Three</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col>
          <Form.Group controlId="formInstagramUsername">
            <Form.Label>Instagram Username</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter username" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Living Style</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Sleep Schedule</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Favorite Food</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Favorite Drink</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Do you smoke?</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Do you have pets?</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Guest Frequency</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Preferred room temp</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Live With Same Gender</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Similar Age Pref</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Dietary Restrictions</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Cook or Eat Out</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Overnight Guests</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>House/Apartment</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>City or Suburbs</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Form.Group controlId="formInterestOne">
            <Form.Label>Furnished/Unfurnished</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest one" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestTwo">
            <Form.Label>Do you have a car?</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest two" />
          </Form.Group>
        </Col>
        <Col md={4}>
          <Form.Group controlId="formInterestThree">
            <Form.Label>Solo bathroom</Form.Label>
            <Form.Control readOnly={true} type="text" placeholder="Enter interest three" />
          </Form.Group>
        </Col>
      </Row>
    </Form>
    </>
  );
}
