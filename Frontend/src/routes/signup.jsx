

import "./signup.css"


export default function Signup() {

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
            <input name="email"></input>

            <label htmlFor="password">password</label>
            <input name="password"></input>
          </div>
          <div class="bottom">
            <button className="btn">Sign Up/Log In</button>
          </div>
        </div>
      </div>
    </div>
  );
}