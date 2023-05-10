import os.path
import re
import subprocess
import time
import tkinter as tk
from datetime import date
from datetime import timedelta
import math
# from time import sleep
# from time import *             #meaning from time import EVERYTHING
# import time
# from time import time, strftime, localtime
# from tkinter import *

from tkinterdnd2 import *
from tkinter import filedialog, ttk
from tkinter.ttk import *
from datetime import datetime
import tkinter


import docx2txt
# import numpy as np
import pyautogui as pg
import sv_ttk


# TODO: internat date DONE
# TODO: move mouse to center when automation, fixes some things i think DONE
# TODO: test everything together
# TODO: test official
# TODO: replace some things (for now) DONE (temporary )

# new internat things
now = datetime.now()
now_internat = now.strftime("%a%y")
filepath_internat = f"/Users/lousergonne/coding/{now_internat}.txt"


    # xml_internat = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <internats_menu>
# <date>{date}</date>
# <Lundi>
# <title>{day1}</title><plat>{plat1}</plat></Lundi>

# <Mardi><title>{day2}</title><plat>{plat2}</plat></Mardi>

# <Mercredi><title>{day3}</title><plat>{plat3}</plat></Mercredi>

# <Jeudi><title>{day4}</title><plat>{plat4}</plat></Jeudi></internats_menu>
# """

def move_mouse():
    screen_size = pg.size()
    x = screen_size[0]/2
    y = screen_size[1]/2
    pg.moveTo(x,y)


def replace(input: str):
    inputt = input
    replace = [["potage du", "Potage du"], ["plat 1", "plat_1"],
               ["Plat 1", "plat_1"], ["plat 2", "plat_2"], ["Plat 2", "plat_2"], ["Légumes", "légumes_"],
               ["\ndessert", "dessert_"], ["Dessert", "dessert_"]]

    for x in replace:
        try:
            input = input.replace(x[0], x[1])
        except:
            pass
    # print(input)
    return inputt


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
        try:
            # number_string_to_month(string)
            pass
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
        return datetime.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    line = "=" * 40
    print(line)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    # print()


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

    def update_presence_day(self, thing, jour, date=""):
        value = 0
        for item in thing:
            cachee = re.findall("<plat></plat>", item)
            value += len(cachee)

        if value == 6:
            try:
                self.jour_lst["days_present"][self.jour_lst["original_days"].index(jour)] = False
            except:
                self.jour_lst["days_present"][self.jour_lst["dayupper_org"].index(jour)] = False

        if len(re.findall("        <date>Vendredi potage_ subtitle_potage 2022</date>", date)) > 0:
            try:
                self.jour_lst["days_present"][self.jour_lst["original_days"].index(jour)] = False
            except:
                self.jour_lst["days_present"][self.jour_lst["dayupper_org"].index(jour)] = False

    def get_plats_index(self):
        # print(self.jour)
        plat_check = self.plats["check_plats"]
        subtitles_check = self.subtitle["check_subtitle"]
        check = ['potage_', 'subtitle_potage', 'plat_1', 'subtitle_plat1', 'plat_2', 'subtitle_plat2', 'accompagnement',
                 'subtitle_accompagnement', 'légumes_', 'subtitle_légumes', 'dessert_', 'subtitle_dessert', "Internat"]

        numc = 0

        for x in check:
            if (numc % 2) == 0:
                if self.plats["plats_present"][self.plats["platlow_org"].index(x)] == False:
                    pass
                else:
                    try:
                        p = self.jour.index(x)
                    except:
                        p = self.jour.index(self.plats["platupper_org"][self.plats["platlow_org"].index(x)])

                    self.plats_indexes.append(p)
            else:
                if self.subtitle['subtitle_present'][self.subtitle['subtitlelow_org'].index(x)] == False:
                    pass
                else:
                    try:
                        p = self.jour.index(x)
                    except:
                        p = self.jour.index(
                            self.subtitle["subtitleupper_org"][self.subtitle["subtitlelow_org"].index(x)])

                    self.plats_indexes.append(p)

            numc += 1

        self.plats_indexes.append(len(self.jour))

        plats_lst = [self.plat1, self.subtitle1, self.plat2, self.subtitle2, self.plat3, self.subtitle3, self.plat4,
                     self.subtitle4, self.plat5, self.subtitle5, self.plat6, self.subtitle6, self.subtitle7]

        num1 = 1
        num2 = 0

        while num1 < len(self.plats_indexes):
            u = self.select_plats(self.plats_indexes[num2], self.plats_indexes[num1])
            for x in u:
                plats_lst[num2].append(x)

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

        # CHANGE MENU DATE

        if "." in self.input:
            nums_month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
            months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
            nums_day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
            for month in nums_month:
                # print(month)
                for day in nums_day:
                    toreplace = f"{day}.{month}."
                    replace_w = f"{day} {months[nums_month.index(month)]}"
                    self.input = self.input.replace(toreplace, replace_w)
                    # print(toreplace)
                    # print(replace_w)
        
                    toreplace = f"{day}.{month}"
                    replace_w = f"{day} {months[nums_month.index(month)]}"
                    self.input = self.input.replace(toreplace, replace_w)
                    # print(toreplace)
                    # print(replace_w)
                
                    # print(replace_w)
            
        # isnumeric()
        # remove days

        daylow = self.days["daylow_org"]
        dayupper = self.days["dayupper_org"]

        num1 = 0
        for x in self.days["original_days"]:
            if daylow[num1] not in self.input and dayupper[num1] not in self.input:
                # # print(f'Day {daylow[num1]} not included template wrong!')
                self.days["days_present"][num1] = False

            elif daylow[num1] in self.input or dayupper[num1] in self.input:
                # # print(f'Day {daylow[num1]} included')
                self.days["days_present"][num1] = True

            num1 += 1

        platlow = self.plats["platlow_org"]
        platupper = self.plats["platupper_org"]

        num1 = 0

        for x in self.plats["check_plats"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                # # print(f'plat {platlow[num1]} not included template wrong')
                self.plats["plats_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                # # print(f'plat {platlow[num1]} included')
                self.plats["plats_present"][num1] = True

            num1 += 1

        platlow = self.subtitle["subtitlelow_org"]
        platupper = self.subtitle["subtitleupper_org"]

        num1 = 0

        for x in self.subtitle["original_subtitles"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                # # print(f'subtitle {platlow[num1]} not included template wrong')
                self.subtitle["subtitle_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                # # print(f'plat {platlow[num1]} included')
                self.subtitle["subtitle_present"][num1] = True

            num1 += 1
        self.input = self.input + " Internat"

    def wordsToList(self):
        L = self.input.split()
        cleanL = []
        abc1 = "abcdefghijklmnopqrstuvwxyzâôûéáœâàëöÿçêâûîô"
        abc = "=:;«»’°|'ïäöüè/%+^¨&<>,..§ëöÿÏÖÜË('^)123456789¥0!-_" + abc1
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

        # self.input, it = remove_internat(
        # self.input, self.days_indexes)
        # # print(it)
        days_lst = [self.day1, self.day2, self.day3, self.day4, self.day5]
        num1 = 1
        num2 = 0

        while num1 < len(self.days_indexes):
            # print(f"{self.days_indexes}")
            # print()
            # print(len(self.input))
            # print(self.input[0])
            # print(self.input[1])
            # print(self.input[2])
            # print(self.input[3])
            # print(self.input[4])
            # print(self.input[5])
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
        return c1

    def filter_plats(self):
        daylow = self.days["daylow_org"]
        days_lst = [self.day1, self.day2, self.day3, self.day4, self.day5]
        num1 = 0
        for x in daylow:

            if self.days["days_present"][self.days["daylow_org"].index(x)] == False:
                pass
            else:
                p = Plats()
                p.plats = plats
                p.subtitle = subtitle
                p.jour_lst = self.days

                p.plat1 = []
                p.plat2 = []
                p.plat3 = []
                p.plat4 = []
                p.plat5 = []
                p.plat6 = []
                p.plat7 = []

                p.subtitle1 = []
                p.subtitle2 = []
                p.subtitle3 = []
                p.subtitle4 = []
                p.subtitle5 = []
                p.subtitle6 = []
                p.subtitle7 = []

                p.jour = days_lst[num1]
                p.plats_indexes = []

                p.get_plats_index()
                self.days = p.jour_lst
                p.plat7 = p.subtitle7
                p.subtitle7 = []

                plats_lst = [p.plat1, p.plat2, p.plat3, p.plat4, p.plat5, p.plat6, p.plat7]
                subtitles_lst = [p.subtitle1, p.subtitle2, p.subtitle3, p.subtitle4, p.subtitle5, p.subtitle6, p.subtitle7]
                num2 = 0
                xmlday = []
                xmlday.append(f"""    <{days_lst[num1][0]}>""")
                date = f"\n        <date>{p.jour[0]} {p.jour[1]} {p.jour[2]} {get_year()}</date>\n"
                self.days = p.jour_lst

                if self.days["days_present"][num1] == False:
                    pass
                else:
                    xmlday.append(date)
                    for x in plats_lst:
                        if x:
                            cache_title = x[0]
                            x.pop(0)
                            cache_plat = []

                            for x1 in x:
                                cache_plat.append(x1)

                            cache_plat = ' '.join([str(item) for item in cache_plat])
                            subtitle_cache = subtitles_lst[num2]
                            try:
                                subtitle_cache.pop(0)
                            except:
                                subtitle_cache = ""

                            subtitle_cache = ' '.join([str(item) for item in subtitle_cache])

                            module1 = f"""
        <slot{self.txt_placeholder}>
            <title>{cache_title}</title>
            <plat>{cache_plat}</plat>  
            <undertitle>{subtitle_cache}</undertitle>
        </slot{self.txt_placeholder}>\n"""
                            xmlday.append(module1)

                            num2 += 1
                xmlday.append(f"""    </{days_lst[num1][0]}>\n""")
                p.update_presence_day(xmlday, days_lst[num1][0], date)

                self.xml.append(xmlday)
                print()
                print()
                print(days_lst[num1][0])
                print()
                print("plat1: ", p.plat1)
                print("plat2: ", p.plat2)
                print("plat3: ", p.plat3)
                print("plat4: ", p.plat4)
                print("plat5: ", p.plat5)
                print("plat6: ", p.plat6)
                print("plat6: ", p.plat7)

                print("subitle1: ", p.subtitle1)
                print("subitle2: ", p.subtitle2)
                print("subitle3: ", p.subtitle3)
                print("subitle4: ", p.subtitle4)
                print("subitle5: ", p.subtitle5)
                print("subitle6: ", p.subtitle6)
                print("subitle6: ", p.subtitle7)

            num1 += 1


    def get_filename(self):
        first_day = ""
        to_ind = ""
        # print(self.days["days_present"])
        if self.days["days_present"][0] == True:
            first_day = self.day1
            to_ind = "Lundi"
        elif self.days["days_present"][1] == True:
            first_day = self.day2
            to_ind = "Mardi"
        elif self.days["days_present"][2] == True:
            first_day = self.day3
            to_ind = "Mercredi"
        elif self.days["days_present"][3] == True:
            first_day = self.day4
            to_ind = "Jeudi"
        elif self.days["days_present"][4] == True:
            first_day = self.day5
            to_ind = "Vendredi"

        index_dates1 = first_day.index(to_ind)
        index_dates2 = first_day.index("potage_")

        datee = []
        while index_dates1 < index_dates2:
            datee.append(first_day[index_dates1])
            index_dates1 += 1

        print(datee)
        month = datee[-1]
        month = month_string_to_number(month)
        print(month)

        day_num = datee[-2]
        print(day_num)
        if len(day_num) < 2:
            day_num = "0" + day_num
        now = datetime.now()
        year = now.strftime("%y")
        # print(type(year))
        log(year)
        filename = str(year) + str(month) + str(day_num)
        log(filename)
        self.filename.append(filename)

    def write_xml(self):
        xml_content = self.xml

        f = open(f"/Users/lousergonne/coding/{self.filename[0]}.xml", "a")
        config = """<?xml version="1.0" encoding="UTF-8"?>\n"""
        menu_inst = """<menu>\n"""
        menu_out = """</menu>\n"""

        f.write(config)
        f.write(menu_inst)

        for x in self.xml:
            check_day = re.search("<(.*)>", x[0])
            check_day = check_day.group(1)

            if self.days["days_present"][self.days["dayupper_org"].index(check_day)] == True:
                try:
                    if x:
                        num1 = 0
                        for x1 in x:
                            if """<plat></plat>""" in x1:
                                # print("empty slot found")
                                pass
                            else:

                                x2 = x1.replace(self.txt_placeholder, str(num1))
                                f.write(x2)
                                try:
                                    findall = re.findall(self.txt_placeholder, x1)
                                    if len(findall) > 0:
                                        num1 += 1
                                except:
                                    pass
                except:
                    # print("error while writing xml")
                    pass

        f.write(menu_out)

        f.close()

   
    def change_xml(self):

        with open(f'/Users/lousergonne/coding/{self.filename[0]}.xml', 'r') as file:
            filedata = file.read()

            # Replace the target string

        for thing in self.replace_in_xml:
            filedata = filedata.replace(thing[0], thing[1])

            # Write the file out again
        with open(f'/Users/lousergonne/coding/{self.filename[0]}.xml', 'w') as file:
            file.write(filedata)

  
    def automate(self):
        def import_xml():
            pg.hotkey("command", "9")
            time.sleep(2)

            # pg.click(1577, 311)
            pg.hotkey("shift", "7")

            time.sleep(2)
            pg.press("backspace")
            time.sleep(2)

            # print("filenameee ", self.filename)
            write_to_clipboard(f"/Users/lousergonne/coding/{self.filename[0]}.xml")
            pg.hotkey("command", "v")

            time.sleep(2)
            pg.press("enter")
            # pg.click(1548, 420)
            time.sleep(2)

            pg.press("enter")
            time.sleep(2)

            pg.press("enter")
            time.sleep(2)

        def indesign_replace():
            # pg.hotkey('command', 'f')
            # time.sleep(2)

            # # select profile
            # pg.click(1888, 303)

            # pg.click(1890, 344)

            # pg.click(2160, 528)
            # time.sleep(2)

            # pg.press("enter")
            # time.sleep(2)

            # pg.click(2200, 723)

            # time.sleep(2)
            pass
        def indesign_export_file():
            pg.hotkey("command", "e")
            time.sleep(2)

            pg.hotkey("shift", "7")
            time.sleep(1)

            write_to_clipboard(self.final_dir_pdf)
            time.sleep(0.5)

            pg.hotkey("command", "v")
            time.sleep(1)

            pg.press("enter")
            time.sleep(1)

            pg.press("enter")
            time.sleep(1)

            pg.press("enter")
            time.sleep(0.5)

        def check_all_pages():
            num1 = 0
            num2 = 1
            while num1 < 5:
                if self.days["days_present"][num1] == False:
                    pg.hotkey("command", "shift", "8")
                    time.sleep(1)
                    pg.press("backspace")
                    time.sleep(1)
                    pg.typewrite(f"{num2}")
                    time.sleep(1)
                    pg.press("enter")
                num1 += 1
                num2 += 1

        def save_indesign_file():
            time.sleep(1)

            pg.hotkey("command", "s")
            time.sleep(2)

            pg.hotkey("shift", "7")
            time.sleep(1)

            write_to_clipboard(self.final_dir_id)
            time.sleep(0.5)

            pg.hotkey("command", "v")
            time.sleep(1)

            pg.press("enter")
            time.sleep(0.5)

            pg.press("enter")
            time.sleep(1)

        time.sleep(2)
        # open indesign file
        subprocess.call(('open', self.indesign_file))
        time.sleep(10)

        pg.click()
        
        # set directories 
        self.final_dir_pdf = f'{self.menu_folder_path}/{self.filename[0]} menu.pdf'
        self.final_dir_id = f'{self.menu_folder_path}/{self.filename[0]} menu indesign'

        # import the xml
        import_xml()

        # replace ¥ with withespace
        indesign_replace()

        # check and delete all non existance pages
        check_all_pages()

        # export as idd file and pdf to folder

        indesign_export_file()
        save_indesign_file()



days = {
    "original_days": ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "check_days": ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "daylow_org": ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'],
    "dayupper_org": ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'],
    "days_present": ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
}
plats = {
    "original_plats": ['potage', 'plat1', 'plat2', 'accompagnement', 'légumes', 'dessert', "Internat"],
    "check_plats": ['potage_', 'plat_1', 'plat_2', 'accompagnement', 'légumes_', 'dessert_', "Internat"],
    "platlow_org": ['potage_', 'plat_1', 'plat_2', 'accompagnement', 'légumes_', 'dessert_', "Internat"],
    "platupper_org": ['Potage_', 'Plat_1', 'Plat_2', 'Accompagnement', 'Légumes_', 'Dessert_', "Internat"],
    "plats_present": ['potage', 'plat1', 'plat2', 'accompagnement', 'légumes', 'dessert', "Internat"]
}
subtitle = {
    'original_subtitles': ['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement',
                           'subtitle_légumes', 'subtitle_dessert'],
    'check_subtitle': ['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement',
                       'subtitle_légumes', 'subtitle_dessert'],
    'subtitlelow_org': ['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement',
                        'subtitle_légumes', 'subtitle_dessert'],
    'subtitleupper_org': ['Subtitle_potage', 'Subtitle_plat1', 'Subtitle_plat2', 'Subtitle_accompagnement',
                          'Subtitle_légumes', 'Subtitle_dessert'],
    'subtitle_present': ['subtitle_potage', 'subtitle_plat1', 'subtitle_plat2', 'subtitle_accompagnement',
                         'subtitle_légumes', 'subtitle_dessert'],
}



def main():
    menu = Menu_du_jour()

    menu.days = days
    menu.plats = plats
    menu.subtitle = subtitle

    menu.days_indexes = []
    menu.day1 = []
    menu.day2 = []
    menu.day3 = []
    menu.day4 = []
    menu.day5 = []
    menu.xml = []
    menu.filename = []

    # menu.indesign_file = '/Users/NLNEW/coding/indesign templates/menu du jour.indt'
    menu.indesign_file = '/Users/lousergonne/coding/indesign templates/menu du jour.indt'
    menu.txt_placeholder = "PLACEHOLDER"

    # input as list ; replacexml = [[word_to_replace, replacement_words], [word_to_replace, replacement_words], ...]
    menu.replace_in_xml = [['potage_', "potage"], ['plat_1', "plat 1"], ['plat_2', "plat 2"], ['légumes_', "légumes"],
                           ['dessert_', "dessert"]]

    root = TkinterDnD.Tk()
    root.title('menu')
    root.geometry("1000x300")

    menu_col = 2
    internat_col = 4

    def menu_file(filename):
        if ".txt" in filename:
            f = open(f"{filename}", "r")
            file_txt = f.read()
        elif ".docx" in filename:
            file_txt = docx2txt.process(filename)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=menu_col)
            raise ValueError("file not compatible")
        return file_txt

    def run_menu(filename):

        w = ttk.Label(root, text=f"file: {filename}")
        w.grid(row=6, column=menu_col)

        # start the time the proccess takes
        # start = time.time()
        originfile_name = filename

        # get the menu folder
        # menu_folder_path = originfile_name.rsplit("/", 1)
        # menu_folder_path = menu_folder_path[0][1:]
        # menu.menu_folder_path = menu_folder_path
        menu.menu_folder_path = "/Users/lousergonne/coding/"
        # print(menu.menu_folder_path)

        menu.input = replace(menu_file(originfile_name))
        # print(menu.input)
        menu.check_input()

        menu.wordsToList()
        menu.split_days()

        menu.filter_plats()
        menu.get_filename()
        # print(menu.input)

        menu.write_xml()

        menu.change_xml()
        move_mouse()

        menu.automate()

        time.sleep(5)
        # internat_indesign_file = '/Users/lousergonne/coding/indesign templates/internat menu.indt'
        # subprocess.call(('open', internat_indesign_file))
        # subprocess.call(('open', filepath_internat))
        # time.sleep(2)
        # subprocess.call("connect_to_db.py")

        ttk.Label(root, text=f"menu number: {menu.filename[0]}").grid(row=4, column=1)

        # connect to sftp to upload pdf 

        
        # end = time.time()
        # elapsed_time = end - start
        # elapsed_time = round(elapsed_time, menu_col)
        # ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=10, column=menu_col)

        log("done")

    def drop(event):
        filename = event.data
        filename = filename.strip("{")
        filename = filename.strip("}")
        log(filename)
        run_menu(filename)
        # internat_indesign_file = '/Users/lousergonne/coding/indesign templates/internat menu.indt'
        # subprocess.call(('open', internat_indesign_file))


    entry_sv = tkinter.StringVar()
    entry = tkinter.Entry(root, textvar=entry_sv, width=100)
    entry.grid(column=1, row=2)
    entry.drop_target_register(DND_FILES)
    entry.dnd_bind('<<Drop>>', drop)

    menu_txt = ttk.Label(root, text="drop your menu file here")
    menu_txt.grid(row=2, column=1)

    sv_ttk.set_theme("dark")
    root.mainloop()


mode = "Normal"
# mode = "xml"
# mode = "automation"

if mode == "Normal":
    main()

original_plat = """
Jour Date Mois
potage_
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
"""
