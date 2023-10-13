import { useLocation } from 'react-router-dom';


export default function Dorms() {
  const location = useLocation();

  return (
    <>
      <div>this is the dorms (/dorms) directory</div>
      <div>this will list all of the dorms and stuff</div>
      <div>Current path: {location.pathname} </div>

    </>
  );
}