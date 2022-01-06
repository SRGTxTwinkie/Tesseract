import Pends
from NextClaim import NextClaim
from keyboard import add_hotkey, wait
from time import sleep

delay = 0.3
f4 = 0

def myF4():
    global f4
    f4 += 1
    print(f4)

def main():

    add_hotkey('alt+1', lambda:Pends.C258_1())
    add_hotkey('shift+alt+1', lambda:Pends.C258_3())

    add_hotkey('alt+2', lambda:Pends.C258_2())
    add_hotkey('shift+alt+2', lambda:Pends.C258_4())

    add_hotkey('alt+3', lambda:Pends.C237())
    add_hotkey('alt+4', lambda:Pends.YearlyCodeRoute())

    add_hotkey('f9', lambda:NextClaim())
    add_hotkey('f4', lambda: myF4())

    add_hotkey('shift+alt+=', lambda:Pends.SwapPend())

    # add_hotkey('ctrl+`', lambda:Pends.AllInOne())

    print('Pends running Alt+#')
    print('^~1 -> Date for inquiry')
    print('~1 -> First replacement message')

    print('~2 -> Second replacement message')

    print('~3 -> Healthy newborn route')

    print('~4 -> HMCR route, notes recvd')

    print('f9 -> Next claim')
    print('Current working pend: ' + str(Pends.pend[3]))
    print('^~= -> change pend') 
    print('ctrl-alt-end ends')

    wait('ctrl+alt+end')

    print('Ended Script')
    exit(0)

if __name__ == '__main__':
    main()