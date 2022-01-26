from time import sleep
import pyautogui as pyg

pyg.hotkey('win', 'shift', 's')
sleep(1)
pyg.moveTo(1013, 112)
pyg.dragTo(1326, 478, duration=0.5)
