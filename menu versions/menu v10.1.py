import time
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

xml = []

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

    def update_presence_day(self, thing, jour, date):
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
        plat_check= self.plats["check_plats"]
        subtitles_check = self.subtitle["check_subtitle"]
        check = ['potage_', 'subtitle_potage', 'plat_1', 'subtitle_plat1', 'plat_2', 'subtitle_plat2', 'accompagnement', 'subtitle_accompagnement', 'légumes_', 'subtitle_légumes','dessert_', 'subtitle_dessert']
        
        numc = 0

        for x in check:
            if (numc % 2) == 0:
                if self.plats["plats_present"][self.plats["platlow_org"].index(x)] == False:
                    pass
                else:
                    try:
                        p = self.jour.index(x)
                    except:
                        p = self.jour.index((self.plats["platupper_org"][self.plats["platlow_org"].index(x)]))

                    self.plats_indexes.append(p)
            else:
                if self.subtitle['subtitle_present'][self.subtitle['subtitlelow_org'].index(x)] == False:
                    pass
                else:
                    try:
                        p = self.jour.index(x)
                    except:
                        p = self.jour.index(self.subtitles["subtitleupper_org"][self.plats["subtitlelow_org"].index(x)])
                    
                    self.plats_indexes.append(p)
            
            numc += 1
                    

        self.plats_indexes.append(len(self.jour))

        plats_lst = [self.plat1, self.subtitle1, self.plat2, self.subtitle2, self.plat3, self.subtitle3, self.plat4, self.subtitle4, self.plat5, self.subtitle5, self.plat6, self.subtitle6]
        
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

        daylow = self.days["daylow_org"]
        dayupper = self.days["dayupper_org"]

        num1 = 0
        for x in self.days["original_days"]:
            if daylow[num1] not in self.input and dayupper[num1] not in self.input:
                # print(f'Day {daylow[num1]} not included template wrong!')
                self.days["days_present"][num1] = False

            elif daylow[num1] in self.input or dayupper[num1] in self.input:
                # print(f'Day {daylow[num1]} included')
                self.days["days_present"][num1] = True
            
            num1 += 1

        platlow = self.plats["platlow_org"]
        platupper = self.plats["platupper_org"]

        num1 = 0

        for x in self.plats["check_plats"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                # print(f'plat {platlow[num1]} not included template wrong')
                self.plats["plats_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                # print(f'plat {platlow[num1]} included')
                self.plats["plats_present"][num1] = True
            
            num1 += 1
        
        platlow = self.subtitle["subtitlelow_org"]
        platupper = self.subtitle["subtitleupper_org"]

        num1 = 0

        for x in self.subtitle["original_subtitles"]:
            if platlow[num1] not in self.input and platupper[num1] not in self.input:
                # print(f'subtitle {platlow[num1]} not included template wrong')
                self.subtitle["subtitle_present"][num1] = False

            elif platlow[num1] in self.input or platupper[num1] in self.input:
                # print(f'plat {platlow[num1]} included')
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
        abc = "=:;«»’°|'ïäöüè/%+^¨&<>,.§ëöÿÏÖÜË('^)123456789¥0!-_" + abc1
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

                p.subtitle1 = []
                p.subtitle2 = []
                p.subtitle3 = []
                p.subtitle4 = []
                p.subtitle5 = []
                p.subtitle6 = []

                p.jour = days_lst[num1]
                p.plats_indexes = []

                p.get_plats_index()
                self.days = p.jour_lst


                plats_lst = [p.plat1, p.plat2, p.plat3, p.plat4, p.plat5, p.plat6]
                subtitles_lst = [p.subtitle1,  p.subtitle2, p.subtitle3, p.subtitle4, p.subtitle5, p.subtitle6]
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
                                subtitle_cache = "¥"

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

                print("subitle1: ", p.subtitle1)
                print("subitle2: ", p.subtitle2)
                print("subitle3: ", p.subtitle3)
                print("subitle4: ", p.subtitle4)
                print("subitle5: ", p.subtitle5)
                print("subitle6: ", p.subtitle6)

            num1 += 1

    def get_filename(self):
        first_day = ""
        to_ind = ""
        print(self.days["days_present"])
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
        month = datee[-1]
        month = month_string_to_number(month)

        day_num = datee[-2]
        if len(day_num) < 2:
            day_num = "0" + day_num
        
        year = time.strftime("%Y")
        year = year.lstrip("2")
        year = year.lstrip("0")
        filename = str(year) + str(month) + str(day_num)
        self.filename.append(filename)

    def write_xml(self):
        xml_content = self.xml

        f = open(f"{self.filename[0]}.xml", "a")
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
                                print("empty slot found")
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
                    print("error while writing xml")
                    pass

        f.write(menu_out)
            
        f.close()

    def change_xml(self):
        
        with open(f'{self.filename[0]}.xml', 'r') as file:
            filedata = file.read()

            # Replace the target string
            
        for thing in self.replace_in_xml:
            filedata = filedata.replace(thing[0], thing[1])

            # Write the file out again
        with open(f'{self.filename[0]}.xml', 'w') as file:
            file.write(filedata)
        
    def automate(self):
        def import_xml(self):
            pg.hotkey("command", "9")
            time.sleep(2)
            
            # pg.click(1577, 311)
            pg.hotkey("shift", "7")

            time.sleep(2)
            pg.press("backspace")
            time.sleep(2)

            write_to_clipboard(f"{self.filename[0]}.xml")
            pg.hotkey("command", "v")
            time.sleep(2)
            pg.press("enter")
            # pg.click(1548, 420)
            time.sleep(2)

            pg.press("enter")
            time.sleep(2)

            pg.press("enter")
            time.sleep(2)
                                            
        def indesign_replace(self):
            pg.hotkey('command', 'f')
            time.sleep(2)

            # select profile
            pg.click(1888, 303)

            pg.click(1890, 344)

            pg.click(2160, 528)
            time.sleep(2)

            pg.press("enter")
            time.sleep(2)

            pg.click(2200, 723)

            time.sleep(2)

        def indesign_export_file(self):
            pg.hotkey("command", "e")
            time.sleep(2)

            pg.hotkey("shift", "7")
            time.sleep(1)

            write_to_clipboard(self.final_dir)
            time.sleep(0.5)

            pg.hotkey("command", "v")
            time.sleep(1)

            pg.press("enter")
            time.sleep(1)

            pg.press("enter")
            time.sleep(1)

            pg.press("enter")
            time.sleep(0.5)

        def check_all_pages(self):
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
        
        def save_indesign_file(self):
            time.sleep(1)

            pg.hotkey("command", "s")
            time.sleep(2)

            pg.hotkey("shift", "7")
            time.sleep(1)

            write_to_clipboard(self.final_dir)
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

        # set directories 
        self.final_dir_pdf = f'{self.menu_folder_path}/{self.filename[0]} menu.pdf'
        self.final_dir_id = f'{self.menu_folder_path}/{self.filename[0]} menu indesign'

        # import the xml
        import_xml(self.filename[0])

        # replace ¥ with withespace
        indesign_replace(self.filename[0])
        
        # check and delete all non existance pages
        check_all_pages()

        # export as idd file and pdf to folder

        indesign_export_file()
        save_indesign_file()


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

inpp = """
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

inp1 = """

Lundi
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

Mardi DATE avril	
potage_	 Potage du jour 2
subtitle_potage	 89dfg
plat_1	 Plat1 2
subtitle_plat1	 7dfg
plat_2	 46dfg
subtitle_plat2	 
accompagnement	 23
subtitle_accompagnement	 dfgdfgdfg
légumes_	 ssss
subtitle_légumes	 2
dessert_	 dfgs
subtitle_dessert	 222

Mercredi DATE MOIS	dfg
potage_	 Potage du jour 39fg
subtitle_potage	 9
plat_1	 Plat1 3dfgd
subtitle_plat1	 9
plat_2	 
subtitle_plat2	 9dfg
accompagnement	 9dfg
subtitle_accompagnement	 
légumes_	 9
subtitle_légumes	 
dessert_	 
subtitle_dessert	 
dfg
Jeudi DATE MOIS	
potage_	 Potage du jour 40
subtitle_potage	 
plat_1	 Plat1 4
subtitle_plat1	 '978
plat_2	 
subtitle_plat2	 ^
accompagnement	 8
subtitle_accompagnement	 9
légumes_	 7
subtitle_légumes	 65
dessert_	 55
subtitle_dessert	 443

Vendredi
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

inp = """"

Lundi 02 avril
potage_	¥
subtitle_potage	¥
plat_1	¥
subtitle_plat1	¥
plat_2	¥
subtitle_plat2	¥
Accompagnement	
subtitle_accompagnement	¥
légumes_	
subtitle_légumes	
dessert_ ¥
subtitle_dessert	

Mardi 2 mai	
 potage_ ¥
subtitle_potage	¥
plat_1
subtitle_plat1
plat_2 ¥
subtitle_plat2
Accompagnement	¥
subtitle_accompagnement	
légumes_	¥
subtitle_légumes	
dessert_	
subtitle_dessert	 

Mercredi 2 mai
 potage_	¥
subtitle_potage	
plat_1 ¥
subtitle_plat1	
plat_2 ¥
subtitle_plat2	
Accompagnement	¥
subtitle_accompagnement	
légumes_	 ¥
subtitle_légumes	
dessert_	 ¥
subtitle_dessert	 

Jeudi 2 mai
 potage_	 ¥
subtitle_potage	
plat_1
subtitle_plat1 ¥
plat_2 ¥
subtitle_plat2 ¥
Accompagnement	
subtitle_accompagnement	 ¥
légumes_	 ¥
subtitle_légumes	
dessert_	 ¥
subtitle_dessert	  ¥

Vendredi 2 mai
 potage_ ¥
subtitle_potage	
plat_1	 ¥
subtitle_plat1 ¥
plat_2	 ¥
subtitle_plat2	
Accompagnement	 ¥
subtitle_accompagnement	 ¥
légumes_	 ¥
subtitle_légumes	 ¥
dessert_	 ¥
subtitle_dessert	 


"""


m.input = inp
m.xml = xml
m.filename = []
m.txt_placeholder = "PLACEHOLDER"

# input as list ; replacexml = [[word_to_replace, replacement_words], [word_to_replace, replacement_words], ...]
m.replace_in_xml = [['potage_', "potage"],['plat_1', "plat 1"], ['plat_2', "plat 2"], ['légumes_', "légumes"], [ 'dessert_', "dessert"]]

m.check_input()

m.wordsToList()
m.split_days()

m.filter_plats()
m.get_filename()

m.write_xml()
m.change_xml()

