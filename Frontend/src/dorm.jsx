import React, { useState, useEffect } from 'react';
import dormsData from "../campus.json";
import 'bootstrap/dist/css/bootstrap.min.css';
import './dorm.css';

const DormGrid = ({ hidden }) => {
  const [dorms, setDorms] = useState([]);

  useEffect(() => {
    fetch('../campus.json')
      .then(response => response.json())
      .then(data => setDorms(data))
      .catch(error => console.error(error));
    console.log(dorms);

  }, []);

  return (
    <div hidden={hidden}>
      <div className="container">
        <div className="row">
          {dormsData.dorms.map((dorm) => (
            <div className="col-sm-6 col-md-4 col-lg-3" key={dorm.id}>
              <div className="card">
                <h2>{dorm.name}</h2>
                <p>Type: {dorm.type}</p>
                <p>Rooms: {dorm.rooms.join(", ")}</p>
                <p>Price: {dorm.price.join(", ")}</p>
                <p>Students per suite: {dorm.students_per_suite}</p>
                <p>Number of occupants: {dorm.numOccu}</p>
                <p>Number of floors: {dorm.numFloor}</p>
                <p>Inclusive: {dorm.inclusive}</p>
                <p>Restroom: {dorm.restroom}</p>
                <p>Cleaning: {dorm.cleaning}</p>
                <p>Schedule: {dorm.schedule}</p>
                <p>Furniture:</p>
                <ul>
                  {Object.entries(dorm.furniture).map(([name, value]) => (
                    <li key={name}>
                      {name}: {Array.isArray(value) ? value.join(" ") : value}
                    </li>
                  ))}
                </ul>
                <p>Amenities:</p>
                <ul>
                  {Object.entries(dorm.amenities).map(([name, value]) => (
                    <li key={name}>
                      {name}: {Array.isArray(value) ? value.join(" ") : value}
                    </li>
                  ))}
                </ul>
                <p>Nearby: {dorm.nearby}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default DormGrid;
