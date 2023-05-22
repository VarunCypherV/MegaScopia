#to view table syntax:
import mysql.connector
import funcmod #user def
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
                  for j in l:
                      print(j,end='\t\t\t')
                  mycursor.execute('select * from '+str(q)+';')
                  c=mycursor.fetchall()
                  n=[]
                  for d in c:
                      print()
                      for e in d:
                          print(e,end='\t\t\t')                 
        else: 
                print("not found")
view_data(x)









































'''Varun
work for you
I am supplying a variable x which is a list contaning data how i gave in the comment next to it
Using that you need to print all the values in the table i specified(No need to format and all just print)
'''
    

    #Print all the values in that table every column

#sql username:root password:vamsithehero


#p.s you can remove the comments, later ill just copy paste the code from this
