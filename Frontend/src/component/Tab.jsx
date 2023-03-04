import { useState } from "react";
import "./Tab.css";
import 'bootstrap/dist/css/bootstrap.min.css';


function Tabs() {
  const [toggleState, setToggleState] = useState(1);

  const toggleTab = (index) => {
    setToggleState(index);
  };

  return (
    <div className="container">
      <div className="bloc-tabs">
        <button
          className={toggleState === 1 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(1)}
        >
          Application
        </button>
        <button
          className={toggleState === 2 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(2)}
        >
          Roommate
        </button>
      </div>

      <div className="content-tabs">
        <div
          className={toggleState === 1 ? "content  active-content" : "content"}
        >


          <div className="card bg-transparent">
            <div className="card-body text-light">
              <h5 className="card-title text-left">Applications: </h5>
              <p className="card-text">Summer Arch 2023: <span className="text-success"> 70%</span></p>
              <a href="#" className="btn btn-success">Continue Application</a>
            </div>
          </div>
        </div>

        <div
          className={toggleState === 2 ? "content  active-content" : "content"}
        >
          <div className="card bg-transparent">
            <div className="card-body text-light">
              <h5 className="card-title text-left">Roommates: </h5>
              <p className="card-text d-block">Josh</p>
              <p className="card-text d-block">Yosh</p>
              <p className="card-text d-block">Yash</p>

              <a href="#" className="btn btn-success">Add roommates</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

export default Tabs;