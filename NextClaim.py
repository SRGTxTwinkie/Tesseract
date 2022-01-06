from subprocess import Popen
from pywinauto import Application
from keyboard import send
from time import sleep
import warnings

warnings.filterwarnings('ignore', message='32')

def NextClaim():   
    delay = 0.2
    sleep(delay)
    app= Application(backend="uia").connect(title_re=".*Excel*", found_index=0)
    app.top_window().set_focus()
    app.top_window().wait('visible')
    #Highlight Finished Claim
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

    try:    
        app= Application(backend="win32").connect(title_re="^Facets*", found_index=0)

    except(Warning):
        print('There was a warning')

    app.top_window().set_focus()
    app.top_window().wait('visible')

    #Enter Claim in Facets
    sleep(delay)
    sleep(delay)
    send('ctrl+o')
    send('ctrl+v')
    send('enter')
    send('f3')