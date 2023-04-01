import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Contact.css';

const ContactUs = ({hidden}) => {
  return (
    <div hidden={hidden}>
      <h1></h1>
      <h1 className='m-5'>Contact Us</h1>
      <form className={"contact-form m-5"}>
        <label htmlFor="name" className='text-white'>Name:</label><br />
        <input type="text" id="name" name="name" /><br />
        <label htmlFor="email" className='text-white'>Email:</label><br />
        <input type="email" id="email" name="email" /><br />
        <label htmlFor="message" className='text-white'>Message:</label><br />
        <textarea id="message" name="message"></textarea><br /><br />
        <input type="submit" value="Submit" />
      </form>
      
      <div className="footer">
        <img src="https://my.aacsb.edu/Portals/0/assets/images/contact/Rensselaer.png" alt="Footer image" />
        <div className="footer-info">
          <h2>Contact</h2>
          <p>Student Living and Learning</p>
          <p>Commons West</p>
          <p>Troy, NY 12180, U.S.A.</p>
          <p>+1.518.276.6284</p>
          <p>fax: +1.518.276.6223</p>
          <p>email: reslife@rpi.edu</p>
          <p>Hours of Operation: M-F, 8:00 a.m. - 5:00 p.m.</p>
        </div>
      </div>
    </div>
  );
};



export default ContactUs;