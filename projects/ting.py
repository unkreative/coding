from audioop import mul
from operator import le
from pickle import TRUE
from textwrap import fill
import time
from turtle import screensize
from types import coroutine
import pyautogui
import numpy as np
import sys
from PIL import Image, ImageDraw
import tempfile
# from pillow import image
# screen_location = "/Users/lousergonne/Desktop/aaa.png"
screen_location = "/Users/lousergonne/Desktop/Screenshot 2022-02-28 at 11.32.26.png"
# screen_location = '/Users/lousergonne/Desktop/Screenshot 2022-03-01 at 10.29.52.png'
pyautogui.screenshot(screen_location)
green_value = [41,200,64]


x_cord = []
y_cord = []

im = Image.open(screen_location).convert('RGB')
im = im.resize((2560, 1600))
im.save(screen_location, dpi=(600, 600))
with Image.open(screen_location).convert('RGB') as pim:

    im  = np.array(pim)
    # Define the blue colour we want to find - PIL uses RGB ordering
    green = [0,0,255]
    green = [97,196,84]

    # Get X and Y coordinates of all blue pixels
    X,Y = np.where(np.all(im==green,axis=2))
    print(X)
    print()
    print(Y)
    print("len: ", len(X))
    print()

    import sys
    from PIL import Image, ImageDraw


    draw = ImageDraw.Draw(pim)
    num1 = 0
    while num1 <= len(X):
        # print(num1)
        if num1 < len(X):
            # print(num1)
            xx = X[num1]
            yy = Y[num1]
            multi = 1.569444444444444
            multi = 0.63716814159292
            multi = 1.527777777777778
            multi = 220/144
            cordinate = (xx, yy)
            num2 = 220/144
            cord2a = xx
            cord2b = yy
            cord2a = cord2a*num2
            cord2b = cord2b*num2
            # multi = 0.518181818181818
        
            cord2 = cord2a, cord2b
            # pyautogui.leftClick(cord2)

            # draw.point(cordinate, fill="green")
            draw.point(cord2, fill="red")
            # draw.point(cord3, fill="orange")
        num1 += 1
    # 
    pim.show()