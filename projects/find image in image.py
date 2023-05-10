from multiprocessing.spawn import import_main_path
from time import time
import cv2
import pyautogui as pg
import PIL
import time
def find_image(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(small_image)
    large_image = cv2.imread(large_image)

    result = cv2.matchTemplate(small_image, large_image, method)
    print(result)
    # We want the  minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc
    print(mnLoc)
    pg.click(mnLoc[0], mnLoc[1])
    # Step 2: Get the size of the template. This is the same size as the match.
    # trows,tcols = small_image.shape[:2]

    # # Step 3: Draw the rectangle on large_image
    # cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # # Display the original image with the rectangle around the match.
    # cv2.imshow('output',large_image)

    # # The image is only displayed if we call this
    # cv2.waitKey(0)


time.sleep(2)

pg.click(235, 164)

time.sleep(1)

pg.click(325, 575)

time.sleep(1)

pg.click(1577, 311)

pg.typewrite("220102")

time.sleep(1)

pg.click(1548, 420)

time.sleep(1)

pg.press("enter")

time.sleep(1)

pg.press("enter")
time.sleep(1)

pg.hotkey('command', 'f')
time.sleep(1)

pg.click(2140, 550)
time.sleep(1)

pg.press("enter")
time.sleep(1)

pg.click(2160, 750)

time.sleep(1)

pg.hotkey("command", "e")
time.sleep(1)

pg.typewrite("220102.jpg")
time.sleep(1)

pg.press("enter")
