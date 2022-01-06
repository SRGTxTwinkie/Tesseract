import os
import time
import keyboard

print('\nstarting browser\n')

os.startfile(r"C:\\Users\\rya72398\\OneDrive - Spectrum Health\\Desktop\\Centricity.url")
os.startfile(r"C:\\Users\\rya72398\\OneDrive - Spectrum Health\\Desktop\\Business Insider.url")
os.startfile(r"C:\\Users\\rya72398\\OneDrive - Spectrum Health\\Desktop\\PolicyTech.url")

keyboard.wait('esc')

print('starting facets')

os.startfile(r"C:\\Users\\rya72398\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Facets\\facets1.lnk")

keyboard.wait('space', suppress=True)

keyboard.write('rya72398')
keyboard.send('tab')
time.sleep(0.2)
keyboard.write('Password1!')
keyboard.send('enter')

time.sleep(2)

keyboard.send('ctrl+f11')
keyboard.send('down')
keyboard.send('enter')

time.sleep(1)

os.system("python C:\\Users\\rya72398\\automation\\Automation\\base.py")

print('\ndone\n')

exit(0)