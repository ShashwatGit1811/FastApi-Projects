from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

users=[]

class RegisterUser(BaseModel):
    name:str
    email:str
    phone:int
    password:str
    c_password:str

class LoginUser(BaseModel):
    email:str
    password:str


@app.post("/register")
def register(user:RegisterUser):
    if user.password!=user.c_password:
        return{"error":"password and c_password does not match"}    
    elif len(str(user.phone))!=10:
         return{"error":"Length of phone number is not exactly 10 "}
    
    users.append(user)
    return {"message":"Registerd Successfully.....!"}
    



@app.post("/login")
def Login(user:LoginUser):
    for i in users:
        if i.email==user.email:
            if i.password==user.password:
                return {"message":f"{i.name} welcome, you are logged in..."}
    return {"message":"Invalid email and password"}


