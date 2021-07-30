from keyboard import send, write
from time import sleep

import keyboard
import keyboard as kb
import pyperclip


claimNum = ''

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

    sleep(1)

    send('shift+f8')
    send('enter')
    sleep(delay)
    sleep(delay)
    send('tab')
    send('space')
    sleep(delay)
    sleep(delay)
    send('shift+tab')
    sleep(delay)
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

    for i in range(24):
        send('tab')
    
    sleep(delay)
    sleep(delay)

    send('space')
    send('tab')

    write('OX6')
    send('enter')
    
def C258_2():
    delay = 0.3

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
    sleep(delay)

    #Override PCA
    send('ctrl+up')
    send('alt+a')
    send('o')
    send('c')
    sleep(delay)
    sleep(delay)

    for i in range(15):
        send('tab')
    
    sleep(delay)
    sleep(delay)

    send('space')
    send('tab')

    write('PCO')
    send('enter')

def C258_3():

    delay = 0.2

    global claimNum

    claimNum = pyperclip.paste()

    sleep(1)
    #Get the date
    send('shift+f10')
    send('a')
    send('shift+f10')
    send('c')

    #Transfer to Claim Inquiry
    send('alt+t')
    send('c')
    send('enter')
    send('enter')

    sleep(delay)

    #Enter Dates
    for i in range(5):
        send('tab')
    
    send('shift+f10')
    send('a')
    send('ctrl+v')

    send('tab')

    send('shift+f10')
    send('a')
    send('ctrl+v')

    send('enter')
    send('y')