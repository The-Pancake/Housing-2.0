// import Root from "./routes/root";
// import Dorms from "./routes/dorms";
// import Account from "./routes/account";
// import Contact from "./routes/contact";
// import Application from "./routes/application";
// import Layout from "./routes/layout";

// import { BrowserRouter } from "react-router-dom";

// import { Route, Routes } from "react-router";

// export default function App() {
//   return (
//     <div className="App">
//       <BrowserRouter>
//         <Routes>
//           <Route path="/" element={<Layout />}>
//             <Route index element={<Root />} />
//             <Route path="/dorms" element={<Dorms />} />
//             <Route path="/account" element={<Account />} />
//             <Route path="/contact" element={<Contact />} />
//             <Route path="/application" element={<Application />} />
//           </Route>
//         </Routes>
//       </BrowserRouter>
//     </div>
//   );
// }


import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; //using version 6
import Root from "./routes/root";
import Dorms from "./routes/dorms";
import Account from "./routes/account";
import Contact from "./routes/contact";
import AppRouter from './routes/AppRouter';
import Layout from "./routes/layout";
import EditProfile from './routes/edit_contact_info';
import Navbar from './components/navbar';

export default function App() {
  return (
    <div className="App">
      <Router>
        <Navbar /> 
        <Routes>
          <Route path="/" element={<Layout/>} />
          <Route path="/dorms" element={<Dorms/>} />
          <Route path="/account" element={<Account/>} />
          <Route path="/contact" element={<Contact/>} />
          <Route path="/application" element={<AppRouter/>} />
          <Route path="/edit-profile" element={<EditProfile />} />
        </Routes>
      </Router>
    </div>
  );
}


