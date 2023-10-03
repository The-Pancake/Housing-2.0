import { useLocation } from 'react-router-dom';

export default function Application() {
  const location = useLocation();
  const firstName = "Firstname";
  const lastName = "Lastname";
  
  const currentStep = 3; // current step value
  const totalSteps = 5;
  const loadingPercentage = (currentStep / totalSteps) * 100;
  const student_email = "lastnf@rpi.edu";
  const student_phone_number = "+1 (518)-***-****";
  return (
    <>
      <div style={{
        textAlign: 'left', paddingLeft: '1.4em', fontSize: '1.9em',
        fontWeight: 'bold', marginBottom: '1em'
      }}>
        {lastName}, {' '}{firstName}
      </div>
      <div style={{
        display: 'flex', justifyContent: 'center', alignItems: 'center',
        gap: '4em', height: '70vh'
      }}>
        <div style={{
          width: '30%',
          backgroundColor: 'lightgray',
          padding: '1em',
          boxSizing: 'border-box',
          height: '60vh',
          display: 'flex', 
          flexDirection: 'column',
          justifyContent: 'space-between',
          borderRadius:'10px'
        }}>
          <div style={{ fontWeight: 'bold', fontSize: '1.5em' }}>Personal Information</div>

          {/* Peronsal info*/}
          <div style={{alignSelf: '',
          fontSize: '1.3em',
          height: '5vh'}}>Email: {student_email}</div> 

          <div style= {{alignSelf: '',
          fontSize: '1.3em', 
          height: '20vh'}}>Phone: {student_phone_number}</div>

          <button style={{ alignSelf: 'flex-end', fontSize: '1em' }}>Edit Contact Info</button>
        </div>
        <div style={{
          width: '30%',
          backgroundColor: 'lightgray',
          padding: '1em',
          boxSizing: 'border-box',
          height: '60vh',
          display: 'flex', 
          flexDirection: 'column',
          justifyContent: 'space-between',
          borderRadius: '10px'
        }}>
          <div style={{ fontWeight: 'bold', fontSize: '1.5em' }}>Application Status</div>
          
          {/* Loading Bar */}
          <div style={{
            height: '40px', 
            width: '100%',
            backgroundColor: '#E0E0E0', 
            position: 'relative',
            marginTop: '10px',
            borderRadius: '4px'
          }}>
            <div style={{
              height: '100%',
              width: `${loadingPercentage}%`,
              backgroundColor: 'green'
            }} />
            <div style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              transform: 'translate(-50%, -50%)',
              color: 'black',
              fontSize: '1.2em',
              fontWeight: 'bold'
            }}>
              {loadingPercentage}%
            </div>
          </div>
          
          <div style={{fontSize: '1.3em', marginTop: '5px', height: '10vh'}}>Step: {currentStep}/{totalSteps}</div>
          
          <button style={{ alignSelf: 'flex-end', fontSize: '1em' }}>Continue Application</button>
        </div>
      </div>
      <div>Current path: {location.pathname} </div>
    </>
  );
}
