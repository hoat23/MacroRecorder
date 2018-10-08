#coding: utf-8
#Developer: Deiner Zapata Silva
#https://recursospython.com/codigos-de-fuente/grabador-teclado-mouse/
#http://nitratine.pythonanywhere.com/youtube/python-hotkeys
#http://recursospython.com/guias-y-manuales/autopy-toolkit/

#pip install autopy
#pip install pynput


from pynput.keyboard import Key, Listener 
from pynput import mouse
from pynput import keyboard
import logging

# LOGGING --------------------------------------------------------------
# Level of logging: 
#   1 -> DEBUG   : Detailed information, typically of interest only when diagnostigs problems.
#   2 -> INFO    : Confirmation that things are working as expected
#   3 -> WARNING : An indication that somtehin unexpected happened. Indicate problems in the near future.
#   4 -> ERROR   : Due to a more serious problem, the software has not been able to perform some function.
#   5 -> CRITICAL: A serious error, indicating that the program itself may be uneble to continue running.

formater = '%(asctime)s:%(message)s'

logging.basicConfig(level=logging.DEBUG,#filename="keylogger.log",
                    format=formater) #LogRecord attributes
logger = logging.getLogger(__name__)

#file_handler.setLevel(logging.DEBUG)
#file_handler = logging.FileHandler('keylogger.log')
#file_handler.setFormatter(formater)
#logger.addHandler(file_handler)

print("init_logging() "+str(logger)+" - [level=DEBUG]")
logging.debug("LOGGING INICIALIZADO")


# KEYBOARD -------------------------------------------------------------
#defining function to print when key is pressed 
def on_press(key):
    logging.debug('{0} pressed'.format(key))

#defining function to print when key is released 
def on_release(key): 
    logging.debug('{0} release'.format(key)) 
    if key == Key.esc:
        # Stop listener 
        return False 
# MOUSE ---------------------------------------------------------------
def on_move(x, y):
    logging.debug('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    logging.debug('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y)))
    #if not pressed:
        # Stop listener
    #    return False

def on_scroll(x, y, dx, dy):
    logging.debug('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
# COLLECT ALL --------------------------------------------------------
# Collect events until released 
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) or Listener(on_press=on_press, on_release=on_release) as listener:
    #listener.join()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

#