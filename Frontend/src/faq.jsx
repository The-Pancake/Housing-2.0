import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './faq.css';

const Faq = ({hidden}) => {
  return (
    <div hidden={hidden}>
      <h1 className='m-5'>Frequently Asked Questions</h1>
      <div className='container'>
        <div className='accordion'>
          <div className='accordion-item'>
            <div className='accordion-item-header'>
              What is your return policy?
            </div>
            <div className='accordion-item-content'>
              We accept returns within 30 days of purchase. Please contact our customer service team for assistance.
            </div>
          </div>
          <div className='accordion-item'>
            <div className='accordion-item-header'>
              How do I track my order?
            </div>
            <div className='accordion-item-content'>
              You will receive a tracking number via email once your order has shipped.
            </div>
          </div>
          <div className='accordion-item'>
            <div className='accordion-item-header'>
              Do you offer international shipping?
            </div>
            <div className='accordion-item-content'>
              Yes, we offer international shipping to most countries. Please contact our customer service team for more information.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Faq;