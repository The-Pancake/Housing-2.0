import React, { useState, useEffect } from 'react';
import dormsData from "../campus.json";

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
        <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
          {dormsData.dorms.map((dorm) => (
            <div className="col" key={dorm.id}>
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{dorm.name}</h5>
                  <p className="card-text">Type: {dorm.type}</p>
                  <p className="card-text">Rooms: {dorm.rooms.join(", ")}</p>
                  <p className="card-text">Price: {dorm.price.join(", ")}</p>
                  <p className="card-text">Students per suite: {dorm.students_per_suite}</p>
                  <p className="card-text">Number of occupants: {dorm.numOccu}</p>
                  <p className="card-text">Number of floors: {dorm.numFloor}</p>
                  <p className="card-text">Inclusive: {dorm.inclusive}</p>
                  <p className="card-text">Restroom: {dorm.restroom}</p>
                  <p className="card-text">Cleaning: {dorm.cleaning}</p>
                  <p className="card-text">Schedule: {dorm.schedule}</p>
                  <p className="card-text">Furniture:</p>
                  <ul className="card-text">
                    {Object.entries(dorm.furniture).map(([name, value]) => (
                      <li key={name}>
                        {name}: {Array.isArray(value) ? value.join(" ") : value}
                      </li>
                    ))}
                  </ul>
                  <p className="card-text">Amenities:</p>
                  <ul className="card-text">
                    {Object.entries(dorm.amenities).map(([name, value]) => (
                      <li key={name}>
                        {name}: {Array.isArray(value) ? value.join(" ") : value}
                      </li>
                    ))}
                  </ul>
                  <p className="card-text">Nearby: {dorm.nearby}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default DormGrid;
