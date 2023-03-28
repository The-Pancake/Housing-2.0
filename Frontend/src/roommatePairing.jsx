import React, { useState } from 'react';
import { ProgressBar, Form, Button } from 'react-bootstrap';

const RoommatePairing = ({ hidden }) => {
  const [progress, setProgress] = useState(0);
  const [answers, setAnswers] = useState([]);

  const questions = [
    {
      text: "What's your living style?",
      choices: ["Neat and tidy", "Relaxed and casual", "A bit of both"]
    },
    {
      text: "What time do you usually wake up?",
      choices: ["Early bird", "Night owl", "It varies"]
    },
    {
        text: "What's your favorite food?",
        choices: ["Chinese", "Japanese", "Korean", "Western", "Indian", "Thai", "Vietnamese", "Other"]
    },
    {
        text: "What's your favorite drink?",
        choices: ["Coffee", "Tea", "Juice", "Milk", "Water", "Other"]
    }
    // Add 10 more questions here
  ];

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
      <ProgressBar now={progress / questions.length * 100} />
      {currentQuestion && (
        <Form>
          <Form.Label>{currentQuestion.text}</Form.Label>
          {currentQuestion.choices.map((choice) => (
            <Form.Check
              type="radio"
              label={choice}
              name="answer"
              onChange={() => handleAnswer(choice)}
            />
          ))}
        </Form>
      )}
      <Button onClick={handleRedo}>Redo</Button>
    </div>
  );
};

export default RoommatePairing;