def validate(email,phone,users):
    for i in  users:
        if i["email"]==email:
            return {"error":"Email already exist"}
        elif i["phone"]==phone: 
            return {"error":"Phone no already exist"}
        else:
            if '@' in email and '.' in email:
                if len(str(phone))==10:
                    return "valid"
                return {"error":"Phone no is invalid"}
            return {"error":"Email is invalid"}