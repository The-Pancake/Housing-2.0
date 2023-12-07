import Card from 'react-bootstrap/Card';
import Carousel from 'react-bootstrap/Carousel';
import dormData from "./dormData";
import "./dorms.css";
import { Link } from "react-router-dom";

const EachDorm = () => {
    const dorms = dormData.map((dorm) => {
        return (
            <Link to={`/DormView/${dorm.id}`} key={dorm.id} style={{ textDecoration: 'none' }}>
                <Card className="eachCard" style={{ width: '28rem', height: '26rem', border: "none" }}>
                    <Card.Body>
                        <Carousel>
                            <Carousel.Item>
                                <img src={dorm.imageOne} alt={`${dorm.dormName} View 1`} />
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageTwo} alt={`${dorm.dormName} View 2`} />
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageThree} alt={`${dorm.dormName} View 3`} />
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageFour} alt={`${dorm.dormName} View 4`} />
                            </Carousel.Item>
                        </Carousel>
                        <div className="bottomBox">
                            <Card.Title>{dorm.dormName}</Card.Title>
                            <Card.Text>{dorm.dormPrice}</Card.Text>
                            <Card.Text>{dorm.dormAddress}</Card.Text>
                            <Card.Text>Closest to: </Card.Text>
                        </div>
                    </Card.Body>
                </Card>
            </Link>
        );
    });

    return (
        <div className="grid">{dorms}</div>
    );
};

export default EachDorm;
