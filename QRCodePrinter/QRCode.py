import sys
from time import sleep
import pyautogui as pyg


def save_print(disp):
    pyg.hotkey('win', 'shift', 's')
    sleep(1)
    pyg.moveTo(1013, 112)
    pyg.dragTo(1326, 478, duration=0.5)
    sleep(1)

    pyg.click(x=1450, y=660)
    sleep(1)
    pyg.hotkey('ctrl', 's')
    sleep(0.8)
    pyg.write(f'QRCode_{disp}')
    sleep(0.2)
    pyg.press('enter')
    sleep(1)
    pyg.hotkey('alt', 'f4')
    sleep(0.5)

    pyg.click(x=1450, y=660)
    pyg.press('pgup')
    sleep(0.3)

sleep(3)

# id do item do share
numero_id = 495

# range --> numero que vai no nome (ultimo é sempre -1)
for i in range(4, 5):

    # Nome do ativo
    ativo = f'GVC000{i}'

    pyg.leftClick(x=481, y=749)
    pyg.press('backspace', presses=3)
    pyg.write(str(numero_id))

    pyg.press('tab', presses=6, interval=0.2)
    sleep(0.2)
    pyg.write(ativo)

    numero_id += 1

    pyg.hotkey('alt', 'tab')
    seguir = input('-->')
    if seguir == '':
        save_print(ativo)
    else:
        sys.exit()
