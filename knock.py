import os
from pynput.mouse import Listener

def on_move(x, y):
    print ("Pointer move to {0}".format(
            (x, y)))

def on_click(x, y, button, pressed):
    print ('{0} at {1}'.format(
            'Pressed' if pressed else 'Release',
            (x, y)))
    
def on_scroll(x, y, dx, dy):
    print ('Scrolled {0}'.format(
            (x, y)))
    return False

def openfolder(path):
    os.startfile(path)
    
def main():
    print "Knock center"
    #openfolder("D:")
    with Listener(
            on_move = on_move,
            on_click = on_click,
            on_scroll = on_scroll) as listener:
        listener.join()
    
if __name__ == "__main__":
    main()
