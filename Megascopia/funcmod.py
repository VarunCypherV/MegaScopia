#some of basic functions defined:
def remove_last_element_of_a_str(s):
    a=len(s)
    d=""
    for i in range(a):
       if i!=a-1:
            d+=s[i]
       else:
            pass
    return(d)


def remove_brackets(s):
    a=""
    for i in s:
        if str(i) in ['(',')']:
            pass
        else:
            a+=i
    return a



        

   
        
    
