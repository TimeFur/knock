import os, sys
import time
from pynput.mouse import Listener
import subprocess
import win32gui

class Mouse_listener():
    
    def __init__(self):
        self.time = time
        
    def on_move(self, x, y):
        print ("Pointer move to {0}".format(
                (x, y)))

    def on_click(self, x, y, button, pressed):
        print ('{0} at {1}'.format(
                'Pressed' if pressed else 'Release',
                (x, y)))
        if pressed:
            self.pressed_time = self.time.clock()
        else:
            self.release_time = self.time.clock()
            print "Release in {0}".format(
                    (self.release_time - self.pressed_time))
        
    def on_scroll(self, x, y, dx, dy):
        print ('Scrolled {0}'.format(
                (x, y)))
        return False


def openfolder(path):
    os.startfile(path)

open_list = []
def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        #print hex(hwnd), win32gui.GetWindowText( hwnd )
        open_list.append(win32gui.GetWindowText(hwnd))

class Win_watch():
    def __init__(self):
        self.open_list = []
        win32gui.EnumWindows(self.winEnumHandler, None)
        
    def winEnumHandler(self, hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            #print hex(hwnd), win32gui.GetWindowText( hwnd )
            self.open_list.append(win32gui.GetWindowText(hwnd))

def main():
    print "Knock center"
    win32gui.EnumWindows(winEnumHandler, None)
    
    w = Win_watch()
    
    for i in open_list:
        print i
        
    openfolder("D:workspace")
    
    time.sleep(0.3)
    win32gui.EnumWindows(winEnumHandler, None)
    for i in open_list:
        print i
    '''
    evt = Mouse_listener()
    with Listener(
            on_move = evt.on_move,
            on_click = evt.on_click,
            on_scroll = evt.on_scroll) as listener:
        listener.join()
    '''
    
    #time.sleep(1)
    path = os.getcwd()
    path = path + "/tool/nircmd.exe"
    runexe = path.replace("\\", "/")
    os.system(runexe + ' win close title "workspace"')
    
if __name__ == "__main__":
    main()
