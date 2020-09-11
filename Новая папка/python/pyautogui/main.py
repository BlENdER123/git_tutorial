import pyautogui as pg
import time

# pg.move(50, 50, 0.5)  сдвигает мышь на определенное количество пикселей относительно ее позиции в данный момент

#pg.moveTo(0, 0, 0.5)  сдвигает мышь на определенное количество пикселей относительно экрана

print(pg.position())

pg.hotkey('winleft')

time.sleep(0.5)

pg.typewrite("firefox\n", 0.3)

time.sleep(2)

pg.typewrite("https://vk.com/im?sel=c146\n", 0.1)

time.sleep(4)

pg.typewrite('hello world', 0,3)

pg.typewrite(["enter"])

