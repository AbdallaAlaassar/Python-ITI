userd = [ {"name": "ziko", "pass": "1234"}, {"name": "abdalla", "pass": "1473"}, {"name": "ahmed", "pass": "5555"} ]

def validate_user(user):
    for i in userd:
        if i["name"] == user:
            return True
    return False

def validate_pass(passw):
    for i in userd:
        if i["pass"] == passw:
            return True
    return False

iuser = input("Enter username: ")


if validate_user(iuser):
    ipass = input("Enter password: ")
    if validate_pass(ipass): 
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")