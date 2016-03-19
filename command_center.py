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
    keybd_event(Base[Key], 0, 2, 0)

def key_down(Key):
    keybd_event(Base[Key], 0, 1, 0)

def press(Key):
    key_down(Key)
    time.sleep(.1)
    key_up(Key)
    
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
    key_down('LSHIFT')
    key_down(hotkey)
    time.sleep(.1)
    key_up('LSHIFT')
    key_up(hotkey)

def reset_to_hotkey(hotkey):
    key_down('CTRL')
    key_down(hotkey)
    time.sleep(.1)
    key_up('CTRL')
    key_up(hotkey)

def select_hotkey(hotkey):
    press(hotkey)

def exit_menu():
    press('g')

def glhf():
    press('ENTER')
    press('g')
    press('l')
    press('h')
    press('f')
    press('ENTER')

def gg():
    press('ENTER')
    press('g')
    press('g')
    press('ENTER')

def find_cc_at_start():
    win32api.SetCursorPos([ int( (screen_x / 2) + (screen_x / 12) ) , int( (screen_y / 2) + (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_master)
    win32api.SetCursorPos([ int( (screen_x / 2) + (screen_x / 12) ) , int( (screen_y / 2) - (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_master)
    win32api.SetCursorPos([ int( (screen_x / 2) - (screen_x / 12) ) , int( (screen_y / 2) + (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_master)
    win32api.SetCursorPos([ int( (screen_x / 2) - (screen_x / 12) ) , int( (screen_y / 2) - (screen_y / 12) ) ])
    left_click()
    add_to_hotkey(hk_master)

def worker():
    select_hotkey(hk_master)
    press('TAB')
    press('s')

def hell_its_about_time():
    center()
    exit_menu()
    glhf()
    screen_drag_select()
    add_to_hotkey(hk_master)
    find_cc_at_start()
    worker()