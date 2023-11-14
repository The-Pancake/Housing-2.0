
from fastapi import FastAPI, Request, Response
import uvicorn
from pymongo import MongoClient

from fastapi.middleware.cors import CORSMiddleware


# ------------------ Database ------------------
# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
# ----------------------------------------------


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/queryGroups")
async def queryGroups(res: Request):
    # is user signed in?
    if not res.cookies.get("rcsid"):
        return False

    group = client["Student_Info"]["Groups"].find_one(
        {"members": res.cookies.get("rcsid")}
    )
    return {"members": group["members"]}





@app.post("/signin")
async def signin(req: Request, res: Response):
    # todo: add error checking
    req_json = await req.json()
    email = req_json.get("email")
    password = req_json.get("password")
    rcsid = req_json.get("rcsid") if req_json.get("rcsid") else 'abc123'
    if (not email or not password):
        res.status_code = 400
        return {"message": "Error: missing email or password"}

    login_info = client["Student_Info"]["Logins"].find_one(
        {"email": email, "password": password})
    if (login_info == None):
        return False
    res.set_cookie(key="rcsid", value=rcsid)
    return True


@app.post("/signup")
async def signup(req: Request, res: Response):
    # todo: add error checking here
    # also maybe try to store just the password hashes
    #  instead of the passwords in plaintext

    # validate that there is email and password present
    #  in the request body
    req_json = await req.json()
    email = req_json.get("email")
    password = req_json.get("password")
    if (not email or not password):
        res.status_code = 400
        return {"message": "Error: missing email or password"}

    client["Student_Info"]["Logins"].update_one(
        {"email": email}, {"$set": {"password": password}}, upsert=True)

    res.status_code = 200
    return {"message": f"Successfully created new account {email} {password}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001,
                log_level="info", reload=True)
