from keyboard import send
from time import sleep

def NextClaim():
    delay = 0.2

    #Highlight Finished Claim
    send('alt+tab')
    sleep(delay)
    send('alt+h')
    send('alt+h')
    send('left')
    send('enter')

    #Copy Next Claim
    sleep(delay)
    send('down')
    send('ctrl+c')
    sleep(delay)

    #Enter Claim in Facets
    sleep(delay)
    send('alt+tab')
    sleep(delay)
    send('ctrl+o')
    send('ctrl+v')
    send('enter')
    send('f3')
