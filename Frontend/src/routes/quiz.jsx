import 'bootstrap/dist/css/bootstrap.css';
// import NavbarLink from "../components/Navbar.jsx";
// import NavbarLink from '../components/Navbar.jsx';
import "./Quiz.css";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';

function Quiz() {
    return (
        <>
            <Container fluid className="h-100">
                <Row className="h-100">
                    <Col md={6} className="d-flex justify-content-center align-items-center">
                        <div className="leftDiv">
                            <div className="Motto">
                                <h2 className='roommateText'>
                                    Find <br/>
                                    Your Perfect RPI <br/>
                                    Roommate
                                </h2>
                            </div>
                            <div className='tag'>
                                <h3>Tagline</h3>
                            </div>
                        </div>
                    </Col>
                    <Col md={6} className="d-flex justify-content-center align-items-center">
                        <div className="rightDiv">
                            <img 
                                className="quizImage" 
                                src="https://www.pngmart.com/files/19/Quiz-Logo-PNG-Transparent-Image.png" 
                                alt="Quiz Logo"
                                // style={{height:"30vw"}}
                            />
                        </div>
                    </Col>
                </Row>
                <Button href="/quizQuestions">Go to Quiz</Button>
            </Container>
        </>
    );
}

export default Quiz;
