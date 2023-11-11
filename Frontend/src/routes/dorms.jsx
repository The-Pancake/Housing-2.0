// import { useLocation } from 'react-router-dom';
// import Dropdown from 'react-bootstrap/Dropdown';
import 'bootstrap/dist/css/bootstrap.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "./dorms";
import Dropdown from 'react-bootstrap/Dropdown';
import EachDorm from "../components/eachDorms";

export default function Dorms() {
  return (
    <>
        <div style={{ display: 'flex', marginLeft:'5%',marginTop:'5%' }}>
            <Dropdown style={{marginRight:'10px'}}>
                <Dropdown.Toggle variant="success" id="dropdown-basic-1">
                    Rooms
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item href="#/action-1">1</Dropdown.Item>
                    <Dropdown.Item href="#/action-2">2</Dropdown.Item>
                    <Dropdown.Item href="#/action-3">3</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>

            <Dropdown style={{marginRight:'10px'}}>
                <Dropdown.Toggle variant="success" id="dropdown-basic-2">
                    Type
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                    <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                    <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>

            <Dropdown>
                <Dropdown.Toggle variant="success" id="dropdown-basic-3">
                    Price
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                    <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                    <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
        </div>
      <EachDorm />
    </>
  );
}
