import React, { useState, useEffect } from 'react';
import dormsData from "../campus.json";
import 'bootstrap/dist/css/bootstrap.min.css';
import './dorm.css';
import { Container, Row, Col } from "react-bootstrap";
import { Modal } from "react-bootstrap";

const DormGrid = ({ hidden }) => {
  const [dorms, setDorms] = useState([]);
  const [showDetails, setShowDetails] = useState(
    Array(dormsData.dorms.length).fill(false)
  );
  const [selectedDorm, setSelectedDorm] = useState(null);

  useEffect(() => {
    fetch('../campus.json')
      .then(response => response.json())
      .then(data => setDorms(data))
      .catch(error => console.error(error));
    console.log(dorms);

  }, []);


  return (
    <div hidden={hidden}>
      <div className="grid-container">
        {dormsData.dorms.map((dorm) => (
          <div className="card" key={dorm.id}>
            <h2>{dorm.name}</h2>
            <p>Type: {dorm.type}</p>
            <button onClick={() => setSelectedDorm(dorm)}>Show more</button>
          </div>
        ))}
      </div>
      <Modal show={selectedDorm !== null} onHide={() => setSelectedDorm(null)}>
        <Modal.Header closeButton>
          <Modal.Title>{selectedDorm?.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Type: {selectedDorm?.type}</p>
          <p>Rooms: {selectedDorm?.rooms.join(", ")}</p>
          <p>Price: {selectedDorm?.price.join(", ")}</p>
          <p>Students per suite: {selectedDorm?.students_per_suite}</p>
          <p>Number of occupants: {selectedDorm?.numOccu}</p>
          <p>Number of floors: {selectedDorm?.numFloor}</p>
          <p>Inclusive: {selectedDorm?.inclusive}</p>
          <p>Restroom: {selectedDorm?.restroom}</p>
          <p>Cleaning: {selectedDorm?.cleaning}</p>
          <p>Schedule: {selectedDorm?.schedule}</p>
          <p>Furniture:</p>
          <ul>
            {Object.entries(selectedDorm?.furniture || {}).map(([name, value]) => (
              <li key={name}>
                {name}: {Array.isArray(value) ? value.join(" ") : value}
              </li>
            ))}
          </ul>
          <p>Amenities:</p>
          <ul>
            {Object.entries(selectedDorm?.amenities || {}).map(([name, value]) => (
              <li key={name}>
                {name}: {Array.isArray(value) ? value.join(" ") : value}
              </li>
            ))}
          </ul>
          <p>Nearby: {selectedDorm?.nearby}</p>
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default DormGrid;
