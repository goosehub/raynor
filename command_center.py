# Base imports
import time
import random

# Windows imports
import win32con
import win32api
from win32api import keybd_event, mouse_event

# Config
from config import *

# Keys
from keys import *

def key_up(Key):
    keybd_event(Key, 0, 2, 0)

def key_down(Key):
    keybd_event(Key, 0, 1, 0)

def press(Key):
    key_down(Base[Key])
    time.sleep(.1)
    key_up(Base[Key])
    
def left_click_down():
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    
def right_click_down():
    mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    
def left_click_up():
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def right_click_up():
    mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    
def left_click():
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(.1)
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def right_click():
    mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(.1)
    mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def center():
    win32api.SetCursorPos([int(screen_x / 2), int(screen_y / 2)])

def screen_drag_select():
    win32api.SetCursorPos([0, 0])
    left_click_down()
    win32api.SetCursorPos([screen_x, screen_y])
    left_click_up()
    center()

def add_to_hotkey(hotkey):
    key_down(Base['LSHIFT'])
    key_down(Base[hotkey])
    time.sleep(.1)
    key_up(Base['LSHIFT'])
    key_up(Base[hotkey])

def reset_to_hotkey(hotkey):
    key_down(Base['CTRL'])
    key_down(Base[hotkey])
    time.sleep(.1)
    key_up(Base['CTRL'])
    key_up(Base[hotkey])

def select_hotkey(hotkey):
    key_down(Base[hotkey])
    key_up(Base[hotkey])

def exit_menu():
    key_down(Base['g'])
    time.sleep(.1)
    key_up(Base['g'])

def glhf():
    key_down(Base['ENTER'])
    time.sleep(.1)
    key_up(Base['ENTER'])
    key_down(Base['g'])
    time.sleep(.1)
    key_up(Base['g'])
    key_down(Base['l'])
    time.sleep(.1)
    key_up(Base['l'])
    key_down(Base['h'])
    time.sleep(.1)
    key_up(Base['h'])
    key_down(Base['f'])
    time.sleep(.1)
    key_up(Base['f'])
    key_down(Base['ENTER'])
    time.sleep(.1)
    key_up(Base['ENTER'])

def find_cc_at_start():
    win32api.SetCursorPos([ int( (screen_x / 2) + (screen_x / 12) ) , int( (screen_y / 2) + (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_cc)
    win32api.SetCursorPos([ int( (screen_x / 2) + (screen_x / 12) ) , int( (screen_y / 2) - (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_cc)
    win32api.SetCursorPos([ int( (screen_x / 2) - (screen_x / 12) ) , int( (screen_y / 2) + (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_cc)
    win32api.SetCursorPos([ int( (screen_x / 2) - (screen_x / 12) ) , int( (screen_y / 2) - (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_cc)

def worker():
    select_hotkey(hk_cc)
    key_down(Base['s'])
    time.sleep(.1)
    key_up(Base['s'])

def hell_its_about_time():
    exit_menu()
    glhf()
    find_cc_at_start()
    worker()
    screen_drag_select()
    add_to_hotkey(hk_workers)