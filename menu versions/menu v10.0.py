import time
from xmlrpc.client import DateTime
import numpy as np
import re
from time import time, strftime, localtime
from datetime import timedelta
from datetime import date
import os.path
import subprocess
import time
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import *
from tkinter.ttk import *
import docx2txt
import pyautogui as pg
from PIL import Image

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


def if_same(in1, in2, arg):
    int(in1)
    int(in2)
    if in1 == in2:
        return True
    elif in1 != in2:
        raise ValueError(f"{arg} are false, value 1: {in1}, value 2: {in2}")


def findall_in_string(input, search_item, search_item2, list_num, list_txt):
    input = str(input)
    findall = re.findall(search_item, input)
    findall2 = re.findall(search_item2, input)

    num = len(findall) + len(findall2)

    txt = findall
    txt2 = findall2
    txt = ' '.join(str(e) for e in txt)
    txt2 = ' '.join(str(d) for d in txt2)
    txt = txt + txt2
    # print(txt)
    # print(num)
    list_num.append(num)
    list_txt.append(txt)

def listToString(s):
    str1 = " "
    return (str1.join(s))


def append_things(number1, number2, appendlist, origin):
    while number1 < number2:
        appendlist.append(origin[number1])
        number1 += 1
    return appendlist


def select_string(number1, number2, menuapp, jour):
    while number1 < number2:
        menuapp.append(jour[number1])
        number1 += 1
    return menuapp


def month_string_to_number(string):
    m = {
        'janv': "01",
        'févr': "02",
        'mars': "03",
        'avri': "04",
        'mai': "05",
        'juin': "06",
        'juil': "07",
        'août': "08",
        'sept': "09",
        'octo': "10",
        'nove': "11",
        'déce': "12"
    }
    s = string.strip()[:4].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError(f'Not a month, string: {string}')

def number_string_to_month(string):
    m = {
        "01": 'janvier',
        "02": "février",
        "03": "mars",
        "04": "avril",
        "05": "mai",
        "06": "juin",
        "07": "juillet",
        "08": "août",
        "09": "septembre",
        "10": "octobre",
        "11": "novembre",
        "12": "décembre"
    }

    try:
        out = m[string]
        return out
    except:
        raise ValueError(f'Not a month, string: {string}')

# time functions

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    line = "=" * 40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()


def get_year():
    todays_date = date.today()
    year = todays_date.year
    month = todays_date.month
    day = todays_date.day

    if month == 12 and day >= 13:
        year = year + 1
    return year

class Jour:
    def find_indexes(self, jour):
        return self.input.index(jour)

class Plats:

    # self.jour = jours input

    def find_plats(self, plat):
        return self.input.index(plat)

    def get_plats_index(self):
        platlow = self.plats["check_plats"]
        platupper = self.plats["platupper_org"]
        # subtitlelow = self.subtitle
        
        print("jour: ", self.jour)
        for x in platlow:
            print("x: ",x)
            print()
            if self.plats["plats_present"][self.plats["platlow_org"].index(x)] == False:
                pass
            else:
                try:
                    p = self.jour.index(x)
                except:
                    p = self.jour.index((self.plats["platupper_org"][self.plats["platlow_org"].index(x)]))

                self.plats_indexes.append(p)
        self.plats_indexes.append(len(self.jour))

        plats_lst = [self.plat1, self.plat2, self.plat3, self.plat4, self.plat5, self.plat6]
        
        print("plats indexes: ",self.plats_indexes)
        num1 = 1
        num2 = 0

        while num1 < len(self.plats_indexes):
            u = self.select_plats(self.plats_indexes[num2], self.plats_indexes[num1])
            for x in u:
                plats_lst[num2].append(x)
            print("num1: ",num1)
            print("num2: ",num2)
            num1 += 1
            num2 += 1


    def select_plats(self, index1, index2):
        c1 = []
        while index1 < index2:
            c1.append(self.jour[index1])
            index1 += 1
        return c1





            
class Menu_du_jour:
    # def __init__(self) -> None:
    #     self.input = input
    #     self.lundi = lundi
    #     self.mardi = mardi
    #     self.mercredi = mercredi
    #     self.jeudi = jeudi
    #     self.vendredi = vendredi
    #     self.days = days
    
    def check_input(self):
        # check the input for things present, system to map present things

        daylow = self.days["daylow_org"]
        dayupper = self.days["dayupper_org"]

        num1 = 0
        for x in self.days["original_days"]:
            if daylow[num1] not in self.input and dayupper[num1] not in self.input:
                print(f'Day {daylow[num1]} not included template wrong!')
                self.days["days_present"][num1] = False

            elif daylow[num1] in self.input or dayupper[num1] in self.input:
                print(f'Day {daylow[num1]} included')
                self.days["days_present"][num1] = True
            
            num1 += 1

        platlow = self.plats["platlow_org"]
        platupper = self.plats["platupper_org"]

        num1 = 0

        for x in self.plats["check_plats"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                print(f'plat {platlow[num1]} not included template wrong')
                self.plats["plats_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                print(f'plat {platlow[num1]} included')
                self.plats["plats_present"][num1] = True
            
            num1 += 1
        
        platlow = self.subtitle["subtitlelow_org"]
        platupper = self.subtitle["subtitleupper_org"]

        num1 = 0

        for x in self.subtitle["original_subtitles"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                print(f'subtitle {platlow[num1]} not included template wrong')
                self.subtitle["subtitle_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                print(f'plat {platlow[num1]} included')
                self.subtitle["subtitle_present"][num1] = True
            
            num1 += 1

        items_to_replace = ["potage du jour"]
        items_final_replace = ["Potage du jour"]

        num1 = 0
        for x in items_to_replace:
            self.input.find(x)
            self.input = self.input.replace(x, items_final_replace[num1])

            num1 += 1

    def wordsToList(self):
        L = self.input.split()
        cleanL = []
        abc1 = "abcdefghijklmnopqrstuvwxyzâôûéáœâàëöÿç"
        abc = "=:;«»’°|'ïäöüè/%+^¨&<>,.§ëöÿÏÖÜË('^)1234567890!-_" + abc1
        ABC = abc1.upper()
        letters = abc + ABC
        for e in L:
            word = ''
            for c in e:
                if c in letters:
                    word += c
            if word != '':
                cleanL.append(word)
        self.input = cleanL

    def split_days(self):
        j = Jour()
        j.input = self.input
        daylow = self.days["daylow_org"]
        dayupper = self.days["dayupper_org"]

        for x in daylow:
            if self.days["days_present"][self.days["daylow_org"].index(x)] == False:
                pass
            else:
                try:
                    p = j.find_indexes(x)
                except:
                    p = j.find_indexes(self.days["dayupper_org"][self.days["daylow_org"].index(x)])
                self.days_indexes.append(p)
        self.days_indexes.append(len(self.input))

        days_lst = [self.day1, self.day2, self.day3, self.day4, self.day5]
        # print(self.days_indexes)
        num1 = 1
        num2 = 0

        while num1 < len(self.days_indexes):
            u = self.select_days(self.days_indexes[num2], self.days_indexes[num1])
            for x in u:
                days_lst[num2].append(x)
            num1 += 1
            num2 += 1


    def select_days(self, index1, index2):
        c1 = []
        while index1 < index2:
            c1.append(self.input[index1])
            index1 += 1
        print()
        return c1

    def filter_plats(self): 
        daylow = self.days["daylow_org"]
        days_lst = [self.day1, self.day2, self.day3, self.day4, self.day5]
        for x in days_lst:
            print(x)
        num1 = 0
        for x in daylow:
            if self.days["days_present"][self.days["daylow_org"].index(x)] == False:
                pass
            else:
                p = Plats()
                p.plats = plats

                p.plat1 = []
                p.plat2 = []
                p.plat3 = []
                p.plat4 = []
                p.plat5 = []
                p.plat6 = []

                p.subtitle1 = []
                p.subtitle2 = []
                p.subtitle3 = []
                p.subtitle4 = []
                p.subtitle5 = []
                p.subtitle6 = []

                p.jour = days_lst[num1]
                p.plats_indexes = []

                p.get_plats_index()

                plats_lst = [p.plat1, p.plat2, p.plat3, p.plat4, p.plat5, p.plat6]
                subtitles_lst = [p.subtitle1,  p.subtitle2, p.subtitle3, p.subtitle4, p.subtitle5, p.subtitle6]

                # num1a = 1
                # num2a = 0
                # while num1a < len(p.plats_indexes):

                #     u = p.select_plats(p.plats_indexes[num2a], p.plats_indexes[num1a])
                #     for x in u:
                #         plats_lst[num2a].append(x)
                #     num1a += 1
                #     num2a += 1
                # num1 += 1


                print("plat1: ", p.plat1)
                print("plat2: ", p.plat2)
                print("plat3: ", p.plat3)
                print("plat4: ", p.plat4)
                print("plat5: ", p.plat5)
                print("plat6: ", p.plat6)

days = {
    "original_days":['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "check_days":['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "daylow_org":['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "dayupper_org":['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'],
    "days_present":['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
}
plats = {
    "original_plats":['potage', 'plat1', 'plat2', 'accompagnement', 'légumes', 'dessert'],
    "check_plats":['potage_', 'plat_1', 'plat_2', 'accompagnement', 'légumes_', 'dessert_'],
    "platlow_org":['potage_', 'plat_1', 'plat_2', 'accompagnement', 'légumes_', 'dessert_'],
    "platupper_org":['Potage_', 'Plat_1', 'Plat_2', 'Accompagnement', 'Légumes_', 'Dessert_'],
    "plats_present":['potage', 'plat1', 'plat2', 'accompagnement', 'légumes', 'dessert']
}
subtitle = {
    'original_subtitles':['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement', 'subtitle_légumes', 'subtitle_dessert'],
    'check_subtitle':['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement', 'subtitle_légumes', 'subtitle_dessert'],
    'subtitlelow_org':['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement', 'subtitle_légumes', 'subtitle_dessert'],
    'subtitleupper_org':['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement', 'subtitle_légumes', 'subtitle_dessert'],
    'subtitle_present':['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement', 'subtitle_légumes', 'subtitle_dessert'],

}

m = Menu_du_jour()
m.days = days
m.plats = plats
m.subtitle = subtitle
m.days_indexes = []

m.day1 = []
m.day2 = []
m.day3 = []
m.day4 = []
m.day5 = []

inp = """
Lundi DATE MOIS asasks s dsd
potage_
potage du jour
subtitle_potage	 
plat_1	 
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Mardi DATE MOIS	a
potage_	 
subtitle_potage	 
plat_1	 a
subtitle_plat1	 
plat_2	 a
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 aa
subtitle_légumes	 a
dessert_	 
subtitle_dessert	 

Mercredi DATE MOIS	
potage_	 ff
subtitle_potage	 f
plat_1	 f
subtitle_plat1	 f
plat_2	 g
subtitle_plat2	 g
accompagnement	 h
subtitle_accompagnement	 hj
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Jeudi DATE MOIS	
potage_	 s
subtitle_potage	 
plat_1	 s
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 d
dessert_	 
subtitle_dessert	 

Vendredi DATE MOIS	
potage_	 sk
subtitle_potage	 
plat_1	
subtitle_plat1	 j
plat_2	 f
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

"""

inp = """

Lundi DATE MOIS	
potage_	 Potage du jour 1
subtitle_potage	 
plat_1	 Plat1 1
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Mardi DATE MOIS	
potage_	 Potage du jour 2
subtitle_potage	 
plat_1	 Plat1 2
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Mercredi DATE MOIS	
potage_	 Potage du jour 3
subtitle_potage	 
plat_1	 Plat1 3
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Jeudi DATE MOIS	
potage_	 Potage du jour 4
subtitle_potage	 
plat_1	 Plat1 4
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 

Vendredi DATE MOIS	
potage_	 Potage du jour 5
subtitle_potage	 
plat_1	Plat1 5
subtitle_plat1	 
plat_2	 
subtitle_plat2	 
accompagnement	 
subtitle_accompagnement	 
légumes_	 
subtitle_légumes	 
dessert_	 
subtitle_dessert	 


"""

m.input = inp

m.check_input()

m.wordsToList()
m.split_days()

m.filter_plats()