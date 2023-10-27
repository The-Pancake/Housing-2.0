import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; //using version 6
//import Root from "./routes/root";
import Dorms from "./routes/dorms";
import Account from "./routes/account";
import Contact from "./routes/contact";
import AppRouter from './routes/AppRouter';
import Layout from "./routes/layout";
import EditProfile from './routes/edit_contact_info';
import Navbar from './components/navbar';
import Login from "./routes/login"
import Application from "./routes/application";
import Layout from "./routes/layout";
import Signup from "./routes/signup";
import Quiz from "./routes/quiz";
import QuizQuestions from "./routes/quizQuestions";
import FAQ from "./routes/faq";


import "./app.css"

export default function App() {
  return (
    <div className="App">
      <Router>
        <Navbar /> 
        <Routes>
          {/* <Route path="/" element={<Layout />}> */}
            <Route index element={<Root />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dorms" element={<Dorms />} />
            <Route path="/quiz" element={<Quiz />} />
            <Route path="/account" element={<Account />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/application" element={<Application />} />
            <Route path="/quizQuestions" element={<QuizQuestions />} />
            <Route path="/faq" element={<FAQ />} />
          {/* </Route> */}
        </Routes>
      </Router>
    </div>
  );
}