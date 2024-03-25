try:
    from pynput import keyboard
except:
    print("installera pynput din lilla bullsmaskare")

def keyPress(key):
    
    return('{0}'.format(key))
    

def press():
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    
    