import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './landing.css';
import RPI_logo_gray from './image/RPI_logo_gray.png';
import index_background from './image/index_background.jpg';

export default function Landing({onButtonClick} ) {
    // set background image
    document.body.style.backgroundImage = `url(${index_background})`;
  return (
    <div>
      <div className="rpi_gray_logo">
        <img src={RPI_logo_gray} alt="RPI Logo" id="logo" />
      </div>

      <div className="login text-center">
          <button type="button" className="btn btn-primary btn-lg btn-danger" id="login" onClick={onButtonClick}>
            Click Here to Find Your Home
          </button>

        <p className="login_info">Welcome to RPI Housing 2.0</p>
        <p className="login_info">
          This website is secured by RPI CAS system, please use your RCS account to login
        </p>
      </div>
    </div>
  );
}


