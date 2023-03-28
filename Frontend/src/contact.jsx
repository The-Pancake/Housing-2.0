import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Contact.css';

const ContactUs = ({hidden}) => {
  return (
    <div hidden={hidden}>
      <h1></h1>
      <h1>Contact Us</h1>
      <form className={"contact-form"}>
        <label htmlFor="name">Name:</label><br />
        <input type="text" id="name" name="name" /><br />
        <label htmlFor="email">Email:</label><br />
        <input type="email" id="email" name="email" /><br />
        <label htmlFor="message">Message:</label><br />
        <textarea id="message" name="message"></textarea><br /><br />
        <input type="submit" value="Submit" />
      </form>

      <div className="container">
        <div className="row">
          <div className="col-md-4 col-sm-6">
            <h3>Office Hours</h3>
            <p>Monday-Friday: 8:30am - 4:30pm</p>
          </div>
          <div className="col-md-4 col-sm-6">
            <h3>Contact Us</h3>
            <p>Phone: (518) 276-6505</p>
            <p>Email: union-admin@rpi.edu</p>
          </div>
          <div className="col-md-4 col-sm-12">
            <h3>Visit Us</h3>
            <p>15th Street, Rensselaer Union Room 3701</p>
            <p>Troy, NY 12180</p>
          </div>
        </div>
        <div className="row">
          <div className="col-md-12">
            <p>&copy; {new Date().getFullYear()} Rensselaer Union</p>
          </div>
        </div>
      </div>
    </div>
  );
};



export default ContactUs;