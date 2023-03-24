import Navbar from "./component/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./Profile.css";
import profile_img from './image/profile.jpg';


const Profile = ({hidden}) => {
    return ( 
        <div className="" hidden={hidden}>
           <div className="container-fluid">
                <div className="row bg-primary full-height">
                    <div className="col-sm-4 bg-warning">
                    <div className="square-img ">
                        <img src={profile_img} alt="profile" className="ratio ratio-1x1" id="profile" fluid/>
                    </div>
                    <p className="text-center">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Incidunt qui corporis, doloremque consequuntur soluta officia corrupti deleniti architecto maxime asperiores perspiciatis explicabo sed! Necessitatibus vel at consequatur cupiditate aut repudiandae tenetur delectus ab sit autem placeat recusandae consequuntur, inventore temporibus animi assumenda nemo suscipit quia modi deserunt, impedit molestias nulla!</p>
                    </div>
                    <div className="col-sm-4">Column 2</div>
                    <div className="col-sm-4">Column 3</div>
                </div>
            </div>
        </div>
     );
}
 
export default Profile;