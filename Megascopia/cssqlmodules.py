#welcome to sql modules :)
import mysql.connector
import funcmod #user def
mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero")
mycursor=mycon.cursor()
 #Engineers ProjectDetails ProjectFinance CustomerDetails

#-------------------------------------------------------------------------------------------------------------------------------------------------
def create_database(d):
        global mycursor
        
        if d:
            try:
                
                mycursor.execute('CREATE DATABASE IF NOT EXISTS ' + d +';')
            except Exception as e:
                print(e)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
def create_table(x): #[user,table,details]
    try:
        mycursor.execute('USE '+x[0]+';')
        
        mycursor.execute('CREATE TABLE '+x[1]+' ('+x[2]+')'+';')             
    except Exception as e:
            print(e)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def insert_into_table():
   try:
        a=input("enter your database: ")
        b=input("enter the table name where u wanna enter records: ")
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero",database=a)
        mycursor=mycon.cursor()
        mycursor.execute('desc '+str(b)+';')
        c=mycursor.fetchall()
        s=""
        print(c)
        for i in c:
                print(i)
                d=input("pls enter value for the above in \' \':")
                s+=str(d)
                s+=" "+","
        o=funcmod.remove_last_element_of_a_str(s)
        o=o.rstrip()
        print('INSERT INTO '+str(b)+' VALUES('+str(o)+');')
        mycursor.execute('INSERT INTO '+str(b)+' VALUES('+str(o)+');') #o means all the details like 3,dude,class 11
        mycon.commit()
        print("done")
   except Exception as e:
           print(e)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_table_records(a,b):
     try:
        while True:
             mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero",database=a) # idea  to get where constriants and
             mycursor=mycon.cursor()
             mycursor.execute('desc '+str(b)+';')       #update pandey set name='pand' where sno='1' and name='pandey'
             z=mycursor.fetchall()
             mycursor.execute('select * from '+str(b)+';')
             g=mycursor.fetchall()
             e=int(input('enter the number of records you want to update')) 
             qw=""
             for i in range(e):
               f=input("enter the attribute you want to update eg)sno or name:")
               if f=='projectid' or 'engineerid':
                       print('sry cant change the project id its unique and permanent')
                       break
               else:
                     change=input('enter the change in value')               
               qw=qw+str(f)+"="+" "+'\"'+str(change)+'\"'+','
             m=funcmod.remove_last_element_of_a_str(qw)
             nsd=int(input('enter the number of constrsints:'))
             assd=''
             for i in range(nsd):
                      c=input("enter one constraint with which you want to refer your record like eg)sno")
                      f=input('enter the value of that constrain:')
                      j=c+'= \''+f+'\''
                      
                      if i!=nsd-2: #nsd-2 for putting and instead of , before last constraint........
                           assd+=j+','
                      elif i==nsd-2:
                           assd+=j+' '+'AND'+' '
                      else:
                            pass
             o=funcmod.remove_last_element_of_a_str(assd)
             mycursor.execute('select * from '+str(b)+' where '+str(o)+';')
             do=mycursor.fetchall()
             if do!=[]:
                       print('update '+str(b)+' SET '+str(m)+' where '+str(o)+';')
                       mycursor.execute('update '+str(b)+' SET '+str(m)+' where '+str(o)+ ';')
                       mycon.commit()
             else:
                        print("no rec")
     except Exception as e:
                print(e)
#update_table_records(a,b)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_table(x):#[user,table,<column names>]                     
        selector=''
        for i in x[2]:
                
                selector=selector+i+','
        else:
                selector=selector.rstrip(',')
        try:
              
              mycursor.execute("USE "+x[0]+';')
              
              mycursor.execute("SELECT "+selector+' FROM '+x[1]+';')
              
              myrecords=mycursor.fetchall()
               
        except Exception as e:
                print(e)
                myrecords=0
        return myrecords
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drop_database():
        try:
               a=input("enter your database: ")
               mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero")
               mycursor=mycon.cursor()
               mycursor.execute('show databases')
               d=mycursor.fetchall()
               g=str(d)
               print(g)
               if a in g :
                   mycon=mysql.connector.connect(host="localhost",user="root",passwd="2004veva",database=a) 
                   mycursor=mycon.cursor()
                   b=input("are you sure you want to drop your database.press Y/N: ")
                   if str(b)=='Y':
                       mycursor.execute(' drop database '+str(a)+';')
                       print("dropped")
                   else:
                        print("process reverted")
               else:
                       print("sorry databse does not exist")
        except Exception as e:
                print(e)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
     try:
        a=input("enter your database: ")
        b=input("enter the table name where u wanna delete records: ")
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero",database=a)
        mycursor=mycon.cursor()
        n=input("enter your desired constraint eg) sno=1")
        mycursor.execute(' DELETE FROM '+str(b)+' where '+str(n)+';')
        print(' DELETE FROM '+str(b)+' where '+str(n)+';')
        
        mycon.commit()
     except Exception as e:
        print(e)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def custom1(x):#x=[user,a,b,c,d,e,f,g,h,l,m,id_]
        x=tuple(x)
        user,a,b,c,d,e,f,g,h,l,m,id_=x
        
        mycursor.execute("USE "+x[0]+';')
        
        mycursor.execute("INSERT INTO projectdetails VALUES("+str(id_)+',"'+f+'","'+a+'","'+b+'",'+c+','+'"'+e+'-'+d+'-01'+'","'+'PENDING'+'",'+m+')')
        
        mycursor.execute("INSERT INTO customerdetails VALUES("+'"'+f+'","'+g+'",'+h+')')
        
        mycursor.execute("INSERT INTO projectfinance VALUES("+str(id_)+','+l+',0,"PENDING")')
        
        mycon.commit()
        
        
#a= construction site string b=project description string c=budget int d=month number e=year f=customer name string g=customer address string h=customer phno int l=amount int m=head engineer id int


def custom2(x):#x=[user,a,b,c,d,e,f,l,m,id_]

        x=tuple(x)
        user,a,b,c,d,e,f,g,h,l,m,id_=x
        
        mycursor.execute("USE "+x[0]+';')
        mycursor.execute("INSERT INTO projectdetails VALUES("+str(id_)+',"'+f+'","'+a+'","'+b+'",'+c+','+'"'+e+'-'+d+'-01'+'","'+'PENDING'+'",'+m+')')
        
        mycursor.execute("INSERT INTO projectfinance VALUES("+str(id_)+','+l+',0,"PENDING")')
        mycon.commit()


def custom3(x): #x=[ user,id,a,b,c,d,e]
        x=tuple(x)
        user,id_,a,b,c,d,e=x
        id_=str(id_)

        mycursor.execute("USE "+user+';')
        
        mycursor.execute("INSERT INTO engineers VALUES("+id_+',"'+a+'",'+'0,"'+d+'-'+c+'-'+b+'",'+e+');')
        mycon.commit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def view_tables(a,b):
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero",database=a)
        mycursor=mycon.cursor()
        mycursor.execute('desc '+str(b)+';')
        c=mycursor.fetchall()
        l=[]
        for i in c:
                l+=[str(i[0])]      #got all the headrers in table
        mycursor.execute('select * from '+str(b)+';')
        d=mycursor.fetchall()
        m=[]
        for j  in d:
                m+=[j]   #got all the tuples data in list
        for j in range(len(m)):
                print()
                for i in range(len(l)):
                        if len(str(l[i]))<16:
                                 if [m[j]]!=[]  :
                                       print(l[i],":\t",m[j][i])
                                 else:
                                       pass
                        else:
                                if [m[j]]!=[]  :
                                       print(l[i],": ",m[j][i])
                                else:
                                       pass               
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search_rec(a,b):
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="vamsithehero",database=a)
        mycursor=mycon.cursor()
        mycursor.execute('desc '+str(b)+';')
        c=mycursor.fetchall()
        l=[]
        for i in c:
                l+=[str(i[0])]      #got all the headrers in table
        mycursor.execute('select * from '+str(b)+';')
        d=mycursor.fetchall()
        m=[]
        for j  in d:
                m+=[j]   #got all the tuples data in list

        d={}
        s=[]
        for j in range(len(m)):
                for i in range(len(l)):
                                 if [m[j]]!=[]  :                                         
                                         d[l[i]]=m[j][i]       
                                 else:
                                       pass
                s+=[d]
        search=int(input('enter the id of the record you want to access:'))
        for i in s:
                if i['projectid']==search:
                        c=s.index(i)
                        for i in s[c]:
                             print(i,':',s[c][i])
        
                else:
                        print('no rec found!!')
                
     
       
                        






































                
        
       

        
        
         
     
        
                

                
                
        


                
        
        
        
         
         
                
