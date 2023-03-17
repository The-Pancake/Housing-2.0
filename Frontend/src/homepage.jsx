
import Navbar from './component/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Tabs from './component/Tab';
import './App.css';
import Dorm from './dorm';
import ContactUs from './contact';


function Homepage() {
  return (
    <div className="Homepage">
      <Navbar></Navbar>
      <Tabs></Tabs>
      <Dorm></Dorm>
      <ContactUs></ContactUs>

    </div>
  );
}

export default Homepage;
