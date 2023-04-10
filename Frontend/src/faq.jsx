import React, { useState } from 'react';
import './FAQ.css';

const faq = () => {
  const [open, setOpen] = useState(null);

  const toggleAnswer = (index) => {
    if (open === index) {
      setOpen(null);
    } else {
      setOpen(index);
    }
  };

  const faqs = [
    {
      question: 'When will the Housing Application be open?',
      answer: 'April 15, 2021.',
    },
    {
      question: 'Will I be able to pre-select a roommate?',
      answer: 'During the housing application process, you will be able to select a preferred roommate/suitemate group. Placement in not guaranteed, however the staff in the Student Living and Learning Office will do their very best to match preferred roommates/suitemates.',
    },
    {
      question: 'What if I do not pre-select a roommate in the application?',
      answer: 'During the housing application process, you will be able to fill out a Roommate Matching Survey and will be able to search for roommates based on answers to their questions. If you do not pre-select a roommate, you will be assigned a roommate based on your answers to the survey.',
    },
    {
      question: 'Is Gender Inclusive Housing an option for students?',
      answer: 'Recognizing that single-gender housing may not be appropriate or comfortable for all students, there are a limited number of rooms made available as Gender Inclusive Housing in both the residence halls and apartments, on a space-available basis. Students signing up for these areas will be permitted to have roommates and suitemates that identify across the gender spectrum. You may choose this option in the housing application.',
    },
    {
      question: 'What housing options will be available to first-year students?',
      answer: 'As a part of CLASS: Clustered Learning, Advocacy, and Support for Students – the student experience at Rensselaer - students live with others from their cohort. This optimizes your transition by maximizing social opportunities via the living and learning experience. A list of first-year residence halls can be found here.',
    },
    {
      question: 'What criteria is utilized to decide room selection?',
      answer: 'Housing preferences are accommodated based on deposit paid date. In other words, the sooner an incoming student submits their deposit, the more likely it is that student will receive their preferred roommate and residence hall.',
    },
    {
      question: 'How do I learn more about the amenities and features of each residence hall?',
      answer: 'The Student Living and Learning website provides amenity information about each of our halls including furniture (and dimensions), air-conditioning (if available), hall carpeting, elevators, laundry, in-suite kitchens (for apartments), and nearest dining hall.',
    },
    {
      question: 'What are my options if I have a medical condition or unique situation that will require a special housing accommodation?',
      answer: 'If you are in need of a housing accommodation, complete the housing accommodation form. Please note that you will be asked to provide medical documentation for cases of medical conditions.',
    },
    {
      question: 'What are Special Interest Housing communities and can first-year students enroll in these communities?',
      answer: 'Special Interest Housing communities offer the opportunity to extend the classroom learning experience to a living environment shared with other students with similar interests and passions. For more information, visit the Student Living and Learning website.',
    },
    {
      question: 'When will the housing application close?',
      answer: 'Please complete your application by May 24, 2021, to ensure the best chance to be assigned your preferred housing. Students who do not complete the application by May 24, 2021, will still receive a housing assignment, but they may miss the opportunity to be placed with preferred roommates/suitemates or in a preferred residence hall.',
    },
  ];

  return (
    <div className="FAQ">
      <h1>Frequently Asked Questions</h1>
      {faqs.map((faq, index) => (
        <div key={index}>
          <div className="question" onClick={() => toggleAnswer(index)}>
            {faq.question}
          </div>
          {open === index && <div className="answer">{faq.answer}</div>}
        </div>
      ))}
    </div>
  );
};

export default faq;