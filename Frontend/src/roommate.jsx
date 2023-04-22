import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';



const Roommates = ({hidden}) => {

  const handleButtonClick = () => {
    history.push('/roommate-pairing');
  };
  const personalInfo = {
    name: 'Your Name',
    interests: ['Interest 1', 'Interest 2', 'Interest 3'],
    contact: 'your.email@example.com'
  };

  const potentialRoommates = [
    {
      name: 'Roommate 1',
      interests: ['Interest 1', 'Interest 2', 'Interest 3'],
      contact: 'roommate1.email@example.com',
      match_rate: 0.75
    },
    {
      name: 'Roommate 2',
      interests: ['Interest 1', 'Interest 2', 'Interest 3'],
      contact: 'roommate2.email@example.com',
        match_rate: 0.6

    },
    {
      name: 'Roommate 3',
      interests: ['Interest 1', 'Interest 2', 'Interest 3'],
      contact: 'roommate3.email@example.com',
        match_rate: 0.5
    }
  ];

  return (
    <div className="container p-4 my-5" style={{
      backgroundColor: 'rgba(33, 37, 41, 0.65)',
      borderRadius: '10px',
      width: '50%'
    }} hidden={hidden}>
      <p className={'text-center fs-1 text-white'}>Personal Information</p>
      <div className="card mb-4 text-white" style={{ width: '100%' , backgroundColor: 'rgba(33, 37, 41, 0.65)'}}>
        <div className="card-body">
          <h5 className="card-title">{personalInfo.name}</h5>
          <p className="card-text"><strong>Interests:</strong> {personalInfo.interests.join(', ')}</p>
          <p className="card-text"><strong>Contact:</strong> {personalInfo.contact}</p>
        </div>
      </div>

      <h2 className="my-4 text-white">Potential Roommates</h2>
      <div className="row">
        {potentialRoommates.map((roommate, index) => (
          <div key={index} className="col-md-6">
            <div className="card mb-4 text-white" style={{ width: '100%', backgroundColor: 'rgba(33, 37, 41, 0.65)' }}>
              <div className="card-body">
                <h5 className="card-title">{roommate.name}</h5>
                <p className="card-text"><strong>Interests:</strong> {roommate.interests.join(', ')}</p>
                <p className="card-text"><strong>Contact:</strong> {roommate.contact}</p>
                <p className="card-text"><strong>Match Rate:</strong> {roommate.match_rate*100+"%"}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <p className={"fs-4 text-white"}> Take the quiz to find your perfect roommate! </p>
    </div>
  );
};

export default Roommates;