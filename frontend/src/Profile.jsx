import Navbar from "./component/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./Profile.css";
import profile_img from './image/profile.jpg';


const Profile = ({hidden}) => {
    return ( 
        <div className="" hidden={hidden}>
           <div className="container-fluid">
                <div className="row bg-primary full-height">
                    <div className="col-sm-4 bg-warning p-0">

                        <div className="card p-3 m-3">
                            <img src={profile_img} alt="profile" className="card-img-top ratio ratio-1x1 mt-2" id="profile" fluid/>
                            <div class="card-body m-0 p-0 pt-3">
                                <h5 class="card-title">Ben Bittidle</h5>
                                <p class="card-text">Hey there, I'm Ben Bittidle, a psychology student and a proud anime otaku. When I'm not studying or playing video games, you'll find me binge-watching anime or reading manga. I'm a bit of a nerd, but I'm always down for some friendly competition and socializing. In terms of living habits, I'm pretty low-maintenance and tidy. I'm respectful of my roommates' privacy and belongings, and I expect the same in return. I'm looking for like-minded otaku roommates to share a living space with. If you're into anime, gaming, and all things nerdy, then let's connect and see if we'd make great roommates!</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4 mt-3 text-white">

                        <h2 className="text-start">Preference</h2>

                        <ul className="list-group text-start">
                            <li className="list-group-item">
                                <input type="checkbox" id="item1" />
                                <label htmlFor="item1">Like anime</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item2" />
                                <label htmlFor="item2">Same major</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item3" />
                                <label htmlFor="item3">Like to watch movie together</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item4" />
                                <label htmlFor="item4">Likes board game</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item5" />
                                <label htmlFor="item5">Quiet</label>
                            </li>
                            
                        </ul>




                        
                        



                    </div>
                    <div className="col-sm-4 bg-danger">Column 3</div>
                </div>
            </div>
        </div>
     );
}
 
export default Profile;