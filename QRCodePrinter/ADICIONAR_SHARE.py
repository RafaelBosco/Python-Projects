from time import sleep
import pyautogui as pyg

sleep(3)

# range --> numero que vai no nome (ultimo é sempre -1)
for i in range(1, 7):

    # Nome do ativo
    dis = f'GVC000{i}'

    pyg.click(x=360, y=280)
    sleep(2.2)

    # seleção da "categoria"
    pyg.press('down', presses=3, interval=0.4)

    sleep(0.5)
    pyg.press('enter')
    pyg.press('tab')
    pyg.write(dis)
    pyg.click(x=866, y=176)
    sleep(1.5)
