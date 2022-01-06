import keyboard as kb
import win32gui as win
from time import sleep

cursorData = win.GetCursorInfo()
sleep(5)
print(cursorData)