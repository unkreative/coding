import re
from PIL import Image
import numpy as np
import pyautogui as pg
import time
import subprocess

filename = 220314
filepath = '/Users/NLNEW/coding/indesign template working 3.indd'
subprocess.call(('open', filepath))
time.sleep(2)
screenshot_path = "/Users/NLNEW/Desktop/screen.png"
# screenshot_path = "/Users/lousergonne/Desktop/screen.png"
pg.screenshot(screenshot_path)

with Image.open(screenshot_path).convert('RGB') as pim:
    im = np.array(pim)

    green = [63, 197, 73]
    # green = [98, 196, 84]

    Y,X = np.where(np.all(im==green, axis=2))

    lx = len(X)
    lx = int(lx/2)
    xcord = X[0]
    ycord = Y[0]

    nx = 1.982142857142857
    ny = 2
    xcord = xcord/nx
    ycord = ycord/ny

final_cords = (round(xcord), round(ycord))

upper_left_corner = (50, 36)
upper_right_corner = (60, 36)
lower_left_corner = (50, 50)
lower_right_corner = (60, 50)

input_points = final_cords
print(input_points)
def check_cords(pt1, pt2, pt3, pt4, ptinp, num=[], num1=[], num2=[], num3=[], result=[]):
    x1, x2, x3, x4, xinp = pt1[0], pt2[0], pt3[0], pt4[0], ptinp[0]
    y1, y2, y3, y4, yinp = pt1[1], pt2[1], pt3[1], pt4[1], ptinp[1]
    
    minimum_x1 = min(x1, x2, x3, x4)
    minimum_y1 = min(y1, y2, y3, y4)

    maximum_x1 = max(x1, x2, x3, x4)
    maximum_y1 = max(y1, y2, y3, y4)
    
    for i in range(minimum_y1, maximum_y1 + 1):
        num.append(i)
    for n in range(minimum_x1, maximum_x1 + 1):
        num1.append(n)
    
    for i in num:
        # print("a")
        for n in num1:
            # print("b")
            cord = (n, i)
            if cord == input_points:
                result.append(True)
                print(True)

res = []
check_cords(upper_left_corner, lower_left_corner, upper_right_corner, lower_right_corner, input_points, result=res)

if res:
    try:
        if res[0] == True:
            print("good")
    except:
        print("false coordinate")
        pg.leftClick(xcord, ycord)
else:
    pg.leftClick(xcord, ycord)


time.sleep(2)

# import xml
def import_xml():
    pg.hotkey("command", "9")
    time.sleep(1)

    pg.click(325, 575)

    time.sleep(1)

    pg.click(1577, 311)

    pg.typewrite(f"{filename}.xml")

    time.sleep(1)

    pg.click(1548, 420)

    time.sleep(1)

    pg.press("enter")

    time.sleep(1)

    pg.press("enter")
    time.sleep(1)

# replace text (¥)
def id_replace():
    pg.hotkey('command', 'f')
    time.sleep(1)

    # select profile
    pg.click(1888, 303)

    pg.click(1890, 344)

    pg.click(2160, 528)
    time.sleep(1)

    pg.press("enter")
    time.sleep(1)

    pg.click(2200, 723)

    time.sleep(1)

# export file as pdf
def id_export_file():
    pg.hotkey("command", "e")
    time.sleep(1)

    # pg.click(1337, 204)

    time.sleep(0.5)
    # pg.click(1337, 204)
    # time.sleep(2)
    # pg.doubleClick(1337, 204)
    time.sleep(1)
    pg.typewrite(f"{filename}")
    time.sleep(1)

    pg.press("enter")
    time.sleep(1)
    pg.press("enter")


def start_auto():
    import_xml()

    id_replace()

    id_export_file()
