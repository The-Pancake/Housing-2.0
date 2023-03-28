import React, { useState, useEffect } from 'react';

const DormGrid = ({ hidden }) => {
  const [dorms, setDorms] = useState([]);

  useEffect(() => {
    fetch('../campus.json')
      .then(response => response.json())
      .then(data => setDorms(data))
      .catch(error => console.error(error));

  }, []);

  return (
    <div hidden={hidden}>
      {dorms.length === 0 && <p>Loading dorm data...</p>}
      {dorms.length > 0 && (
        <div className="row row-cols-1 row-cols-md-3 g-4">
          {dorms.map(dorm => (
            <div className="col" key={dorm.id}>
              <div className="card h-100">
                <div className="card-body">
                  <div className="card-body">
                    <h5 className="card-title">{dorm.name}</h5>
                    <ul>
                      {dorm.rooms.map(room => (
                        <li key={room}>{room}</li>
                      ))}
                    </ul>
                    <ul>
                      {dorm.price.map(price => (
                        <li key={price}>{price}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default DormGrid;
