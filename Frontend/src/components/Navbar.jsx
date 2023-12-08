import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import { Link } from 'react-router-dom';
//import { LinkContainer } from 'react-router-bootstrap';

const NavbarLink = () => {
    return (
        <Navbar expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="/">Housing 2.0</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/dorms">Dorms</Nav.Link>
            <Nav.Link href="/faq">FAQ</Nav.Link>
            <Nav.Link href="/quiz">Quiz</Nav.Link>
            <Nav.Link href="/application">Application</Nav.Link>
            <Nav.Link href="/account">Account</Nav.Link>
            <Nav.Link href="/contact">Contact</Nav.Link>

          </Nav>
          <Button variant="outline-success" href="/signup">Signup</Button>
          <Button variant="outline-success" href="/login">Login</Button>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    );
}

export default NavbarLink;