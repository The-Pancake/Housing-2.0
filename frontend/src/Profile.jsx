import Navbar from "./component/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./Profile.css";
import profile_img from './image/profile.jpg';


const Profile = () => {
    return ( 
        

        

        <div className="">



            <Navbar></Navbar>


            <div className="container-fluid">


                <div className="row bg-primary full-height">
                    <div className="col-sm-4 bg-warning">

                    <div className="square-img">
                        <img src={profile_img} alt="profile" id="profile" />
                    </div>
                    <p className="text-center">Your description here</p>

                    </div>
                    <div className="col-sm-4">Column 2</div>
                    <div className="col-sm-4">Column 3</div>
                </div>

            </div>




            
        </div>


     );
}
 
export default Profile;