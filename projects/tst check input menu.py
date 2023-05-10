from pickle import TRUE
import subprocess
import time
import tkinter as tk
from tkinter import filedialog, ttk
import re
import docx2txt

menu2 = """
Lundi 17 janvier

potag3
Potage du jour
subtitle_potage

plat1 
Ragoût de jeune bovin aux carottes 
Subtitle_plat1
Biohaff Baltes Stegen
plat2 
Subtitle_plat2
Ragoût de tofu fumé aux carottes
accompagnement 
Boulgour
Subtitle_accompagnement

dessert  
Gâteau aux noix
Subtitle_dessert


Mardi 18 janvier 
potag3
Potage du jour
subtitle_potage

plat1 
Chili con carne 
Subtitle_plat1

plat2 
Chili sin carne
Subtitle_plat2

accompagnement 
Riz de Camargue 
Subtitle_accompagnement

dessert 
Fruits  
Subtitle_dessert

Mercredi  19 janvier 

potag3
Potage du jour 
subtitle_potage

plat1 
Pâtes aux brocolis rôtis, pois chiches et citron
Subtitle_plat1

plat2 
Pâtes, champignons, ricotta et pignons de pin
Subtitle_plat2
Champignons de Glabech (Nommern)
Ricotta de Fromagerie luxembourgeoise
dessert 
Tiramisu à l’orange
Subtitle_dessert
Jeudi 20 janvier 

potag3
Potage du jour 
subtitle_potage

plat1 
Bifanas de porc 
Subtitle_plat1
plat2 
Galette de betteraves et quinoa 
Subtitle_plat2
accompagnement 
Pommes de terre
Subtitle_accompagnement
Légumes 
Chou blanc 
Subtitle_légumes
dessert 
Fruits 
Subtitle_dessert

Vendredi 21 janvier 

potag3
Potage du jour 
subtitle_potage
plat1 
Cassoulet de poisson 
Subtitle_plat1
plat2 
Cassoulet végétarien
Subtitle_plat2
haricots lingots, tomates et oignons
accompagnement 
Polenta 
Subtitle_accompagnement
dessert 
Feuilletée aux pommes 
Subtitle_dessert
"""
def if_same(inp1, inp2):
    print("input1 :", inp1)
    print("input2 :", inp2)
    if inp1 - inp2 == 0:
        return True
    else:
        return False

def correct_lundi(input1, input2, input3, input4, arg):

    if arg == 1:
        len1 = len(input1)
        for x in range(len1, 0):
            input1.pop(x)

        return input1
    elif arg == 2:
        calc = input2[0] / 4
        input2[0] = int(calc)

        return input2

    elif arg == 3:
        len3 = len(input3)
        for y in range(len3, 0):
            input3.pop(y)

        return input3
    elif arg == 4:
        return input4
    

def findall(num, input, list1, list2, argument_day, search_item1, search_item2):

    if argument_day == "lundi":
        num_down = []
        num_up = re.findall(search_item1[0], input)
        
    else:
        num_up = re.findall(search_item1[num], input)
        num_down = re.findall(search_item2[num], input)

    list1.append(len(num_down) + len(num_up))
    print("aaab", list1)
    list2.append(num_up + num_down)
    print("aaab", list2)
    

def check_input3(input):
    num1 = 1
    num2 = 0

    plats_down = ["potag3", "plat1 ", "plat2 ", "accompagnement ", "Légumes ", "dessert "]
    plats_up = ["potag3", "Plat1 ", "Plat2 ", "Accompagnement ", "Légumes ", "Dessert "]

    sub_down = ["subtitle_potage", "subtitle_plat1", "subtitle_plat2", "subtitle_accompagnement", "subtitle_légumes", "subtitle_dessert"]
    sub_up = ["Subtitle_potage", "Subtitle_plat1", "Subtitle_plat2", "Subtitle_accompagnement", "Subtitle_légumes", "Subtitle_dessert"]
    lst1 = []
    lst2 = []
    lst11 = []
    lst22 = []
    results = []
    # plats
    findall(0, input, lst1, lst2, "lundi", plats_down, plats_up)
    findall(1, input, lst1, lst2, "", plats_down, plats_up)
    findall(2, input, lst1, lst2, "", plats_down, plats_up)
    findall(3, input, lst1, lst2, "", plats_down, plats_up)
    findall(4, input, lst1, lst2, "", plats_down, plats_up)
    # subtitles
    findall(0, input, lst11, lst22, "lundi", sub_up, sub_down)
    findall(1, input, lst11, lst22, "", sub_up, sub_down)
    findall(2, input, lst11, lst22, "", sub_up, sub_down)
    findall(3, input, lst11, lst22, "", sub_up, sub_down)
    findall(4, input, lst11, lst22, "", sub_up, sub_down)


    # while num2 < 1:
    #     num_lundi = re.findall(plats_down[num2], input)
    #     num_len_lundi = len(num_lundi)
    #     lst1.append(num_lundi)
    #     lst11.append(num_len_lundi)
    #     num2 += 1
        
        
    # while num1 < 5:
    #     num_down = re.findall(plats_down[num1], input)
    #     num_up = re.findall(plats_up[num1], input)

    #     num_down_ = len(num_down)
    #     num_up_ = len(num_up)

    #     num_app1 = num_down + num_up
    #     num_app2 = num_down_ + num_up_
    #     print(num_app1)
    #     lst1.append(num_app1)
    #     lst11.append(num_app2)
    #     num1 += 1
    #     # print(lst1)
    #     # print(lst11)
    
    # num3 = 6
    # num4 = 0

    # while num4 < num3:
    #     num2_down = re.findall(sub_down[num4], input)
    #     num2_up = re.findall(sub_up[num4], input)

    #     num2_down_ = len(num2_down)
    #     num2_up_ = len(num2_up)

    #     num_app11 = num2_down + num2_up
    #     print(num_app11)
    #     num_app22 = num2_down_ + num2_up_
    
    #     lst2.append(num_app11)
    #     lst22.append(num_app22)
    #     # print(lst2)
    #     # print(lst22)
    #     num4 += 1

    num5 = 0
    print(lst11, " aaa", lst11, lst2, lst22)

    while num5 < 6:
        print("num5: ", num5)
        print("lst11: ", lst11, "len list: ", len(lst11))
        print("lst22: ", lst22, "len list: ", len(lst22))
        res = if_same(lst11[num5], lst22[num5])
        print(res)
        results.append(res)
        print(num5)
        num5 += 1
    
    num6 = 0
    while num6 <= 6:
        if results[num6] == True:
            pass
        else:
            raise ValueError(f"plat number {num6} isnt correct")
        num6 += 1

    return "l"

menu = check_input3(menu2)
print(menu)