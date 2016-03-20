# Dead or Alive
# Alan O'Donohoe 16/3/15
from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HEART)
        sleep(200)
        display.show(Image.HEART_SMALL)
        sleep(200)     
    else:
        display.show(Image.SKULL)
