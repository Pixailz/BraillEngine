from utils import *

# this file is here to disable cursor and re enable it when the program exit

atexit.register(ansi.enableCursor)

ansi.disableCursor()
