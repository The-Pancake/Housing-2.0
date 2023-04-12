import Navbar from "./component/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./Profile.css";
import profile_img from './image/profile.jpg';


const Profile = ({hidden}) => {
    return ( 
        <div className="" hidden={hidden}>
           <div className="container-fluid">
                <div className="row full-height">
                    <div className="col-sm-4 p-0">

<div className="card p-3 m-3 profile-card cool-bg">
    <div class="text-center">
        <img src={profile_img} alt="profile" className="card-img-top ratio mt-2" id="profile" fluid/>
    </div>
    <div class="card-body m-0 p-0 pt-3">
        <h5 class="card-title text-white">Ben Bittidle</h5>
        <p class="card-text text-white">Hiiii! I'm Ben-senpai! I'm a kawaii psychology student who loves all things anime and video games! When I'm not studying, I'm watching anime and reading manga, nya~! I'm a bit of an otaku, but I'm always up for some friendly competition and hanging out with my fellow otaku senpais! As for my living habits, I'm pretty easy-going and tidy! I always respect my roommates' privacy and belongings, and I hope they'll do the same for me, nya~! I'm looking for like-minded otaku senpais to share a living space with, so if you're into anime, gaming, and all things nerdy, let's connect and see if we'd make great roommates, uwu~!</p>
    </div>
</div>

                    </div>
                    <div className="col-sm-4 mt-3 text-white">

                        <h2 className="text-start">Preference</h2>

                        <ul className="list-group text-start cool-bg">
                            <li className="list-group-item">
                                <input type="checkbox" id="item1" className="m-2" />
                                <label htmlFor="item1 text-white">Like anime</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item2" className="m-2"/>
                                <label htmlFor="item2 text-white">Same major</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item3" className="m-2"/>
                                <label htmlFor="item3 text-white">Like to watch movie together</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item4" className="m-2"/>
                                <label htmlFor="item4 text-white">Likes board game</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item5" className="m-2"/>
                                <label htmlFor="item5 text-white">Quiet</label>
                            </li>
                            <li className="list-group-item">
                                <input type="checkbox" id="item6" className="m-2"/>
                                <label htmlFor="item6 text-white">Clean</label>
                            </li>
                        </ul>


                    </div>
                    <div className="col-sm-4 align-items-center justify-content-center">

                        <form className="bg-transparent update-form">
                            <h1 className="h3 m-0 mb-3 text-white">Update Preferences</h1>
                            <div className="form-group">
                                <a href="/application" className="btn btn-lg btn-block mb-3 my-5 bg-primary text-white">
                                    Go to Application Page
                                </a>
                            </div>

                            <div className="form-group mt-5">
                            <label htmlFor="bio">Update Bio</label>
                            <textarea
                                className="form-control cool-bg"
                                id="bio"
                                rows="3"

                            />
                            </div>
                            <button type="submit" className="btn btn-primary btn-lg btn-block my-2">Update Bio</button>
                        </form>

                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default Profile;