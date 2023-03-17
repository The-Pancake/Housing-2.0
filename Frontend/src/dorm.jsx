import { useState } from "react";
import "./App.css";
import Landing from "./landing.jsx";
import Homepage from "./homepage";
import Dorm from "./dorm.jsx";

function App() {
  const [showHomepage, setShowHomepage] = useState(false);
  const [showDorm, setShowDorm] = useState(false);

  const handleButtonClick = () => {
    setShowHomepage(true);
  };

  const handleDormClick = () => {
    setShowDorm(true);
  };

  return (
    <div className="App">
      {showHomepage ? (
        <Homepage />
      ) : (
        <Landing onButtonClick={handleButtonClick} />
      )}
      {showDorm ? <Dorm /> : null}
    </div>
  );
}

export default Dorms;
