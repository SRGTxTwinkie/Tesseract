import Pends
from NextClaim import NextClaim
from keyboard import add_hotkey, wait
from time import sleep

delay = 0.3
f4 = 0

def main():

    add_hotkey('alt+1', lambda:Pends.C258_1())
    add_hotkey('shift+alt+1', lambda:Pends.C258_3())

    add_hotkey('alt+2', lambda:Pends.C258_2())
    add_hotkey('shift+alt+2', lambda:Pends.C258_4())

    add_hotkey('alt+3', lambda:Pends.C237())
    add_hotkey('alt+4', lambda:Pends.C104())
    add_hotkey('f9', lambda:NextClaim())

    print('Pends running Alt+#')

    wait('ctrl+alt+end')

    print('Ended Script')
    exit(0)

if __name__ == '__main__':
    main()