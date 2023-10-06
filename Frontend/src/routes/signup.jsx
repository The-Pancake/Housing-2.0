

import { useState } from "react";
import "./signup.css"


export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function handleEmailChange(e) {
    setEmail(e.target.value);
  }

  function handlePasswordChange(e) {
    setPassword(e.target.value);
  }

  function submit() {
    console.log(email)
    console.log(password)
    let data = { email, password}
    console.log(data)
    /*
    This is an example fetch call
    We don't have an API yet, but it would be something like this
    fetch("http://localhost:8000/items", {
      method: "POST",
      body: JSON.stringify(data)
    }).then(res => res.json())
      .then(res => {
        console.log(res)
    })
    */
  }

  return (
    <div className="signupBg">
      <div>empty space</div>
      <div className="whiteBg">
        <div className="content">
          <div>
            <h1>Sign Up/Log in</h1>
            <h3>Tagline</h3>
          </div>
          <div className="inputs">
            <label htmlFor="email">RPI Email Address</label>
            <input name="email" value={email} onChange={handleEmailChange}></input>

            <label htmlFor="password">password</label>
            <input name="password" value={password} onChange={handlePasswordChange}></input>
          </div>
          <div className="bottom">
            <button className="btn" onClick={() => submit()}>Sign Up/Log In</button>
          </div>
        </div>
      </div>
    </div>
  );
}