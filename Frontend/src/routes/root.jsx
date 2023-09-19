import { useLocation } from 'react-router-dom';


export default function Root() {
  const location = useLocation();

  return (
    <>
      <div>this is the root (/) directory</div>
      <div>Current path: {location.pathname} </div>

    </>
  );
}