import fastapi 
import json
import pydantic

# import fast API
app = fastapi.FastAPI()

# Declare a student class 
class Student(pydantic.BaseModel):
    name: str
    sex: str
    major: str
    dormPref: str
    year: str
    geo: str
    sleepHours: list
    musicPreference: list
    hobbies: list
    dorm: str

# Sample get message
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get a student from "front-end" and return it 
@app.get("/students/")
async def student(info: Student):
    return info
