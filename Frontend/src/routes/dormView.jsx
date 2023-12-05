
import { useParams } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import dormData from "../components/dormData";
import { Container, Row, Col } from 'react-bootstrap';
import "./dormView.css"; // Make sure the CSS changes are included in this file

function DormView() {
    const { dormId } = useParams();
    const thisDorm = dormData.find(dorm => dorm.dormId === dormId);

    return (
        <>
            <div style={{ width: "95vw" }}>

                <Container>
                    <Row>
                        <Col md={7} className="left-image-wrapper">
                            <img src={thisDorm.imageOne} alt="Large" className="img-fluid" />
                        </Col>
                        <Col md={5} className="right-images-wrapper">
                            <img src={thisDorm.imageFour} alt="Small 1" className="img-fluid" />
                            <img src={thisDorm.imageFour} alt="Small 2" className="img-fluid" />
                        </Col>
                    </Row>
                </Container>

                <div className="container mt-5">
                    <div className="row justify-content-center">
                        <div className="col-md-7">
                            <div className="p-5">
                                <h3 style={{}}>{thisDorm.dormAddress}</h3>
                                <h2><span>$<strong>{thisDorm.dormPrice}</strong> <strong>{thisDorm.numRooms}</strong> room/s <strong>{thisDorm.numBeds}</strong> bed/s <strong>{thisDorm.sqft}</strong> sqft</span></h2>
                                <h2>About {thisDorm.dormName}</h2>
                                <h3>Type: Suite</h3>
                                <h3>Students per Suite: 2</h3>
                                <h3>Student Occupants: 102</h3>
                                <h3>Student Staff: 5</h3>
                                <h3>Number of Floors: 4</h3>
                                <h3>Theme: None</h3>
                                <h3>Co-Ed: Yes</h3>
                                <h3>Gender Breakdown: Mixed</h3>
                                <h3>Inclusive: Yes</h3>
                                <h3>Cleaning: None</h3>
                                <h3>Cleaning Schedule: None</h3>
                                <h3>Gender Restroom: Yes</h3>
                                <h3>Closest Dining Hall: Commons</h3>
                            </div>
                        </div>
                        <div className="col-md-5 outlined">
                            <div className="p-5">
                                <h2><b>Amenities</b></h2>
                                <h3>Air Conditioning</h3>
                                <h3>Blinds</h3>
                                <h3>Building Lounge</h3>
                                <h3>Cable TV</h3>
                                <h3>Card Access</h3>
                                <h3>Carpet</h3>
                                <h3>Elevator</h3>
                                <h3>Ethernet</h3>
                                <h3>Floor Lounge</h3>
                                <h3>Indoor Bike Storage</h3>
                                <h3>Kitchen</h3>
                                <h3>Laundry</h3>
                                <h3>Printer</h3>
                                <h3>Study Rooms</h3>
                                <h3>Wireless</h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default DormView;