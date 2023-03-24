import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './faq.css';

function FAQ() {
  // State for managing the FAQ data
  const [faqData, setFaqData] = useState([]);

  return (
    <div className="container">
      <h1>Frequently Asked Questions</h1>
      {faqData.map((faq, index) => (
        <div className="accordion" key={index}>
          <div className="accordion-item">
            <h2 className="accordion-header" id={`heading-${index}`}>
              <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target={`#collapse-${index}`} aria-expanded="true" aria-controls={`collapse-${index}`}>
                {faq.question}
              </button>
            </h2>
            <div id={`collapse-${index}`} className="accordion-collapse collapse" aria-labelledby={`heading-${index}`} data-bs-parent=".accordion">
              <div className="accordion-body">
                {faq.answer}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default FAQ;
