import time
import os
import math
import random
L=['Building your database','Mining data','Constructing user interface','Demolishing useless data']
random.shuffle(L)

try:
    space=(os.get_terminal_size().columns()/2)*' '
except:
    space=' '*4*20  #tab_size x no. of tabs
def load():
    printvar='MEGASCOPIA'
    print(space[:len(space)-(math.floor(len(printvar)/2))]+printvar)
    time.sleep(1)
    print()
    
    printvar='Personalised Space for Builders'
    print(space[:len(space)-math.floor(len(printvar)/2)]+printvar)
    time.sleep(1)
    print('\n\n')

    for i in L:
        print(i,flush=True,end='')
        for j in range(5):
            print('.',end='',flush=True)
            time.sleep(0.1)
        print()
    print('\n\n')
    print(space+'LOADED!!')
    time.sleep(1.5)
    return(1)
    
    
    



