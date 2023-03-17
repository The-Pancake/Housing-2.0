import React from 'react';

//contact
function Contact({hidden}) {
  return (
    <div className="container" hidden={hidden}>
      <h1>Contact Us</h1>
      <p>Email: <a href="mailto:contact@example.com">Whatever the email is</a></p>
      <p>Phone: Whatever the number is</p>
      <p>Address: 1999 Burdett Ave, Troy, 12180</p>
      <p>Hours: Office Hours here</p>

      <h2>Send an Email</h2>
      <form action="submit-form.php" method="POST">
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Name</label>
          <input type="text" className="form-control" id="name" name="name" required />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email</label>
          <input type="email" className="form-control" id="email" name="email" required />
        </div>
        <div className="mb-3">
          <label htmlFor="message" className="form-label">Message</label>
          <textarea className="form-control" id="message" name="message" rows="5" required></textarea>
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
}

export default Contact;
