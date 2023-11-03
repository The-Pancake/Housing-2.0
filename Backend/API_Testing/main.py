import fastapi 
import pydantic
import uvicorn

# Class objects come before app declaration
# Declare a student class, this is all the information on the student that is recieved from the front end 
class Student(pydantic.BaseModel):
    name: str
    sex: str
    major: str 
    dormPref: str | None = None
    year: str
    geo: str
    sleepHours: list  
    musicPreference: list | None = None
    hobbies: list | None =  None
    dorm: str | None = None

# import fast API
app = fastapi.FastAPI()

# Declaring a sample Student to send to "backend"
studentDatabase = {
    0: Student(name='john', sex='m', major='Computer Science', dormPref='', year='freshman', geo='NY',sleepHours=[9,10], musicPreference=['Pop'], hobbies=['Gaming'], dorm='')
}

# Sample get message
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Following returns the student dictionary 
@app.get("/students/{student_id}")
async def students(student_id: int):

    # Check if ID is valid
    if student_id > len(studentDatabase):
        raise fastapi.HTTPException(status_code=418, detail="Student Doesn't Exist")
    
    # Return student 
    return studentDatabase[student_id]
    

if __name__ == "__main__":


    # Execute uvicorn in command line so we don't need to type if every time
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")