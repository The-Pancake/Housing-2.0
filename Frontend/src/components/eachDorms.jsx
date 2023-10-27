import Card from 'react-bootstrap/Card';
import Carousel from 'react-bootstrap/Carousel';
import dormData from "./dormData";
import "./dorms.css";
const eachDorm = () => {
    const dorms = dormData.map((dorm) => {
        return (
            <>
                <Card style={{ width: '25rem',height:'20rem' }}>
                    <Card.Body>
                        <Carousel>
                            <Carousel.Item>
                                <img src={dorm.imageOne}></img>
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageTwo}></img>
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageThree}></img>
                            </Carousel.Item>
                            <Carousel.Item>
                                <img src={dorm.imageFour}></img>
                            </Carousel.Item>
                        </Carousel>
                        <Card.Title>{dorm.dormName}</Card.Title>
                        <Card.Text>{dorm.dormPrice}</Card.Text>
                        <Card.Text>{dorm.dormAddress}</Card.Text>
                        <Card.Text>Closest to: </Card.Text>
                    </Card.Body>
                </Card>
            </>
        )
    })
    return(
        <>
            <div className="grid">{dorms}</div>
        </>
    )
}

export default eachDorm;