import { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import questions from './quiz.json';

const RoommatePairing = ({ hidden }) => {
  const [progress, setProgress] = useState(0);
  const [answers, setAnswers] = useState([]);

  const handleAnswer = (answer) => {
    setProgress(progress + 1);
    setAnswers([...answers.slice(0, progress), answer]);
    const radios = document.getElementsByName('answer');
    for (let i = 0; i < radios.length; i++) {
      radios[i].checked = false;
    }
  };

  const handleRedo = () => {
    setProgress(0);
    setAnswers([]);
  };

  const currentQuestion = questions[progress];
  return (
    <div hidden={hidden}>
      <div className="row">
        <div className="col-lg-8 offset-lg-2">
          <div className="progress mt-5 mb-5 bg-light">
            <div
              className="progress-bar bg-primary"
              role="progressbar"
              style={{ width: `${(progress / questions.length) * 100}%` }}
              aria-valuenow={progress}
              aria-valuemin="0"
              aria-valuemax={questions.length}
            ></div>
          </div>
          {currentQuestion && (
            <Form
              className="mt-5 mb-5 text-white"
              style={{ backgroundColor: 'rgba(33, 37, 41, 0.65)' }}
            >
              <Form.Group>
                <Form.Label className="h5 m-0">{currentQuestion.question}</Form.Label>
                {currentQuestion.answer.map((choice) => (
                  <Form.Check
                    type="radio"
                    label={choice}
                    name="answer"
                    onChange={() => handleAnswer(choice)}
                    className="h5 m-2 my-3"
                  />
                ))}
              </Form.Group>
            </Form>
          )}
          <Button onClick={handleRedo} variant="primary" size="lg" className="mt-3">
            Redo
          </Button>
        </div>
      </div>
    </div>
  );
};

export default RoommatePairing;