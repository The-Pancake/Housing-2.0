import { useState } from 'react';
import ProgressBar from 'react-bootstrap/ProgressBar';
import { Container, Row, Col, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import questionsData from './questions.json';
import "./quiz";
import Layout from './layout';

function QuizQuestions() {
    const [questionIndex, setQuestionIndex] = useState(0);


    const handleNext = () => {
        if (questionIndex < questionsData.length - 1) setQuestionIndex(questionIndex + 1);
    };

    const handlePrevious = () => {
        if (questionIndex > 0) setQuestionIndex(questionIndex - 1);
    };

    const getProgress = () => {
        return (questionIndex / (questionsData.length - 1)) * 100;
    }

    return (
        <>  
            <Layout/>
            <Container className="h-100" id="container" style={{marginTop:"10%"}}>
                <Row className="h-50 justify-content-between align-items-center">
                    <ProgressBar now={getProgress()} style={{marginBottom:"5%"}}/>
                    <Col className="text-center">
                        <h2>{questionsData[questionIndex].question}</h2>
                    </Col>
                </Row>
                <Row className="h-50 justify-content-between align-items-center">
                    <Col className="text-center">
                        <Button style={{ borderRadius: '30px', marginBottom:"3%"}}>{questionsData[questionIndex].answers[0]}</Button>
                    </Col>
                    <Col className="text-center">
                        <Button style={{ borderRadius: '30px', marginBottom:"3%" }}>{questionsData[questionIndex].answers[1]}</Button>
                    </Col>
                </Row>
                <Row className="h-50 justify-content-between align-items-center">
                    <Col className="text-center">
                        <Button style={{ borderRadius: '30px' }}>{questionsData[questionIndex].answers[2]}</Button>
                    </Col>
                    <Col className="text-center">
                        <Button style={{ borderRadius: '30px' }}>{questionsData[questionIndex].answers[3]}</Button>
                    </Col>
                </Row>
                <Row className="mt-5">
                    <Col className="text-center">
                        <Button variant="secondary" onClick={handlePrevious}>Previous</Button>
                    </Col>
                    <Col className="text-center">
                        <Button variant="primary" onClick={handleNext}>Next</Button>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default QuizQuestions;
