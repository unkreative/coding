from tkinter import Image
from PIL import Image, ImageDraw
import numpy as np
import pyautogui as pg

# screenshot_path = "/Users/lousergonne/Desktop/Screenshot tst.png"
screenshot_path = "/Users/NLNEW/Desktop/amen.png"
pg.screenshot(screenshot_path)

# im = Image.open(screenshot_path).convert('RGB')
# im = im.resize((2560, 1600))
# im.save(screenshot_path)
print("step 1")

with Image.open(screenshot_path).convert('RGB') as pim:
    pim.resize((2559, 1439))
    pim.save(screenshot_path)

with Image.open(screenshot_path).convert('RGB') as pim:
    print(pim.getdata)
    print(pim.getpixel)
    print("step 2")

    im = np.array(pim)
    
    green = [97,196,84]
    green = [63, 197, 73]

    Y,X = np.where(np.all(im==green, axis=2))
    print(X, Y)

    draw = ImageDraw.Draw(pim)

    num1 = 1
    while num1 < len(X):
        xx = X[num1]
        yy = Y[num1]
        cord1 = (xx, yy)
        cord2a = xx*144
        cord2b = yy*144

        mac = 226.98
        imac = 218
        cord2a = cord2a/imac
        cord2b = cord2b/imac
        cord2 = (cord2b, cord2a)

        n1x = 2.018181818181818
        n1y = 2
        n2x = 1.982142857142857
        n2y = 2
        cord3a = xx/n1x
        cord3b = yy/n1y
        cord4a = xx/n2x
        cord4b = yy/n2y
        
        cord3 = (cord3a, cord3b)
        cord4 = (cord4a, cord4b)

        draw.point(cord1, fill="blue")
        draw.point(cord2, fill="red")
        draw.point(cord3, fill="orange")
        draw.point(cord4, fill="green")
        
        
        num1 += 1
    # pg.leftClick(cord2a, cord2b)
    pg.leftClick(cord4a, cord4b)


    print("x: ", xx, "y: ", yy)
    print("x: ", cord2a, "y: ", cord2b)
    pim.show()


n1x = 2.018181818181818
n1y = 2
n2x = 1.982142857142857
n2y = 2
