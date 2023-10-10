import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import 'bootstrap/dist/css/bootstrap.css';
import "./Signup.css";

function Login() {
    return (
        <div>
            <div className='parent'>
                <div className='child leftSide'>
                    {/* <h1>Balls</h1> */}
                    {/* <img src="https://news.rpi.edu/sites/default/files/DJI_0154%20copy.jpg"/> */}
                </div>
                <div className='child rightSide'>
                    <h1 style={{textAlign:"left"}}>Login</h1>
                    <h3 style={{textAlign:"left"}}>Tagline</h3>
                    <Form className="formInfo">
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>RPI Email Address</Form.Label>
                            <Form.Control type="email" placeholder="Enter RPI email" />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicCheckbox">
                            <Form.Check type="checkbox" label="I agree to the Terms of Service and Privacy Policy" />
                        </Form.Group>
                        <Button  type="submit" className="submitButton">
                            Signup
                        </Button>
                        <br/>
                        <Form.Text style={{textAlign:"left"}}>
                            Already have an account? <b><u>Log in</u></b>
                        </Form.Text>
                    </Form>
                </div>
            </div>
        </div>
    )
}

export default Login;