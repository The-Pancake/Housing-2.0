import fastapi 
import json
import pydantic

# import fast API
app = fastapi.FastAPI()

# Declare a student class, this is all the information on the student that is recieved from the front end 
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

# Declaring a sample Student to send to "backend"
students = {
    0: Student(name='john', sex='m', major='Computer Science', dormPref='', year='freshman', geo='NY',sleepHours=[9,10], musicPreference=['Pop'], hobbies=['Gaming'], dorm='')
}

# Sample get message
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Following returns the student dictionary 
@app.get("/students/")
async def students() -> dict[str, dict[int, Student]]:
    return {0: students}
