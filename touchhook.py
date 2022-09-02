import win32gui
import win32con
import win32api

from datetime import datetime

class TouchHook(object):
    def __init__(self, hwnd, tsState):
        self.tsState = tsState
        self.oldWndProc = win32gui.SetWindowLong(hwnd, win32con.GWL_WNDPROC, self.wndProc)
    
    def handleTouchMessage(self, wParam, lParam):
        x = win32api.HIWORD(lParam)
        y = win32api.LOWORD(lParam)
        code = win32api.HIWORD(wParam)
        id = win32api.LOWORD(wParam)
        print(datetime.now(), id, code, x, y)

    def wndProc(self, hwnd, msg, wparam, lparam):
        try:
            # 触摸屏 按下
            if msg == win32con.WM_NCHITTEST:
                self.tsState["down"] = True
                # self.handleTouchMessage(wparam, lparam)
            # 触摸屏 抬起
            if msg == win32con.WM_SETCURSOR:
                self.tsState["down"] = False
                # self.handleTouchMessage(wparam, lparam)
            return win32gui.CallWindowProc(self.oldWndProc, hwnd, msg, wparam, lparam)
        except:
            pass
