import { useLocation } from 'react-router-dom';


export default function Signup() {
  const location = useLocation();

  return (
    <>
      <div>this is the signup (/) directory</div>
      <div>Current path: {location.pathname} </div>

    </>
  );
}