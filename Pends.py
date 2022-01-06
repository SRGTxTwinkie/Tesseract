from keyboard import send, write, wait
from time import sleep
import NextClaim

import keyboard
import keyboard as kb
import pyperclip

C258 = [24, 15, 4, 258]
C266 = [23, 14, 3, 266]

pend = C266


claimNum = ''

def SwapPend():
    global pend
    if pend[3] == 266:
        pend = C258
    elif pend[3] == 258:
        pend = C266
    print('Current pend is now: ' + str(pend[3]))

def C237():

    delay = 0.3
    print('C237')
    
    sleep(1)

    send('shift+f8')
    sleep(delay)
    send('enter')
    sleep(delay)
    write('facets_ba')
    sleep(delay)
    sleep(delay)
    send('tab')
    sleep(delay)
    send('tab')
    sleep(delay)
    sleep(delay)
    write('c518')
    sleep(delay)
    send('enter')

    print('Done')

def C104():

    delay = 0.3
    print('C104')
    
    sleep(1)

    send('shift+f8')
    sleep(delay)
    send('enter')
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    send('tab')
    sleep(delay)
    send('space')
    send('shift+tab')
    sleep(delay)
    write('hmcr')
    sleep(delay)
    send('tab')
    sleep(delay)
    send('tab')
    sleep(delay)
    write('c061')
    sleep(delay)
    send('enter')

    print('Done')

def C258_1():
    delay = 0.3

    pyperclip.copy(claimNum)

    sleep(1)
    #Add Note
    send('ctrl+down')
    send('ctrl+down')
    sleep(delay)
    send('alt+e')
    send('a')
    write('Replaced by claim ')
    send('ctrl+v')
    sleep(delay)
    send('enter')
    sleep(delay)

    #EOB Code
    send('ctrl+up')
    sleep(delay)
    send('alt+b')
    write('k33')
    send('enter')
    send('tab')
    send('enter')
    sleep(delay)

    #Override Deny All
    send('alt+a')
    send('o')
    send('c')
    sleep(delay)
    sleep(delay)

    for i in range(pend[0]):
        send('tab')
    
    sleep(delay)
    sleep(delay)

    send('space')
    send('tab')

    write('OX6')
    send('enter')

    send('f3')
    
def C258_2():
    delay = 0.3

    global claimNum

    sleep(1)
    #Add Note

    send('ctrl+down')
    send('ctrl+down')
    sleep(delay)
    send('alt+e')
    send('a')
    write('Replaces claim ')
    send('ctrl+v')
    send('enter')
    sleep(1)

    #Override PCA
    send('ctrl+up')
    send('alt+a')
    send('o')
    send('c')
    sleep(delay)
    sleep(delay)

    for i in range(pend[1]):
        send('tab')
    
    sleep(delay)
    sleep(delay)

    send('space')
    send('tab')

    write('PCO')
    send('enter')

    send('f3')

def C258_3():

    delay = 0.2

    global claimNum

    claimNum = pyperclip.paste()


    sleep(1)

    send('ctrl+down')

    for i in range(pend[2]):
        send('tab')


    #Get the date
    send('shift+f10')
    send('a')
    send('shift+f10')
    send('c')

    sleep(delay)

    #Transfer to Claim Inquiry
    send('alt+t')
    send('c')
    send('enter')
    # send('down')
    send('down')         
    send('enter')

    sleep(delay)

    sleep(delay)

    #Enter Dates
    for i in range(5):
        send('tab')
    
    send('shift+f10')
    send('a')
    send('ctrl+v')

    sleep(delay)
    sleep(delay)

    send('tab')

    sleep(delay)
    sleep(delay)

    send('shift+f10')
    send('a')
    send('ctrl+v')

    sleep(delay)

    send('enter')
    send('y')

def C258_4():
    sleep(1)

    delay = 0.2

    send('ctrl+o')
    sleep(delay)
    send('n')
    sleep(delay)
    send('ctrl+c')

    sleep(delay)
    sleep(delay)

    send('esc')
    # sleep(delay)
    # send('f3')
    sleep(delay)
    send('f4')
    sleep(delay)
    
    send('ctrl+f4')
    sleep(delay)
    send('ctrl+f4')
    
    sleep(delay)
    send('ctrl+o')
    sleep(delay)
    send('enter')

    return


def YearlyCodeRoute():

    delay = 0.3
    print('C104')
    
    sleep(1)

    send('shift+f8')
    sleep(delay)
    send('enter')
    sleep(1)
    send('tab')
    send('space')
    send('shift+tab')
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    write('prc.cfg')
    sleep(delay)
    send('tab')
    sleep(delay)
    send('tab')
    sleep(delay)
    write('c178')
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    sleep(delay)
    send('enter')

    sleep(delay)
    NextClaim.NextClaim()

    print('Done')
