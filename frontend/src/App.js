import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./landing";
import Main from "./main";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/main" element={<Main />} />
      </Routes>
    </Router>
  );
}

export default App;
