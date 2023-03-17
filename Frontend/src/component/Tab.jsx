import { useState } from "react";
import "./Tab.css";
import 'bootstrap/dist/css/bootstrap.min.css';


function Tabs({hidden}) {
  const [toggleState, setToggleState] = useState(1);

  const toggleTab = (index) => {
    setToggleState(index);
  };

  return (
    <div className="container" hidden={hidden}>
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


          <div className="card bg-transparent app-card">
            <div className="card-body text-light">
              
              <h5 className="card-title text-left mb-5">Applications: </h5>
              <div className="my-3">

                <p className="card-text text-left">Summer Arch 2023:</p>
                <div className="progress">
                  <div className="progress-bar" role="progressbar" style={{ width: "25%" }} aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
                </div>

              </div>

              <a href="#" className="btn btn-success mt-5">Continue Application</a>
            </div>
          </div>
        </div>

        <div
          className={toggleState === 2 ? "content  active-content" : "content"}
        >
          <div className="card bg-transparent">
            <div className="card-body text-light">

            <div className="mb-5">

              <h5 className="card-title text-left mb-3 ">Group SPAM W: </h5>
              <p className="card-text d-block mb-1">Tommie Trishna</p>
              <p className="card-text d-block mb-1">Valentinus Ramakant</p>
              <p className="card-text d-block mb-1">Marijus Ciarán</p>



            </div>
              
              <div className="d-flex justify-content-around">

                <a href="#" className="btn btn-danger">Leave group</a>
                <a href="#" className="btn btn-success">Add roommates</a>



              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

export default Tabs;