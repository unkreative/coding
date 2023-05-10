
from signal import pthread_kill
from tkinter import Image
from PIL import Image, ImageDraw
import numpy as np

upper_left_corner = (50, 36)
upper_right_corner = (60, 36)
lower_left_corner = (50, 50)
lower_right_corner = (60, 50)
input_points = (50, 50)
ymax1 = 50
ymin1 = 36
xmax1 = 60
xmin1 = 50
print("a")
screenshot_path = '/Users/NLNEW/Desktop/Screenshot 2022-03-15 at 12.20.37.png'

screenshot_path = '/Users/NLNEW/Desktop/Screenshot 2022-03-15 at 12.15.22.png'
        

# for i in range(upper_left_corner[1], upper_left_corner[0]):
#     print(i)

def on_line(pt1, pt2, pt3, results):

    x1, x2, x3 = pt1[0], pt2[0], pt3[0]

    y1, y2, y3 = pt1[1], pt2[1], pt3[1]

    slope = (y2 - y1) / (x2 - x1)
    print(slope)

    pt3_on = (y3 - y1) == slope * (x3 - x1)


    pt3_between = (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))
    on_and_between = pt3_on and pt3_between

    print(on_and_between)


def on_line2(pt1=(50, 36), pt2=(60, 36), pt3=(55, 36)):
    x1, x2, x3 = pt1[0], pt2[0], pt3[0]

    y1, y2, y3 = pt1[1], pt2[1], pt3[1]
    check1 = []
    min1x = min(x1, x2)
    max1x = max(x1, x2)

    min1y = min(y1, y2)
    max1y = max(y1, y2)

    slope = (y2 - y1) / (x2 - x1)

    if (y3 - y1) == slope * (x3 - x1):
        print("TRUE 1")
        check1.append(True)
    else:
        check1.append(False)

    if min1x <= x3 <= max1x and min1y <= y3 <= max1y:
        print("TRUE 2")
        check1.append(True)
    else:
        print(False)
        check1.append(False)
    
    print(check1)
    return check1

def check_cords(pt1, pt2, pt3, pt4, ptinp, num=[], num1=[], num2=[], num3=[]):
    x1, x2, x3, x4, xinp = pt1[0], pt2[0], pt3[0], pt4[0], ptinp[0]
    y1, y2, y3, y4, yinp = pt1[1], pt2[1], pt3[1], pt4[1], ptinp[1]
    
    minimum_x1 = min(x1, x2, x3, x4)
    minimum_y1 = min(y1, y2, y3, y4)

    maximum_x1 = max(x1, x2, x3, x4)
    maximum_y1 = max(y1, y2, y3, y4)
    

    print(minimum_x1)
    print(minimum_y1)
    print(maximum_x1)
    print(maximum_y1)


    for i in range(minimum_y1, maximum_y1 + 1):
        print(i)
        num.append(i)
    for n in range(minimum_x1, maximum_x1 + 1):
        print(n)
        num1.append(n)

    print(num)
    print(num1)
    
    for i in num:
        for n in num1:
            cord = (i, n)
            if cord == input_points:
                print(True)

check_cords(upper_left_corner, lower_left_corner, upper_right_corner, lower_right_corner, input_points)
# print(num1)
# print(num2)

# print("A")
# with Image.open(screenshot_path).convert('RGB') as pim:
#     draw = ImageDraw.Draw(pim)
#     print("A")

#     for i in num1:
#         print("A")
#         for n in num2:
#             cord1 = (i, n)
#             print(cord1)

#             draw.point(cord1, fill="blue")
#     pim.show()
        