import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './faq.css';

const faq = ({hidden}) => {
  return (
    <div hidden={hidden}>
    <h1 className='m-5'>Frequently Asked Questions</h1>
    <div className='container'>
      <div className='accordion'>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse1'
          >
             When will the Housing Application be open?
          </div>
          <div id='collapse1' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            April 15, 2021. 
            </div>
          </div>
        </div>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse2'
          >
            Will I be able to pre-select a roommate?
          </div>
          <div id='collapse2' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            During the housing application process, you will be able to select a preferred roommate/suitemate group. Placement in not guaranteed, however the staff in the Student Living and Learning Office will do their very best to match preferred roommates/suitemates. 
            </div>
          </div>
        </div>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse3'
          >
            When will the housing application close?
          </div>
          <div id='collapse3' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            Please complete your application by May 24, 2021, to ensure the best chance to be assigned your preferred housing. Students who do not complete the application by May 24, 2021, will still receive a housing assignment, but they may miss the opportunity to be placed with preferred roommates/suitemates or in a preferred residence hall.
            </div>
          </div>
        </div>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse3'
          >
            Will I be required to have a meal plan?
          </div>
          <div id='collapse3' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            All first-year students will be required to have a meal plan for the Fall 2021 semester. Meal plan options will be communicated upon the release of the housing application.            </div>
          </div>
        </div>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse3'
          >
            Am I able to bring a car to campus?
          </div>
          <div id='collapse3' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            First-year students may not bring a car to campus and will not be able to purchase a parking pass.
            </div>
          </div>
        </div>
        <div className='accordion-item'>
          <div
            className='accordion-item-header'
            data-bs-toggle='collapse'
            data-bs-target='#collapse3'
          >
            What housing options will be available to first-year students?
          </div>
          <div id='collapse3' className='accordion-collapse collapse'>
            <div className='accordion-body'>
            As a part of CLASS: Clustered Learning, Advocacy, and Support for Students – the student experience at Rensselaer - students live with others from their cohort. This optimizes your transition by maximizing social opportunities via the living and learning experience. A list of first-year residence halls can be found here.            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  );
};

export default faq;