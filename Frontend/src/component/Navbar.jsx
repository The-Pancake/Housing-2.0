import 'bootstrap/dist/css/bootstrap.min.css';
import React , {useCallback, useState} from 'react';


const Navbar = ({  viewSelector }) => {
  const selectRoommateView = useCallback(() => {
      viewSelector('roommate');
  })

   const selectContactView = useCallback(() => {
     viewSelector('contact');
   });
   const selectFaqView = useCallback(() => {
    viewSelector('faq');
  });
   const selectTabsView = useCallback(() => {
     viewSelector('tabs');
   });
   const selectDormView = useCallback(() => {
    viewSelector('dorm');
  }
  )
  const selectProfileView = useCallback(() => {
    viewSelector('Profile');
  })
    const selectRoommatePairingView = useCallback(() => {
    viewSelector('roommatePairing');
    })
        function refresh_page(){
        window.location.reload();
        }
  
  ;
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
                <li className="nav-item" onClick={selectDormView}>
                  <a className="nav-link me-3" >Dorms</a>
                </li>
                <li className="nav-item" onClick={selectContactView}>
                  <a className="nav-link me-3" >Contact Us</a>
                </li>
                <li className="nav-item" onClick={selectFaqView}>
                  <a className="nav-link me-3" >FAQ</a>
                </li>
                <li className="nav-item" onClick={selectProfileView}>
                  <a className="nav-link me-3">My Profile</a>
                </li>
                  <li className="nav-item" onClick={selectRoommateView}>
                  <a className="nav-link me-3">Roommate</a>
                </li>
                    <li className="nav-item" onClick={selectRoommatePairingView}>
                    <a className="nav-link me-3">Pairing System</a>
                </li>
              </ul>
              <ul className="navbar-nav ms-auto mx-auto">
                <li className="nav-item">
                  <a className="nav-link me-3" onClick={refresh_page}>Log Out</a>
                </li>
              </ul>
            </div>
          </div>
            <style jsx>{`
        nav a:hover {
          color: #f00;
            cursor: pointer;
        }
      `}</style>
        </nav>
      );    
}
 
export default Navbar;