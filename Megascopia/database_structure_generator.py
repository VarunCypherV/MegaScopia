import cssqlmodules as handle

def generate_structure(x):#x=[user/database]
    
    handle.create_table([x,'customerdetails','customername varchar(30),permanentaddress char(255),phonenumber bigint'])
    handle.create_table([x,'projectfinance','projectid int,totalamount int,amountreceived bigint,status char(20)'])
    handle.create_table([x,'projectdetails','projectid int,customername varchar(30),constructionsite text,projectdescription text,projectbudget bigint,estimatedenddate date,projectstatus char(20),headengineerid int'])
    handle.create_table([x,'engineers','engineerid int,engineername char(40),noofprojectsdone int,dateofjoining date,annualsalary bigint'])
