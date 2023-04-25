import { Link } from 'react-router-dom';
import './landing.css';

function Landing() {
  return (


    <div>
        <div className="rpi_gray_logo">
        <img src="./image/RPI_logo_gray.png" alt="RPI Logo" id="logo" />
        </div>
    
        <div className="login text-center">
        <Link to="/main">
        <button type="button" className="btn btn-primary btn-lg btn-danger" id="login">Click Here to Find Your Home</button>
        </Link>
        <p className="login_info">Welcome to RPI Housing 2.0</p>
        <p className="login_info">This website is secured by RPI CAS system, please use your RCS account to login</p>
        </div>

    </div>
        

    // <div>
    //   <h1>Landing Page</h1>
      
    // </div>
  );
}

export default Landing;
