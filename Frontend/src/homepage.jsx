
import Navbar from './component/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Tabs from './component/Tab';


function Homepage() {
  return (
    <div className="Homepage">
      <Navbar></Navbar>
      <Tabs></Tabs>
      {/* <div className="container con">
        <div className="row">
          <div className="col-md-12 d-flex align-items-center justify-content-center">
            <div className="card align-self-center" id="card">
              <div className="card-body text-dark">
                <h1>Hello World!</h1>
              </div>
            </div>
          </div>
        </div>
      </div> */}



    </div>
  );
}

export default Homepage;
