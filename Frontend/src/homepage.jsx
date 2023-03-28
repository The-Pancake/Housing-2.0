
import Navbar from './component/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Tabs from './component/Tab';
import './App.css';
import { useState } from 'react';
import Contact from './contact';
import DormGrid from './dorm';
import ProfileGrid from './Profile';
import Roommates from './roommate';
import RoommatePairing from './roommatePairing';

export default function Homepage({ hidden }) {
  const [view, setView] = useState('home');
  const height = window.visualViewport.height - 80;
  return (
    <div className="Homepage" hidden={hidden}>
      <Navbar viewSelector={setView} />
      <Tabs hidden={view !== 'tabs'}></Tabs>
      <Contact hidden={view !== 'contact'} />
      <DormGrid hidden={view !== 'dorm'} />
      <ProfileGrid hidden={view !== 'Profile'} />
        <Roommates hidden={view !== 'roommate'} />
        <RoommatePairing hidden={view !== 'roommatePairing'} />
    </div>
  );
}
