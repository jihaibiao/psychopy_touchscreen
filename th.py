
import win32gui
from touchhook import TouchHook
th = None #the touch handler to be filled
winList = []
tsState = { "down": False }
#search through visible windows for the right handler
def callback (HWND, list_object):
    # print(type(win32gui.GetWindowText(HWND)))
    if 'PsychoPy' in win32gui.GetWindowText(HWND):
        try:
            # print(win32gui.GetWindowText(HWND))
            list_object.append(HWND)
        except:
            pass

#only execute this code once at the beginning
if th is None:
    win32gui.EnumWindows(callback, winList)
    th = TouchHook(winList[0], tsState)
    print('th initialized')