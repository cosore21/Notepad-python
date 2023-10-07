import random
import pyautogui as pg
import time

words=("hi", "hello","Good morning")
time.sleep(8)

for i in range(100):

    a=random.choice(words)
    pg.write("you are a"+ a)
    pg.press("Enter")