import 'bootstrap/dist/css/bootstrap.min.css';
import React , {useCallback, useState} from 'react';


const Navbar = ({ fixed, viewSelector }) => {
  const [navbarOpen, setNavbarOpen] = React.useState(false);

   const selectContactView = useCallback(() => {
     viewSelector('contact');
   });
   const selectTabsView = useCallback(() => {
     viewSelector('tabs');
   });
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav me-auto mx-auto">
                <li className="nav-item" onClick={selectTabsView}>
                  <a className="nav-link me-3" >Application</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link me-3" >Dorms</a>
                </li>
                <li className="nav-item" onClick={selectContactView}>
                  <a className="nav-link me-3" >Contact Us</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link me-3" >My Profile</a>
                </li>
              </ul>
              <ul className="navbar-nav ms-auto mx-auto">
                <li className="nav-item">
                  <a className="nav-link me-3" href="#">Log Out</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      );    
}
 
export default Navbar;