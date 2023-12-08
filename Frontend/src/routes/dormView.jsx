import { useParams } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import dormData from "../components/dormData.js";
import ImageGallery from 'react-image-gallery';
import "./dormView.css";

function DormView() {
    const { dormId } = useParams();
    const thisDorm = dormData.find(dorm => dorm.id === dormId);
    if (!thisDorm) {
        return <div>Dorm not found</div>;
    }
    console.log(thisDorm.dormPrice);

    const images = [
        {
            original: thisDorm.imageOne,
            thumbnail: thisDorm.imageOne,
        },
        {
            original: thisDorm.imageTwo,
            thumbnail: thisDorm.imageTwo,
        },
        {
            original: thisDorm.imageThree,
            thumbnail: thisDorm.imageThree,
        },
        {
            original: thisDorm.imageFour,
            thumbnail: thisDorm.imageFour,
        },
    ];

    return (
        <div className="flat-detail">
            <div className="container mt-5 mb-5">
                <div className="row">
                    <div className="col-lg-12">
                        <div className="fd-top flat-detail-content">
                            <div>
                                <h3 className="flat-detail-title">{thisDorm.dormName}</h3>
                                <p className="fd-address"> <i className="fas fa-map-marker-alt"></i>
                                {thisDorm.dormAddress}</p>
                            </div>
                            <div>
                                <span className="fd-price">${thisDorm.dormPrice}</span>
                            </div>
                        </div>
                        <ImageGallery flickThreshold={0.50} slideDuration={0} items={images} showNav={false} showFullscreenButton={false} showPlayButton={false} />
                        <div className="row">
                            <div className="col-lg-8">
                                <div className="fd-item">
                                    <h4>Description</h4>
                                    <p>This is dorm {thisDorm.dormName}. It is currently located at {thisDorm.dormAddress} for ${thisDorm.dormPrice} per month. It includes {thisDorm.numRooms} room/s and {thisDorm.numBeds} beds.</p>
                                </div>
                                <div className="fd-item fd-property-detail">
                                    <h4>Property Details</h4>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>Kitchen: </span>
                                            <span>1</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>Number of Rooms: </span>
                                            <span>{thisDorm.numRooms}</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>Number of Beds:  </span>
                                            <span>{thisDorm.numBeds}</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>Rating: </span>
                                            <span>{thisDorm.rating}/5</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>Total Ratings: </span>
                                            <span>{thisDorm.ratingAmt}</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>Square Foot:  </span>
                                            <span>{thisDorm.sqft}</span>
                                        </div>
                                    </div>
                                </div>
                                {/* <div className="fd-item fd-features">
                                    <h4>Features</h4>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check"></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check"></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>Lorem Ipsum</span>
                                        </div>
                                    </div>
                                </div> */}
                                {/* <div className="fd-item">
                                    <h4>Maps</h4>
                                    <iframe src="https://www.google.com/maps/place/Barton+Hall/@42.729118,-73.6766864,17z/data=!3m1!4b1!4m6!3m5!1s0x89de0f9e2d6ecedf:0xcef59faad0bf7f6e!8m2!3d42.7291141!4d-73.6741061!16s%2Fg%2F11bwqqgbj0?entry=ttu" width="100%" height="450" loading="lazy"></iframe>
                                </div> */}
                            </div>
                            <div className="col-lg-4">
                                <div className="fd-sidebar-item">
                                    <h4>Points of Interest</h4>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Nearest Dining Hall</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Nearest Dorm</span>
                                    </div>
                                    {/* <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Lorem Ipsum Dolor</span>
                                    </div> */}
                                </div>
                                {/* <div className="fd-sidebar-item">
                                    <h4>Category</h4>
                                    <ul className="category-ul">
                                        <li>Category 1</li>
                                        <li>Category 2</li>
                                        <li>Category 3</li>
                                        <li>Category 4</li>
                                        <li>Category 5</li>
                                    </ul>
                                </div> */}
                                {/* <div className="fd-sidebar-item">
                                    <h4>Recently Added</h4>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Lorem Ipsum Dolor</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Lorem Ipsum Dolor</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>Lorem Ipsum Dolor</span>
                                    </div>
                                </div> */}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DormView;
