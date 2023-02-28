import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import Landing from './landing.jsx';
import Homepage from './homepage';

function App() {
  const [showHomepage, setShowHomepage] = useState(false)

  const handleButtonClick = () => {
    setShowHomepage(true)
  }

  return (
    <div className="App">
      {showHomepage ? (
        <Homepage />
      ) : (
        <Landing onButtonClick={handleButtonClick} />
      )}
    </div>
  )
}

export default App