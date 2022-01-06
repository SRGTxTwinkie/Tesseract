from time import sleep
import pytesseract
from PIL import ImageGrab
import pyautogui
import mouse
import win32gui, win32ui
from win32api import GetSystemMetrics
import pyperclip
import pywinauto
import re


#Confusing win32 commands

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)          #I think DC refers to the content that's actually /in/ the window
hwnd = win32gui.WindowFromPoint((0,0))          #This is just getting the window handle for easy finding later
facets_hwnd = win32gui.FindWindow(None, "Facets - ")
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))  #Screen size for cursor math

my_tesseract = 'C:/Users/rya72398/AppData/Local/Programs/Tesseract-OCR/tesseract'

try:
    pytesseract.pytesseract.tesseract_cmd = my_tesseract #Put your own location here
except(Exception):
    print(Exception)
    print('Need correct tesseract location\n Maybe here: /AppData/Local/Programs/Tesseract-OCR/tesseract')
    print('Or here: /Programs (86)/Tesseract-OCR/tesseract?')


try:    
    facets = pywinauto.Application(backend="win32").connect(title_re="^Facets*", found_index=0) # The trys are there to prevent ugly errors

except(Warning):
    print('There was a warning')
        


before = pyautogui.position()           #This part moves the mouse back where it should be after changing the window,
facets.top_window().set_focus()         #I've had trouble with that before
mouse.move(x=before[0], y=before[1])
facets.top_window().wait('visible')


mouse.wait(button='left',target_types='down')       #Watch for next mouse down
orig_mousex, orig_mousey = pyautogui.position()     #Save coords for rectangle

box = (orig_mousex-2, orig_mousey+2, orig_mousex+1, orig_mousey-1) #The + and - are to make it a bit easier to slect?

while mouse.is_pressed(button='left'):              #This loop goes until you release the button
    mousex, mousey = pyautogui.position()
    box = (orig_mousex, orig_mousey, mousex, mousey)
        
    dcObj.DrawFocusRect(box)                            #This is a win32gui thing, draws a focus box with dotted lines and stuff
    win32gui.InvalidateRect(facets_hwnd, monitor, True) # Refresh the entire monitor, clears the whole screen, especially the stuff inside the rectangle


im = ImageGrab.grab(box)                                #Pillow grabs the most recent coords of the box you dragged
text = pytesseract.image_to_string(im,config='digits')  #pytesseract lets you only grab digits



##This is important, sometimes tesseract will interpret a cut off letter as a - or . or +"
##Not sure how to fix it easily


if len(text) != 12:
    print('The number scanned was not 12 digits')


print(text)

pyperclip.copy(str(text))