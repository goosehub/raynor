# Windows imports
import win32con
import win32api

# Config
from config import *

def KeyUp(Key):
    keybd_event(Key, 0, 2, 0)

def KeyDown(Key):
    keybd_event(Key, 0, 1, 0)

def Press(Key, speed=1):
    rest_time = 0.05/speed
    if Key in Base:
        Key = Base[Key]
        KeyDown(Key)
        time.sleep(rest_time)
        KeyUp(Key)
        return True
    if Key in Combs:
        KeyDown(Base[Combs[Key][0]])
        time.sleep(rest_time)
        KeyDown(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][0]])
        return True
    return False
    
def left_click_down():
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    
def right_click_down():
    mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    
def left_click_up():
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def right_click_up():
    mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    
def left_click(t):
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(t)
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def right_click(t):
    mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(t)
    mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def center():
    win32api.SetCursorPos([int(screen_x / 2), int(screen_y / 2)])