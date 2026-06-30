from fastapi import FastAPI
from pydantic import BaseModel
from validation import validate

app=FastAPI()

users=[
    {"name":"raj","email":"raj@gmail.com","phone":1234567890},
    {"name":"om","email":"om@gmail.com","phone":9876543210}
    ]

class RegisterUser(BaseModel):
    name:str
    email:str
    phone:int


@app.get("/display")
def DisplayUsers():
    return {"data":users}


@app.post("/register")
def Register(user:RegisterUser):
    check=validate(user.email,user.phone,users)
    if check=="valid":
        users.append(user)
        return {"message":"Registerd Successfully.....!"}
    else:
        return check



@app.get("/search")
def Search(name:str):
    for i in users:
        if i.name==name:
            return {"data":i}
    
    return {"error":"user not found"}



@app.post("/delete")
def Delete(name:str="",email:str="",phone:int=0):
    for i in users:
        if i.name==name or i.phone==phone or i.email==email:
            users.remove(i)
            return {"success":"user deleted"}

    return {"error":"user not found"}


@app.put("/update")
def Update(upd_data:RegisterUser,email:str="",phone:int=0):
    index=0
    check=validate(upd_data.email,upd_data.phone,users)
    if check=="valid":
        for i in users:
            if i["phone"]==phone or i["email"]==email:
                users[index]=upd_data 
                return {"Update":"Your data is Updated Successfully"}
            index+=1
        return {"error":"user not found"}
    else:
        return check