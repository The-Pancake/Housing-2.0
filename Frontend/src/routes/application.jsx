import { useLocation } from 'react-router-dom';

export default function Application() {
  const location = useLocation();
  return (
    <>
      <div>this is the application page</div>
      <div>this will show the application status and stuff</div>
      <div>Current path: {location.pathname} </div>
    </>
  );
}