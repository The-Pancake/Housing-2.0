import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Contact.css';

const ContactUs = ({hidden}) => {
  return (
    <div hidden={hidden}>
      <h1></h1>
      <h1>Contact Us</h1>
      <form>
        <label htmlFor="name">Name:</label><br />
        <input type="text" id="name" name="name" /><br />
        <label htmlFor="email">Email:</label><br />
        <input type="email" id="email" name="email" /><br />
        <label htmlFor="message">Message:</label><br />
        <textarea id="message" name="message"></textarea><br /><br />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default ContactUs;