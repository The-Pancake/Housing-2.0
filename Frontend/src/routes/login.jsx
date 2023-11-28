import { useState } from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import 'bootstrap/dist/css/bootstrap.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "./signup.css"


export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rcsid, setRcsid] = useState("");

  function handleEmailChange(e) {
    setEmail(e.target.value);
  }

  function handlePasswordChange(e) {
    setPassword(e.target.value);
  }

  function handleRCSIDChange(e) {
    setRcsid(e.target.value);
  }

  function submit(e) {
    console.log(email)
    console.log(password)
    let data = { email, rcsid, password}
    console.log(data)
    e.preventDefault();
    fetch('http://localhost:3001/signin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      credentials: "include"
    })
    .then(res=>res.json())
    .then(res=>{
      console.log(res)
      // if (res.status === "success") {
      //   window.location.href = "/home";
      // }
    })
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
    <div>
            <div className='parent'>
                <div className='child leftSide'>
                    <img src="https://news.rpi.edu/sites/default/files/DJI_0154%20copy.jpg"/> 
                </div>
                <div className='child rightSide'>
                    <h1 style={{textAlign:"left"}}>Login</h1>
                    <h3 style={{textAlign:"left"}}>Tagline</h3>
                    <Form className="formInfo">
                        <Form.Group className="mb-3">
                            <Form.Label htmlFor="email">RPI Email Address</Form.Label>
                            <Form.Control type="email" placeholder="Enter RPI email" name="email" value={email} onChange={handleEmailChange}/>
                        </Form.Group>
                        <Form.Group className="mb-3">
                            <Form.Label htmlFor="rcsid">RCSID</Form.Label>
                            <Form.Control type="text" placeholder="Enter RCSID" name="rcsid" value={rcsid} onChange={handleRCSIDChange}/>
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label htmlFor="password">Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" name="password" value={password} onChange={handlePasswordChange}/>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicCheckbox">
                            <Form.Check type="checkbox" label="I agree to the Terms of Service and Privacy Policy" />
                        </Form.Group>
                        <Button  type="submit" className="submitButton" onClick={submit}>
                            Sign in
                        </Button>
                        <br/>
                        <Form.Text style={{textAlign:"left"}}>
                            Dont have an account? <b><u>Sign up</u></b>
                        </Form.Text>
                    </Form>
                </div>
            </div>
        </div>
    // <div className="signupBg">
    //   <div>empty space</div>
    //   <div className="whiteBg">
    //     <div className="content">
    //       <div>
    //         <h1>Sign Up/Log in</h1>
    //         <h3>Tagline</h3>
    //       </div>
    //       <div className="inputs">
    //         <label htmlFor="email">RPI Email Address</label>
    //         <input name="email" value={email} onChange={handleEmailChange}></input>

    //         <label htmlFor="password">password</label>
    //         <input name="password" value={password} onChange={handlePasswordChange}></input>
    //       </div>
    //       <div className="bottom">
    //         <button className="btn" onClick={() => submit()}>Sign Up/Log In</button>
    //       </div>
    //     </div>
    //   </div>
    // </div>
  );
}