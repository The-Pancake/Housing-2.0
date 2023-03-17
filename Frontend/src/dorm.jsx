import React from 'react';

const DormGrid = ({ dorms }) => {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gridTemplateRows: 'repeat(10, auto)', gridGap: '10px' }}>
      {dorms.map(dorm => (
        <div key={dorm.id} style={{ border: '1px solid #ccc', padding: '10px' }}>
          <h2>{dorm.name}</h2>
          <p>{dorm.description}</p>
        </div>
      ))}
    </div>
  );
};

export default Dorm;