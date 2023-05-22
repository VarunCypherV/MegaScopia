import os
import time
import database_structure_generator as defaults

#User defined imports
import cssqlmodules as sql

control=0
run_bias=''

def clear():
    print('\n'*45)          #For python shell due to lack of cls command
    

def login(x):
    
    if x[0]==1:
        
        
        
        start=1
        while start:
            global control
            global run_bias
            if control==0:
                print("Hello user! Please login into your account!")
                print("If you don't have an account,register now")
                print('\n\n')
            else:   
                clear()
            if not run_bias:    
                print('1.Login\n2.Register\n3.Exit Application')
                choice=input()
                control=1
                clear()
            else:
                choice=run_bias
            if choice=='1':
                print('LOGIN SCREEN:\n\n')
                username=input("Enter your username:")
                password=input("Enter your password:")
                print('\n\n')
                for i in x[1]:
                    j=i.split()
                    
                    if (j and j[0]==username and j[1]==password):
                        print("Login Successful!")
                        return_handle=j[0]
                        time.sleep(2)
                        start=0
                        break
                    elif j and j[0]==username:
                        print("Invalid Credentials")
                        time.sleep(2)
                        break
                else:
                    print("User not found!")
                    print("1.Register directly with the provided details")
                    print("2.Take me to the register page")
                    print("Any other option to return to homepage")
                    ch=input()
                    if ch=='1':
                        with open("users.txt",'a') as f:
                            f.seek(0,0)                                                       
                            f.write(username+' '+password+'\n')
                            
                            
                        print("Registration Complete!!")
                        time.sleep(1)
                        print("Creating your own Database")
                        time.sleep(2)
                        
                        sql.create_database(username)
                        print("Adding necessary Data Handles")
                        time.sleep(2)
                        defaults.generate_structure(username)
                        print("Done!!")
                        time.sleep(2)
                        return_handle=0
                        start=0
                        
                        
                    elif ch=='2':
                        run_bias='2'
                        clear()
                    time.sleep(2)
                        
            elif choice=='2':
                print("REGISTRATION PAGE:\n\n")
                print("You are one step away from your own personalised space for construction projects!")
                print('\n\n')
                username=input("Create a username:")
                password=input("Set your password:")
                confirm=input("Press Enter to proceed or any other key to terminate")
                clear()
                if confirm=='':
                    for i in x[1]:
                        
                        j=i.split()
                        if j and j[0]==username :
                            
                            print("Username Already exists!!")
                            print("Register with a new username or if it is yours, use the Login page")
                            time.sleep(3)
                            break
                            
                    else:
                        with open("users.txt",'a') as f:
                            f.seek(0,0)
                            
                            
                            f.write(username+' '+password+'\n')
                            
                            
                        print("Registration Complete!!")
                        time.sleep(1)
                        print("Creating your own Database")
                        time.sleep(2)
                        sql.create_database(username)
                        print("Adding necessary Data Handles")
                        time.sleep(2)
                        defaults.generate_structure(username)
                        print("Done!!")
                        time.sleep(2)
                        
                        return_handle=0
                        start=0
                run_bias=''    
                
            elif choice=='3':
                start=0
                return_handle=1
            else:
                print("Please input a valid choice")
        return return_handle
