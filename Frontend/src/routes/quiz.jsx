import 'bootstrap/dist/css/bootstrap.css';
import "./Quiz.css";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Layout from './layout';

function Quiz() {
    return (
        <>
            <Layout/>
            <Container fluid className="h-100" style={{ marginTop: "5%" }}>
                <Row className="h-100">
                    <Col md={6} className="d-flex justify-content-center align-items-center">
                        <div >
                            <div className="Motto">
                                <h2 className='roommateText'>
                                    Find <br />
                                    Your Perfect RPI <br />
                                    Roommate
                                </h2>
                            </div>
                            <div className='tag'>
                                <h3>Tagline</h3>
                            </div>
                        </div>
                    </Col>
                    <Col md={6} className="d-flex justify-content-center align-items-center">
                        <div >
                            <img 
                                className="quizImage" 
                                src="https://www.pngmart.com/files/19/Quiz-Logo-PNG-Transparent-Image.png" 
                                alt="Quiz Logo"
                                style={{ height: "30vw", maxWidth: "100%" }}
                            />
                        </div>
                    </Col>
                </Row>
                <Row className="justify-content-center mt-3">
                    <Col md={12} className="d-flex justify-content-center">
                        <Button href="/quizQuestions" className="btn-lg" style={{background:"3AB8FF"}}>Take Roommate Quiz</Button>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default Quiz;
