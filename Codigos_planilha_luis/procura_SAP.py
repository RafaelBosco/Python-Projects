import sys
import pyautogui as pyg
from time import sleep

sleep(3)
for i in range(26):
    pyg.click(x=58, y=242)
    pyg.press('down', presses=i)
    pyg.hotkey('ctrl', 'c')
    pyg.hotkey('alt', 'tab')
    sleep(0.5)
    pyg.click(x=194, y=218)
    pyg.hotkey('ctrl', 'v')
    pyg.press('enter')
    sleep(1)
    pyg.click(x=395, y=561)
    pyg.press('enter')
    sleep(1)
    pyg.write('bz01')
    pyg.press('enter')

    continua = input('-->')
    if continua != '':
        sys.exit()
    else:
        sleep(2)
        pyg.press('f3')
        sleep(0.5)
        pyg.click(x=1051, y=25)