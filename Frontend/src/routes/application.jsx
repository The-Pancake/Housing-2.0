import { useLocation } from 'react-router-dom';

export default function Application() {
  const location = useLocation();
  const firstName = "John";
  const lastName = "Dave";
  return (
    <>
      <div style ={{ textAlign: 'left', paddingLeft: '1.4em', fontSize: '1.9em'
      , fontWeight: 'bold', marginBottom: '1em'}}>{lastName}, {' '}{firstName}</div>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '4em', height: '70vh'}}>
        <div style={{
          width: '30%', backgroundColor: 'lightgray', padding: '1em',
          boxSizing:'border-box', height: '60vh'
        }}>
          <div  style={{fontWeight: 'bold', fontSize: '1.5em'}}>Personal Information</div>
          <button style={{marginTop: 'auto',alignSelf: 'flex-end', fontSize: '1em'}}>Edit Contact Info</button>
        </div>
        <div style={{
          width:'30%', backgroundColor: 'lightgray', padding: '1em',
          boxSizing: 'border-box', height: '60vh'
        }}>
          <div style={{fontWeight: 'bold', fontSize: '1.5em'}}>Application Status</div>
          <button style={{marginTop: 'auto',alignSelf: 'flex-end', fontSize: '1em'}}>Continue Application</button>
          {/*content for application status in here*/}
        </div>
      </div>
      <div>this is the application page</div>
      <div>Current path: {location.pathname} </div>
    </>
  );
}
