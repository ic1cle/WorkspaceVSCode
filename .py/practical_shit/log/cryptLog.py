import time
from cryptography.fernet import Fernet

f = Fernet(b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=')
userLogin = False
signOrSetup = input("Sign in, Sign up: ")

def signIn(): # Sign in
    user = input("Username? ")
    userPass = (input("Password? "))
    usrpass = ((user + "\n") + userPass)

    with open('userDB.txt') as file: # Checks the login credentials
     if str(f.encrypt(usrpass.encode())) in file.read():
         userLogin = True

def signUp(): # Sign Up
    user = input("Username? ")
    userPass = (input("Password? "))
    usrpass = ((user + "\n") + userPass) + "\n"

    with open('userDB.txt') as file:
        if str(f.encrypt(user.encode())) in file.read(): # Checks if Username exists
            print("Username Already exists")
        else:
            with open("userDB.txt", "r") as file: # Pusts (Username + Password) in userDB.txt
                userDB_file = file.readlines()
            
            usrpass = ((user + "\n") + userPass) + "\n"
            userDB_file.append(str(f.encrypt(usrpass.encode())))

            with open("userDB.txt", "a") as userDB:
	            contents = "".join(userDB_file)
	            userDB.write(contents)

            loopsignin = input("Sign In(Y, N)? ") # Asks if you want to sign in
            if loopsignin.lower() == ("y"):
                signIn()
                if userLogin == True:
                    print("Success!")
                else:
                    print("Login Failed")
                    print("Try Again")
                    time.sleep(1)
                    signIn()

# Start and Confirm Sign up
if signOrSetup.lower() == ("sign up"):
    signUp()

# Start and Confirm Sign in
if signOrSetup.lower() == ("sign in"):
    signIn()
    if userLogin == True:
         print("Success!")
    else:
        print("Login Failed")
        print("Try Again")
        time.sleep(1)
        signIn()
       