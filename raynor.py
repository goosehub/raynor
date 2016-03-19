# Boilerplate
from command_center import *

# Loading wait
# print("Ready to roll out")
# time.sleep(5)
# x, y = win32api.GetCursorPos()
# print(x)
# print(y)
# time.sleep(5)
# x, y = win32api.GetCursorPos()
# print(x)
# print(y)
# time.sleep(5)
# x, y = win32api.GetCursorPos()
# print(x)
# print(y)
# time.sleep(5)
# x, y = win32api.GetCursorPos()
# print(x)
# print(y)

# center()
# hell_its_about_time()
time.sleep(5)

# Image imports
from PIL import Image
from PIL import ImageGrab
import pyscreenshot as ImageGrab
# import numpy
# import cv2
# import pytesser
    
if __name__ == '__main__':
    # print( int(screen_x - (screen_x / 1.5))  , int(screen_y - (screen_y / 5)) , int(screen_x * 0.6) , int(screen_y - (screen_y / 10)) )
    # im=ImageGrab.grab(bbox=( int(screen_x - (screen_x / 1.5))  , int(screen_y - (screen_y / 5)) , int(screen_x * 0.6) , int(screen_y - (screen_y / 10)) ))
    # im=ImageGrab.grab(bbox=( 600, 700, 1000, 800 ) )
    im=ImageGrab.grab()
    im.show()
    ImageGrab.grab_to_file('im.png')

import win32gui
import win32ui 

w = 500
h = 500

hwnd = win32gui.GetForegroundWindow()
wDC = win32gui.GetWindowDC(hwnd)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, 'tmp.bmp')
# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())