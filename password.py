#this the module which allows the user to encrypt the password 
from cryptography.fernet import Fernet



master_pwd = input("what is the your password? ")

def view(): #declaretion of function name as a view
    #pass # pass means if the statement is empty for a while
    with open("password.txt", "r") as f:
        for line in f.readlines():
            #print(line.rstrip()) #this line means it will print the account and password and rstrip() function  is already define in the python library 
            data=line.rstrip()
            user, passw = data.split("|") # this line means user and passw were the pipe operator will be there then it will split and account name will be assign to user and password will be assign to passw
            print("User:",user ," Password:",passw)



def add():
   # pass
   name=input("Account Name: ")
   password=input("Password: ")

#with means it will automatically close the file after the all operation has been done
#it can been written as file = open("password.txt",'a') and then close the file with file.close()
#here a means the mode od the file a stands for append the file thier are many types of mode i.e write and read also  
#as f means the file that is created can be written as f 
   with open("password.txt", "a") as f:
       f.write(name + "|" + password + "\n" )


while True:
    mode = input("Would you like to add a new password or view existing one (view, add)? enter q for quit :- " "\n")

    if mode == "q":
        break
    
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")

