import { useLocation } from 'react-router-dom';


export default function Contact() {
  const location = useLocation();

  return (
    <>
      <div>this is the contact us page</div>
      <div>maybe a form for email contact or something</div>
      <div>Current path: {location.pathname} </div>

    </>
  );
}