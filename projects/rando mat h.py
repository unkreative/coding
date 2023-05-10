import time
import pyautogui as pg
import subprocess

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

p = [8, 10, 32, 42, 54, 82, 90, 98, 99, 100]

num1 = 1
time.sleep(3)
while num1 <= 100:
    if num1 in p:
        num1 += 1
    if num1 in p:
        num1 += 1
    if num1 in p:
        num1 += 1
    
    # for x in p:
    #     print("a")
    #     if num1 == p[x]:
    #         num1 += 1
    pg.press("enter")
    print("penis")

    link = f"""https://bordboeken.averbode.be/CMS/CDS/Averbode/Published%20Content/Auteurs/Auteur_Franstalig/Amplitude/Tome%203/Amplitude%203%20-%20R%C3%A9f%C3%A9rentiel/Resources/Amplitude3_Referentiel.pdf_/{num1}.png"""
    print(link)
    pg.hotkey("command", "l")
    time.sleep(0.5)
    pg.hotkey("delete")
    time.sleep(0.5)
    write_to_clipboard(link)
    pg.hotkey("command", "v")
    time.sleep(1)
    pg.hotkey("enter")
    time.sleep(1)
    pg.hotkey("command", "s")
    time.sleep(1)
    pg.hotkey("shift", "7")
    time.sleep(0.5)
    path = '/Users/lousergonne/Desktop/mathebuch'

    write_to_clipboard(link)

    pg.hotkey("command", "v")
    time.sleep(0.5)
    pg.hotkey("enter")
    time.sleep(1)
    # pg.typewrite(f"{num1}.png")
    
    time.sleep(0.5)
    pg.hotkey("enter")
    pg.click(430, 400)
    pg.click(430, 400)
    pg.click(430, 400)
    pg.click(430, 400)
    time.sleep(1)
    pg.hotkey("esc")


    num1 += 1