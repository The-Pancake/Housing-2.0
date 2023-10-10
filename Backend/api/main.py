

from fastapi import FastAPI, Request, Response
import uvicorn
import json



app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.post("/signup")
async def signup(req: Request, res: Response):
  # todo: add error checking here

  # validate that there is email and password present
  #  in the request body
  reqJson = await req.json()
  email = reqJson.get("email")
  password = reqJson.get("password")
  if (not email or not password):
    res.status_code = 400
    return {"message": "Error: missing email or password"}

  loginFile = open("./data/logins.json", "r")
  loginInfo = json.load(loginFile)
  
  loginInfo[email] = password
  loginFile.close()
  loginFile = open("./data/logins.json", "w")
  

  json.dump(loginInfo, loginFile)

  loginFile.close()
  res.status_code = 200
  return {"message": f"Successfully created new account {email} {password}"}

  
  

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=3001, log_level="info", reload=True)