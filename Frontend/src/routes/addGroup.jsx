import "./addGroup.css";
import { useEffect, useState } from "react";
import { Form, InputGroup, Stack, Modal, Container, Button, Col, Row } from "react-bootstrap";


export default function AddGroup() {
  const [group, setGroup] = useState(["abc123", "bcd234", "cde345"]);
  const [show, setShow] = useState(false);
  const [input, setInput] = useState("");
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const removeUser = (user) => setGroup(group.filter((u) => u !== user));
  const addUser = (user) => setGroup([...new Set([...group, user])]);

  useEffect(() => {
    // query api for group members
    fetch("http://localhost:3001/queryGroups", {
      method: "GET",
      credentials: "include"
    }).then(res => res.json())
      .then(res => {
        console.log(res)
        setGroup(res.members)
    })
  }, [])

  useEffect(() => {
    fetch("http://localhost:3001/updateGroup", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "http://localhost:3001",
      },
      body: JSON.stringify(group),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
      });
  }, [group]);
  
  return (
    <>
      <div className="main">
        <Container fluid className="h-100">
          <Row className="h-100">
            <Col
              md={6}
              className="d-flex flex-column justify-content-center align-items-center w-100"
            >
              <div className="w-100">
                  <h2>
                    Add/modify groups
                  </h2>
              </div>
              <div style={{"font-size": "2rem"}}>
                <p>Current group:</p>
                <Stack gap={1}>
                {
                  group.map((user, index) => {
                    return (
                      <div key={index} className="d-flex">
                        <p className="flex-grow-1 m-0">{user}</p>
                        <Button variant="danger" onClick={()=>removeUser(user)}>-</Button>
                      </div>
                    );
                  })
                }
                <Button onClick={handleShow}>Add member</Button>
                </Stack>
              </div>
            </Col>
          </Row>
        </Container>
        <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add Group Member</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Enter RCSID      
          <InputGroup className="mb-3">
            <Form.Control
              placeholder="RCSID"
              aria-label="RCSID"
              aria-describedby="rcsid"
              onChange={e => setInput(e.target.value)}
            />
          </InputGroup>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={() => {handleClose(); addUser(input)}}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      </div>
    </>
  );
}
