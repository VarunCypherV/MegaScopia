#PROJECT TITLE-MEGASCOPIA
'''GROUP MEMBERS
Vamsi Krishna-Admn:1082
Sri Narayana-Admn:3333
Varun Vetrivendan-Admn:8334

'''
#Database name-(Created for every user with their username)
#Name of tables-CUSTOMER DETAILS, PROJECT FINANCE, PROJECT DETAILS, ENGINEERS
#Packages and modules as listed below



#All header files
import os
import time
import math
import random
import mysql.connector

#All custom modules import
import loading_screen
import login_megascopia
import cssqlmodules
import funcmod



#All custom functions definitions
def clear():
    print('\n'*45)          #For python shell due to lack of cls command
    

def update_users():
    global userslist
    with open('users.txt') as f:
        userslist=[f.readlines()]
        
def generate_project_id():
    with open('engineerids.txt','r') as f:
        used_ids=f.readlines()
    with open('projectids.txt','a+') as f:
        #used_ids=f.readlines()
        start=1
        id_=0
        while start:
            for i in range(4):
                id_+=random.randint(1,9) 
                id_*=10
            else:
                id_/=10
                if id_ in used_ids:
                    id_=0
                else:
                    start=0
        f.write(str(int(id_))+'\n')
    return int(id_)

def engineer_id():
    with open('engineerids.txt','r') as f:
        used_ids=f.readlines()
    with open('engineerids.txt','a+') as f:
        #used_ids=f.readlines()
        start=1
        id_=0
        while start:
            for i in range(4):
                id_+=random.randint(1,9) 
                id_*=10
            else:
                id_/=10
                if id_ in used_ids:
                    id_=0
                else:
                    start=0
        f.write(str(int(id_))+'\n')
    return int(id_)
                    
        
def addproject():
    global logged_in_as
    print("\t\t\t\t\tAdd Project")
    print("Quit the process by just pressing enter")
    print('\n\n')
    print("Part 1.Project Details\n\n")               #PART 1
    a=input('Construction Site:')
    if a:
        b=input('Project Description:')
        if b:
            proceed=0
            for z in range(4):
                c=input('Project Budget(estimate in rupees):')
                if c.isdigit():
                    proceed=1
                    break
                elif not c:
                    print("Please enter the right format\n")
            else:
                print('\n Too many invalid attempts. Please restart your process(press enter to home)')
                input()
                clear()

                
            if proceed:
                proceed=0
                print("Estimated Project End Date")

                for z in range(4):
                    d=input("Month number(01=Jan,12=Dec):")           
                    if d.isdigit() and len(d)==2:
                        proceed=1
                        break
                    elif not d:
                        print("Please enter the right format\n")
                else:
                    print('\n Too many invalid attempts. Please restart your process(press enter to home)')
                    input()
                    clear()
                    
            if proceed:                    
                proceed=0
                for z in range(4):
                    e=input("Year:")           
                    if e.isdigit() and len(e)==4:
                        proceed=1
                        break
                    elif not e:
                        print("Please enter the right format\n")
                else:
                    print('\n Too many invalid attempts. Please restart your process(press enter to home)')
                    input()
                    clear()

                
            if proceed:
                print('\n\n\nPart 2.Customer data')                 #PART 2
                proceed=0
                while not proceed:
                    x=input("Customer name:")
                    handle=cssqlmodules.view_table([logged_in_as,'customerdetails',['CustomerName']])
                    if x and x in handle:
                        proceed=1
                        reg_type=1 #user known so no need extra details
                    elif x:
                        proceed=1
                        reg_type=2
            if proceed and reg_type==2:
                proceed=0
                g=input("Customer Permanent address:")
                if g:
                    proceed=1
                if proceed:
                    proceed=0
                    h=input("Customer Phone Number:")
                    if h:
                        proceed=1
                

                if proceed:
                    proceed=0
                    l=input("Total amount to be paid:")
                    if l and l.isdigit():
                        proceed=1
                


                if proceed:                                    ##PART 3
                    print("\n\n\nPart 3.Engineers")
                    proceed=0
                    m=input("Head Engineer id(4 digit):")
                    with open('engineerids.txt','r') as f:
                        used_ids=f.readlines()
                    if m and len(m)==4 and m+'\n' in used_ids:
                        proceed=1
                    elif m:
                        proceed=0
                        print("Engineer not found!!!")
                        input("Press enter to home")
                    else:
                        proceed=0

                if proceed:
                    id_=generate_project_id()
                    cssqlmodules.custom1([logged_in_as,a,b,c,d,e,x,g,h,l,m,id_])
                    print("Creating!")
                    time.sleep(2)
                    print("Done!!")
                    input("Press enter to home")
                    clear()
                    
            elif proceed and reg_type==1:        
                            
                proceed=0
                

                if proceed:
                    proceed=0
                    l=input("Total amount to be paid:")
                    if l and l.isdigit():
                        proceed=1
                


                if proceed:
                    print("\n\n\nPart 3.Engineers")
                    proceed=0
                    m=input("Head Engineer id(4 digit):")
                    if m and len(m)==4:
                        proceed=1

                if proceed:
                    id_=generate_project_id()
                    cssqlmodules.custom1([logged_in_as,a,b,c,d,e,x,l,m,id_])
                    print("Creating!!")
                    time.sleep(2)
                    print("Done!!")
                    input("Press Enter to home")
                    clear()
            
                
    
def view_data(x): #x=[database name,table name]
        
        s=''
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="2004veva",database=x[0])
        mycursor=mycon.cursor()
        p=x[1]#---------->table name
        q=str(p)
        mycursor.execute('show tables;')
        f=mycursor.fetchall() #list of all tables
        m=[]
        for i in list(f):
            i=funcmod.remove_brackets(i)
            m+=[i]                                                                                                  #q-table name , m-list of table name
        if q in m:
                  mycursor.execute('DESC '+str(p)+';') 
                  g=mycursor.fetchall()
                  l=[]                                                                                                 
                  for j in g:
                      l+=[j[0]] 
                                                                                                                   
                  for j in l:       #printing of titles 
                      print(j,end='\t\t\t')
                  mycursor.execute('select * from '+str(q)+';')
                  c=mycursor.fetchall()
                  n=[]
                  for d in c:
                      print() 
                      for e in d:
                          print(e,end='\t\t\t')                  ######check if table is alligned if only first name of customer is used################
        else:  
                print("not found")    
    


def addengineer():
    global logged_in_as
    clear()
    print("Add Engineer\n\n")
    print("(press enter anytime to exit the process)\n\n")
    proceed=0
    a=input("Engineer Name:")
    if a:
        proceed=1
    if proceed:
        print("Date of Joining-")
        b=input("Enter the day of the month:")
        if b and b.isdigit() and 0<int(b) and 31>=int(b):
            proceed=1
        elif b:
            print("Invalid input. Terminating")
            proceed=0
            time.sleep(2)
        
    if proceed:
        c=input("Enter month number 01-January to 12-December:")
        if c and c.isdigit() and 0<int(c) and 12>=int(c) and len(c)==2:
            proceed=1
        elif c:
            print("Invalid input. Terminating")
            proceed=0
            time.sleep(2)
    if proceed:
        d=input("Enter the year in YYYY form:")
        if d and len(d)==4:
            proceed=1
        elif d:
            print("Invalid input. Terminating")
            proceed=0
            time.sleep(2)
    if proceed:
        e=input("Annual salary in INR:")
        if e and e.isdigit():
            proceed=1
        elif e:
            print("Invalid Input!Terminating")
            proceed=0
            time.sleep(2)
    if proceed:
        print("Creating!!")
        time.sleep(0.5)
        print("Generating engineer id!!")
        x=engineer_id()
        time.sleep(0.5)
        print("Adding data to database!!")
        cssqlmodules.custom3([logged_in_as,x,a,b,c,d,e])
        print("Done!!")
        time.sleep(2)
        clear()



#General variables




#Changing the working directory
os.chdir(r'C:\Users\Admin\Desktop\Megascopia')


#Mains
update_users()

load_state=loading_screen.load()   
clear()

logged_in=0
while load_state==1:
    if not logged_in:
        logged_in_as=login_megascopia.login([load_state]+userslist)
        update_users()
    
    if logged_in_as and not logged_in_as == 1:
       logged_in=1
       clear()
       print("Hello "+logged_in_as+'\n\n\n')
       print('1.Add a project')
       print('2.View Ongoing or Past Projects')
       print('3.Update project details')
       print('4.View Engineers')
       print('5.Add Engineers')
       print('6.Update Engineer Data')
       print('7.Search Projects')
       print('8.Logout')
       choice=input()
       if choice=='1':
           clear()
           addproject()

       if choice=='2':
           clear()

           cssqlmodules.view_tables(logged_in_as, 'projectdetails')
           print('\n\n')
           cssqlmodules.view_tables(logged_in_as,'projectfinance')
           print('\n\n')
           cssqlmodules.view_tables(logged_in_as,'customerdetails')
           print('\n\n')
           input("Press enter to return")
           
       if choice=='3':
           a=logged_in_as
           b='projectdetails'
           cssqlmodules.update_table_records(a,b)

       if choice=='5':
           clear()
           addengineer()


       if choice=='6':
           a=logged_in_as
           b='engineers'
           cssqlmodules.update_table_records(a,b)                                                       
       if choice=='8':
            print('\n\n')
            print('Successfully Logged Out!!')
            input("Press Enter to continue")
            logged_in=0
       if choice=='4':
            clear()
            cssqlmodules.view_tables(logged_in_as,'engineers')
            print('\n\n')
            input("Press Enter to Home")
       if choice=='7':
           a=logged_in_as
           b='projectdetails'
           cssqlmodules.search_rec(a,b)
           
    elif logged_in_as==1:
        load_state=0
print("\n\nSee you again!")
print("Press enter to close")
input()
