

from fastapi import FastAPI, Request, Response
import uvicorn
import json
from pymongo import MongoClient



# ------------------ Database ------------------
# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
# ----------------------------------------------


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/profile")
async def profile(res: Request):
    # is user signed in?
    if (not res.cookies.get("account")):
        return False

    print(res.cookies.get("account"))
    return {"message": "tbd"}


@app.post("/signin")
async def signin(req: Request, res: Response):
    # todo: add error checking
    reqJson = await req.json()
    email = reqJson.get("email")
    password = reqJson.get("password")
    if (not email or not password):
        res.status_code = 400
        return {"message": "Error: missing email or password"}


    # loginFile = open("./data/logins.json", "r")
    # loginInfo = json.load(loginFile)

    loginInfo = client["Student_Info"]["Logins"].find_one({"email": email, "password": password})
    if (loginInfo == None):
        return False
    res.set_cookie(key="account", value=email)
    return True


@app.post("/signup")
async def signup(req: Request, res: Response):
    # todo: add error checking here
    # also maybe try to store just the password hashes
    #  instead of the passwords in plaintext

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
    uvicorn.run("main:app", host="127.0.0.1", port=3001,
                log_level="info", reload=True)





# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database("Campus")
    print(dbname)
    print(dbname.list_collection_names())
    temp = dbname["Dorms"].find()
    print(temp)
    print(type(temp))
    for x in temp:
        print(x)
