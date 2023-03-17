import 'bootstrap/dist/css/bootstrap.min.css';


const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav me-auto mx-auto">
                <li className="nav-item">
                  <a className="nav-link me-3" href="#">Application</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link me-3" href="#">Dorms</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link me-3" href="#">Contact Us</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link me-3" href="#">My Profile</a>
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