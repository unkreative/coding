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


# indesign_template = '/Users/NLNEW/coding/indesign template working 3.indd'
menu_indesign_template = '/Users/NLNEW/coding/menu du jour.indt'
internat_indesign_template = '/Users/NLNEW/coding/internat menu.indt'

folder = []

delay1 = 0.5
delay2 = 1
delay3 = 2
delay4 = 4


# basic funtions
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
        raise ValueError(f"{arg} are false")


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


def wordsToList(strn):
    L = strn.split()
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
    return cleanL


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
        raise ValueError('Not a month')


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


# check input functions
def check_input(input):
    daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    number1 = 0
    while number1 < len(daylow):
        if daylow[number1] not in input and dayupper[number1] not in input:
            raise ValueError('Day not inclouded')
        else:
            number1 += 1
        print("input check 1 done")

        return input


def check_input2(input):
    plat1_correct = "\nplat1"
    plat2_correct = "\nplat2"
    légumes_correct = "\nLégumes"
    plat1_num = re.findall("\nplat 1", input)
    plat2_num = re.findall("\nplat 2", input)
    plat11_num = re.findall("\nPlat 1", input)
    plat22_num = re.findall("\nPlat 2", input)
    légumes_num = re.findall("\nlégumes", input)

    for x in plat1_num:
        input = input.replace(plat1_num[0], plat1_correct)

    for x in plat2_num:
        input = input.replace(plat2_num[0], plat2_correct)

    for x in plat11_num:
        input = input.replace(plat11_num[0], plat1_correct)

    for x in plat22_num:
        input = input.replace(plat22_num[0], plat2_correct)

    for x in légumes_num:
        input = input.replace(légumes_num[0], légumes_correct)

    # print(input)
    print("input check 2 done")

    return input


def check_input3(input):
    plats_down = ["\npotage", "\nplat1", "\nplat2", "\naccompagnement", "\nLégumes", "\ndessert"]
    plats_up = ["\nfill_string", "\nPlat1", "\nPlat2", "\nAccompagnement", "fill_string", "\nDessert"]

    sub_down = ["\nsubtitle_potage", "\nsubtitle_plat1", "\nsubtitle_plat2", "\nsubtitle_accompagnement",
                "\nsubtitle_légumes", "\nsubtitle_dessert"]
    sub_up = ["\nSubtitle_potage", "\nSubtitle_plat1", "\nSubtitle_plat2", "\nSubtitle_accompagnement",
              "\nSubtitle_légumes", "\nSubtitle_dessert"]

    plats = ["potage", "plat1", "plat2", "accompagnement", "Légumes", "dessert"]

    plats_num_list = []
    plats_text_list = []
    sub_num_list = []
    sub_text_list = []
    results = []

    num1 = 0
    while num1 < 6:
        findall_in_string(input, plats_down[num1], plats_up[num1], plats_num_list, plats_text_list)
        num1 += 1

    num1 = 0
    while num1 < 6:
        findall_in_string(input, sub_down[num1], sub_up[num1], sub_num_list, sub_text_list)
        num1 += 1

    num1 = 0
    while num1 <= 5:
        print("plats_num_list: ", plats_num_list)
        print("sub_num_list: ", sub_num_list)
        value = if_same(plats_num_list[num1], sub_num_list[num1], num1)
        value = f"{plats[num1]} is {value}"
        # print(value)
        results.append(value)
        num1 += 1

    # print(results)
    print("input check 3 done")
    return input


def check_input4(input):
    input = str(input)

    if input.count("&") > 0:
        input = input.replace("&", "&amp;")

    else:
        print("not found")

    if input.count("<") > 0:
        input = input.replace("<", "&lt;")

    if input.count(">") > 0:
        input = input.replace(">", "&gt;")
    print("input check 4 done")
    return input


# find days, etc.
# menu_list = menu list from wordstolist
def find_days(menu_list, menus, menu_ind, arg):
    daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    number2 = 0

    len_menu = len(daylow)

    while number2 <= len_menu:
        if daylow[number2] in menu_list or dayupper[number2] in menu_list:

            menus.append(daylow[number2])

            id = dayupper[number2]

            indexx = menu_list.index(id)
            menu_ind.append(indexx)

            number2 += 1

            if number2 == len_menu:
                break

    if arg == "1":
        return menus
    elif arg == "2":
        return menu_ind


def find_plats(indicator, list_plats, index_plats):
    global id
    index_plats.clear()
    plat_down_tmpl = ["potage", "subtitle_potage", "plat1", "subtitle_plat1", "plat2", "subtitle_plat2",
                      "accompagnement", "subtitle_accompagnement", "Légumes", "subtitle_légumes", "dessert",
                      "subtitle_dessert"]
    plat_up_tmpl = ["potage", "Subtitle_potage", "Plat1", "Subtitle_plat1", "Plat2", "Subtitle_plat2", "Accompagnement",
                    "Subtitle_accompagnement", "Légumes", "Subtitle_légumes", "Dessert", "Subtitle_dessert"]
    plats_final = ["potage", "Subtitle_potage", "plat 1", "Subtitle_plat1", "plat 2", "Subtitle_plat2",
                   "accompagnement", "Subtitle_accompagnement", "légumes", "Subtitle_légumes", "dessert",
                   "Subtitle_dessert"]

    number2 = 0
    plat_len = len(plat_down_tmpl)

    while number2 < plat_len:
        if plat_down_tmpl[number2] in indicator or plat_up_tmpl[number2] in indicator:

            list_plats.append(plats_final[number2])

            if plat_down_tmpl[number2] in indicator:
                id = plat_down_tmpl[number2]

            if plat_up_tmpl[number2] in indicator:
                id = plat_up_tmpl[number2]

            indexx = indicator.index(id)

            index_plats.append(indexx)

        number2 += 1

    return list_plats


# split things
def splitslots(day, day_indexes, app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, app11, app12):
    len_index = len(day_indexes)
    number1 = 0
    day_indexes.append(len(day))
    n1 = 1
    while number1 < len_index:
        number2 = number1 + n1

        if number1 == 0:
            app1 = select_string(day_indexes[number1], day_indexes[number2], app1, day)

        if number1 == 1:
            app2 = select_string(day_indexes[number1], day_indexes[number2], app2, day)

        if number1 == 2:
            app3 = select_string(day_indexes[number1], day_indexes[number2], app3, day)

        if number1 == 3:
            app4 = select_string(day_indexes[number1], day_indexes[number2], app4, day)

        if number1 == 4:
            app5 = select_string(day_indexes[number1], day_indexes[number2], app5, day)

        if number1 == 5:
            app6 = select_string(day_indexes[number1], day_indexes[number2], app6, day)

        if number1 == 6:
            app7 = select_string(day_indexes[number1], day_indexes[number2], app7, day)

        if number1 == 7:
            app8 = select_string(day_indexes[number1], day_indexes[number2], app8, day)

        if number1 == 8:
            app9 = select_string(day_indexes[number1], day_indexes[number2], app9, day)

        if number1 == 9:
            app10 = select_string(day_indexes[number1], day_indexes[number2], app10, day)

        if number1 == 10:
            app11 = select_string(day_indexes[number1], day_indexes[number2], app11, day)

        if number1 == 11:
            app12 = select_string(day_indexes[number1], day_indexes[number2], app12, day)

        number1 += 1
    return "done"


def show_date(number, app, jour, year):
    num1 = 0
    num2 = number[0]

    while num1 < num2:
        app.append(jour[num1])
        num1 += 1
    app.append(f"{year}")
    return app


# xml things
def toxml(xml, day_plats, day_slot1a, day_slot1b, day_slot2a, day_slot2b, day_slot3a, day_slot3b, day_slot4a,
          day_slot4b, day_slot5a, day_slot5b, day_slot6a, day_slot6b):
    # print(day_plats)
    # print(day_slot1b)
    print()

    number1 = 0
    number2 = 0
    day_plats = (day_slot1a, day_slot2a, day_slot3a, day_slot4a, day_slot5a, day_slot6a)

    day_underitles = (day_slot1b, day_slot2b, day_slot3b, day_slot4b, day_slot5b, day_slot6b)

    indexumm = len(day_plats)

    while number1 < indexumm:
        cache = []
        cache.clear()

        plat = day_plats[number1]

        u = day_underitles[number1]
        cache_title = []
        if len(plat) > 1:
            if bool(plat):
                if plat[0] == "potage":
                    plat[0] = "potage"

                if plat[0] == "plat1":
                    plat[0] = "plat 1"

                if plat[0] == "plat2":
                    plat[0] = "plat 2"

                if plat[0] == "Accompagnement":
                    plat[0] = "accompagnement"

                if plat[0] == "Légumes":
                    plat[0] = "légumes"

                if plat[0] == "Dessert":
                    plat[0] = "dessert"

                print("Title: ", plat[0], "; Menu: ", plat[1])

                cache_title.append(plat[0])
                # print(cache_title[0])

                plat.pop(0)

            if bool(u):
                u.pop(0)

            cache_plat = " ".join(str(x) for x in plat)
            cache_under = " ".join(str(x) for x in u)
            if not cache_under:
                cache_under = cache_under + "¥"
            if not plat:
                number1 += 1
                pass
            else:
                module1 = f"""
                <slot{number2}>
                    <title>{cache_title[0]}</title>
                    <plat>{cache_plat}</plat>  
                    <undertitle>{cache_under}</undertitle>
                </slot{number2}>\n"""
                xml.append(module1)
                number2 += 1

            number1 += 1
        else:
            number1 += 1

    while number2 < 6:
        module1 = f"""
                <slot{number2}>
                    <title>¥</title>
                    <plat>¥</plat>  
                    <undertitle>¥</undertitle>
                </slot{number2}>\n"""
        xml.append(module1)
        number2 += 1


def create_file_name(day1):
    # print(day1)
    app = []
    year = time.strftime("%Y")
    year = year.lstrip("2")
    year = year.lstrip("0")
    # print(year)
    month = day1[2]

    month = month_string_to_number(month)
    month = str(month)
    day = day1[1]
    if len(day) < 2:
        day = "0" + day
    app = year + month + day
    return app

def create_id_filename(date, month):
    year = get_year()
    year = str(year).lstrip("2")
    year = str(year).lstrip("0")

    print(date)
    print(month)
    month = month_string_to_number(month)

    if len(date) < 2:
        date = "0" + date
    app = year + month + date
    return app


def writexml(file_name, day1, day2, day3, day4, day5, date1, date2, date3, date4, date5):
    fwrite = open(f"{file_name}.xml", "a")
    date1 = listToString(date1)
    date2 = listToString(date2)
    date3 = listToString(date3)
    date4 = listToString(date4)
    date5 = listToString(date5)
    day1 = listToString(day1)
    day2 = listToString(day2)
    day3 = listToString(day3)
    day4 = listToString(day4)
    day5 = listToString(day5)

    dayss = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    fwrite.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
    fwrite.write("""<menu>\n""")
    days = [day1, day2, day3, day4, day5]
    date = [date1, date2, date3, date4, date5]
    number1 = 0
    while number1 < 5:
        fwrite.write(f"""   <{dayss[number1]}>\n""")
        fwrite.write(f"""       <date>{date[number1]}</date>""")
        fwrite.write(days[number1])
        fwrite.write(f"""   </{dayss[number1]}>\n""")
        number1 += 1
    fwrite.write("""</menu>\n""")
    fwrite.close()


# run the menu code
def run_menu(input):
    year = get_year()

    # lists
    days = []
    days_index = []

    lundi = []
    lundi_plats = []
    lundi_plats_index = []
    lundi_date = []
    lundi_slot1a = []
    lundi_slot2a = []
    lundi_slot3a = []
    lundi_slot4a = []
    lundi_slot5a = []
    lundi_slot6a = []

    lundi_slot1b = []
    lundi_slot2b = []
    lundi_slot3b = []
    lundi_slot4b = []
    lundi_slot5b = []
    lundi_slot6b = []
    lundi_xml = []

    mardi = []
    mardi_plats = []
    mardi_plats_index = []
    mardi_date = []
    mardi_slot1a = []
    mardi_slot2a = []
    mardi_slot3a = []
    mardi_slot4a = []
    mardi_slot5a = []
    mardi_slot6a = []

    mardi_slot1b = []
    mardi_slot2b = []
    mardi_slot3b = []
    mardi_slot4b = []
    mardi_slot5b = []
    mardi_slot6b = []
    mardi_xml = []

    mercredi = []
    mercredi_plats = []
    mercredi_plats_index = []
    mercredi_date = []
    mercredi_slot1a = []
    mercredi_slot2a = []
    mercredi_slot3a = []
    mercredi_slot4a = []
    mercredi_slot5a = []
    mercredi_slot6a = []

    mercredi_slot1b = []
    mercredi_slot2b = []
    mercredi_slot3b = []
    mercredi_slot4b = []
    mercredi_slot5b = []
    mercredi_slot6b = []
    mercredi_xml = []

    jeudi = []
    jeudi_plats = []
    jeudi_plats_index = []
    jeudi_date = []
    jeudi_slot1a = []
    jeudi_slot2a = []
    jeudi_slot3a = []
    jeudi_slot4a = []
    jeudi_slot5a = []
    jeudi_slot6a = []

    jeudi_slot1b = []
    jeudi_slot2b = []
    jeudi_slot3b = []
    jeudi_slot4b = []
    jeudi_slot5b = []
    jeudi_slot6b = []
    jeudi_xml = []

    vendredi = []
    vendredi_plats = []
    vendredi_plats_index = []
    vendredi_date = []
    vendredi_slot1a = []
    vendredi_slot2a = []
    vendredi_slot3a = []
    vendredi_slot4a = []
    vendredi_slot5a = []
    vendredi_slot6a = []

    vendredi_slot1b = []
    vendredi_slot2b = []
    vendredi_slot3b = []
    vendredi_slot4b = []
    vendredi_slot5b = []
    vendredi_slot6b = []
    vendredi_xml = []

    input = check_input(input)
    input = check_input2(input)
    input = check_input3(input)
    input = check_input4(input)

    input = wordsToList(input)

    days = find_days(input, days, days_index, "2")

    lundi = append_things(days[0], days[1], lundi, input)
    mardi = append_things(days[1], days[2], mardi, input)
    mercredi = append_things(days[2], days[3], mercredi, input)
    jeudi = append_things(days[3], days[4], jeudi, input)
    vendredi = append_things(days[4], len(input), vendredi, input)

    lundi_plats = find_plats(lundi, lundi_plats, lundi_plats_index)
    mardi_plats = find_plats(mardi, mardi_plats, mardi_plats_index)
    mercredi_plats = find_plats(mercredi, mercredi_plats, mercredi_plats_index)
    jeudi_plats = find_plats(jeudi, jeudi_plats, jeudi_plats_index)
    vendredi_plats = find_plats(vendredi, vendredi_plats, vendredi_plats_index)

    lundi_date = show_date(lundi_plats_index, lundi_date, lundi, year)
    mardi_date = show_date(mardi_plats_index, mardi_date, mardi, year)
    mercredi_date = show_date(mercredi_plats_index, mercredi_date, mercredi, year)
    jeudi_date = show_date(jeudi_plats_index, jeudi_date, jeudi, year)
    vendredi_date = show_date(vendredi_plats_index, vendredi_date, vendredi, year)

    run_lundi = splitslots(lundi, lundi_plats_index, lundi_slot1a, lundi_slot1b, lundi_slot2a, lundi_slot2b,
                           lundi_slot3a, lundi_slot3b, lundi_slot4a, lundi_slot4b, lundi_slot5a, lundi_slot5b,
                           lundi_slot6a, lundi_slot6b)
    run_mardi = splitslots(mardi, mardi_plats_index, mardi_slot1a, mardi_slot1b, mardi_slot2a, mardi_slot2b,
                           mardi_slot3a, mardi_slot3b, mardi_slot4a, mardi_slot4b, mardi_slot5a, mardi_slot5b,
                           mardi_slot6a, mardi_slot6b)
    run_mercredi = splitslots(mercredi, mercredi_plats_index, mercredi_slot1a, mercredi_slot1b, mercredi_slot2a,
                              mercredi_slot2b, mercredi_slot3a, mercredi_slot3b, mercredi_slot4a, mercredi_slot4b,
                              mercredi_slot5a, mercredi_slot5b, mercredi_slot6a, mercredi_slot6b)
    run_jeudi = splitslots(jeudi, jeudi_plats_index, jeudi_slot1a, jeudi_slot1b, jeudi_slot2a, jeudi_slot2b,
                           jeudi_slot3a, jeudi_slot3b, jeudi_slot4a, jeudi_slot4b, jeudi_slot5a, jeudi_slot5b,
                           jeudi_slot6a, jeudi_slot6b)
    run_vendredi = splitslots(vendredi, vendredi_plats_index, vendredi_slot1a, vendredi_slot1b, vendredi_slot2a,
                              vendredi_slot2b, vendredi_slot3a, vendredi_slot3b, vendredi_slot4a, vendredi_slot4b,
                              vendredi_slot5a, vendredi_slot5b, vendredi_slot6a, vendredi_slot6b)

    # print("run_lundi: ", run_lundi)
    # print("run_mardi: ", run_mardi)
    # print("run_mercredi: ", run_mercredi)
    # print("run_jeudi: ", run_jeudi)
    # print("run_vendredi: ", run_vendredi)

    run_lundi = toxml(lundi_xml, lundi_plats, lundi_slot1a, lundi_slot1b, lundi_slot2a, lundi_slot2b, lundi_slot3a,
                      lundi_slot3b, lundi_slot4a, lundi_slot4b, lundi_slot5a, lundi_slot5b, lundi_slot6a, lundi_slot6b)
    run_mardi = toxml(mardi_xml, mardi_plats, mardi_slot1a, mardi_slot1b, mardi_slot2a, mardi_slot2b, mardi_slot3a,
                      mardi_slot3b, mardi_slot4a, mardi_slot4b, mardi_slot5a, mardi_slot5b, mardi_slot6a, mardi_slot6b)
    run_mercredi = toxml(mercredi_xml, mercredi_plats, mercredi_slot1a, mercredi_slot1b, mercredi_slot2a,
                         mercredi_slot2b, mercredi_slot3a, mercredi_slot3b, mercredi_slot4a, mercredi_slot4b,
                         mercredi_slot5a, mercredi_slot5b, mercredi_slot6a, mercredi_slot6b)
    run_jeudi = toxml(jeudi_xml, jeudi_plats, jeudi_slot1a, jeudi_slot1b, jeudi_slot2a, jeudi_slot2b, jeudi_slot3a,
                      jeudi_slot3b, jeudi_slot4a, jeudi_slot4b, jeudi_slot5a, jeudi_slot5b, jeudi_slot6a, jeudi_slot6b)
    run_vendredi = toxml(vendredi_xml, vendredi_plats, vendredi_slot1a, vendredi_slot1b, vendredi_slot2a,
                         vendredi_slot2b, vendredi_slot3a, vendredi_slot3b, vendredi_slot4a, vendredi_slot4b,
                         vendredi_slot5a, vendredi_slot5b, vendredi_slot6a, vendredi_slot6b)

    file_name = create_file_name(lundi_date)
    write_to_clipboard(file_name)

    run_xml = writexml(file_name, lundi_xml, mardi_xml, mercredi_xml, jeudi_xml, vendredi_xml, lundi_date, mardi_date,
                       mercredi_date, jeudi_date, vendredi_date)
    # print("run_lundi: ", run_lundi)
    # print("run_mardi: ", run_mardi)
    # print("run_mercredi: ", run_mercredi)
    # print("run_jeudi: ", run_jeudi)
    # print("run_vendredi: ", run_vendredi)
    # print("run_xml: ", run_xml)

    folder.append(file_name)

    return file_name


# internat functions
def cleanup(day1, day2, day3, day4):
    replace = ["potage", "Potage", "plat1", "Plat1", "plat2", "Plat2", "accompagnement", "Accompagnement", "légumes",
               "Légumes", "dessert", "Dessert", "subtitle_potage", "Subtitle_potage", "subtitle_plat1",
               "Subtitle_plat1", "subtitle_plat2", "Subtitle_plat2", "subtitle_accompagnement",
               "Subtitle_accompagnement", "subtitle_légumes", "Subtitle_légumes", "subtitle_dessert",
               "Subtitle_dessert", "Subtitle_"]
    days = [day1, day2, day3, day4]
    for x in days:
        for y in replace:
            if y in x:
                x.remove(y)
            else:
                pass


def internats_writexml(file_name, xml, date):
    fwrite = open(f"{file_name}.xml", "a")

    fwrite.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
    fwrite.write("""<internats_menu>\n""")

    number1 = 0
    fwrite.write(f"""       <date>{date}</date>""")

    while number1 < 4:
        fwrite.write(f"{xml[number1]}")

        number1 += 1
    fwrite.write("""</internats_menu>\n""")
    fwrite.close()


# run internat things

def run_internat(input):
    year = get_year()
    str_input = check_input(input)
    str_input = check_input2(str_input)
    str_input = check_input4(str_input)
    lst_input = wordsToList(str_input)

    idays_index = []
    idays = []
    internat_days = find_days(lst_input, idays, idays_index, "2")

    internat_lundi = []
    internat_mardi = []
    internat_mercredi = []
    internat_jeudi = []

    internat_lundi = append_things(internat_days[0], internat_days[1], internat_lundi, lst_input)
    internat_mardi = append_things(internat_days[1], internat_days[2], internat_mardi, lst_input)
    internat_mercredi = append_things(internat_days[2], internat_days[3], internat_mercredi, lst_input)
    internat_jeudi = append_things(internat_days[3], internat_days[4], internat_jeudi, lst_input)

    # print(lundi)
    # print(mardi)
    # print(mercredi)
    # print(jeudi)

    internat_day1 = internat_lundi[1]
    internat_day2 = internat_jeudi[1]
    internat_month = internat_jeudi[2]

    filename = f"{create_id_filename(internat_lundi[1], internat_lundi[2])}"
    xml_filename = f"{filename}-internat"
    final_month = f"menu du {internat_day1} au {internat_day2} {internat_month} {year}"

    cleanup(internat_lundi, internat_mardi, internat_mercredi, internat_jeudi)

    days = [internat_lundi, internat_mardi, internat_mercredi, internat_jeudi]
    ndays = ["lundi", "mardi", "mercredi", "jeudi"]
    num1 = 0
    xml = []

    # print(days)
    while num1 < len(days):
        day = days[num1]
        nday = ndays[num1]
        # print(type(day))

        day.pop(0)
        day.pop(0)
        day.pop(0)

        num5 = 1
        while num5 < len(day):
            xx = str(day[num5])
            uppercase = xx[0].isupper()
            if uppercase == False:
                pass
            else:
                day[num5] = f"\n{xx}"
            num5 += 1

        cache = ' '.join([str(item) for item in day])

        print("cache: ", cache)

        module2 = f"""
        <slot{num1}>
            <title>{nday}</title>
            <plat>{cache}</plat>
        </slot{num1}>\n"""

        print(module2)
        xml.append(module2)
        num1 += 1

    internats_writexml(xml_filename, xml, final_month)
    return filename, xml_filename


# automate things
# general

# connect to server
def server_connect():
    finder = '/System/Library/CoreServices/Finder.app'

    subprocess.call(('open', finder))
    time.sleep(delay2)

    pg.press("escape")
    time.sleep(delay2)

    pg.hotkey("command", "k")
    time.sleep(delay2)

    pg.hotkey("enter")
    time.sleep(delay1)

# find if fullscreen
def find_full_size(screenshot):
    with Image.open(screenshot).convert('RGB') as pim:
        im = np.array(pim)

        green = [63, 197, 73]
        # green = [98, 196, 84]

        Y, X = np.where(np.all(im == green, axis=2))

        lx = len(X)
        lx = int(lx / 2)
        xcord = X[0]
        ycord = Y[0]

        nx = 1.982142857142857
        ny = 2
        xcord = xcord / nx
        ycord = ycord / ny

    final_cords = (round(xcord), round(ycord))

    upper_left_corner = (50, 36)
    upper_right_corner = (60, 36)
    lower_left_corner = (50, 50)
    lower_right_corner = (60, 50)

    input_points = final_cords
    print(input_points)

    def check_cords(pt1, pt2, num=[], num1=[], result=[]):
        x1, x2 = pt1[0], pt2[0]
        y1, y2 = pt1[1], pt2[1]

        minimum_x1 = min(x1, x2)
        minimum_y1 = min(y1, y2)

        maximum_x1 = max(x1, x2)
        maximum_y1 = max(y1, y2)

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
                    break

    res = []
    check_cords(upper_left_corner, lower_left_corner, result=res)
    print(res)
    if res:
        try:
            if res:
                if res[0] == True:
                    print("good")
                else:
                    print("none")

        except:
            print("false coordinate")
            pg.leftClick(xcord, ycord)
    return res


# import xml
def import_xml(filename):
    pg.hotkey("command", "9")
    time.sleep(delay2)
    
    # pg.click(1577, 311)
    pg.hotkey("shift", "7")

    time.sleep(delay2)
    pg.press("backspace")
    time.sleep(delay2)

    write_to_clipboard(f"{filename}.xml")
    pg.hotkey("command", "v")
    time.sleep(delay2)
    pg.press("enter")
    # pg.click(1548, 420)
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay2)


# replace text (¥)
def indesign_replace(filename):
    pg.hotkey('command', 'f')
    time.sleep(delay2)

    # select profile
    pg.click(1888, 303)

    pg.click(1890, 344)

    pg.click(2160, 528)
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay2)

    pg.click(2200, 723)

    time.sleep(delay2)


# export file as pdf
def indesign_export_file(filename, final_dir):
    pg.hotkey("command", "e")
    time.sleep(delay3)

    pg.hotkey("shift", "7")
    time.sleep(delay2)

    write_to_clipboard(final_dir)
    time.sleep(delay1)

    pg.hotkey("command", "v")
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay1)


def save_indesign_file(filename, final_dir):
    time.sleep(delay2)
    # for test purposes
    # pg.hotkey("command", "shift", "s")

    # real solution
    pg.hotkey("command", "s")
    time.sleep(delay3)

    pg.hotkey("shift", "7")
    time.sleep(delay2)

    write_to_clipboard(final_dir)
    time.sleep(delay1)

    pg.hotkey("command", "v")
    time.sleep(delay2)

    pg.press("enter")
    time.sleep(delay1)

    pg.press("enter")
    time.sleep(delay2)

# menu automation
def automate(indesign_file, filename):
    server_connect()
    time.sleep(3)

    subprocess.call(('open', indesign_file))
    time.sleep(8)

    screen_path = "/Users/NLNEW/Desktop/screen.png"
    final_dir_pdf = f'Volumes/Classes_21_22/Chelsea Studios/1 Graphic Designers/2 Clients/16 Restaurant Mélusine/Menu/{filename}/{filename} menu.pdf'
    final_dir_id = f'Volumes/Classes_21_22/Chelsea Studios/1 Graphic Designers/2 Clients/16 Restaurant Mélusine/Menu/{filename}/{filename} menu indesign'

    pg.screenshot(screen_path)

    results = find_full_size(screen_path)
    print(results)

    import_xml(filename)
    indesign_replace(filename)
    indesign_export_file(filename, final_dir_pdf)
    save_indesign_file(filename, final_dir_id)

# indesign automation 

def internat_automate(id_file, filename, xml_filename):
    server_connect()
    time.sleep(3)

    subprocess.call(('open', id_file))
    time.sleep(8)

    screen_path = "/Users/NLNEW/Desktop/screen.png"
    final_dir_pdf = f'Volumes/Classes_21_22/Chelsea Studios/1 Graphic Designers/2 Clients/16 Restaurant Mélusine/Menus/{filename}/{filename} internat'
    final_dir_id = f'Volumes/Classes_21_22/Chelsea Studios/1 Graphic Designers/2 Clients/16 Restaurant Mélusine/Menus/{filename}/{filename} internat indesign'

    pg.screenshot(screen_path)

    results = find_full_size(screen_path)
    print(results)

    import_xml(xml_filename)
    indesign_replace(filename)
    indesign_export_file(filename, final_dir_pdf)
    save_indesign_file(filename, final_dir_id)

# GUI

def overlay():
    root = tk.Tk()
    root.title('menu')
    root.geometry("1000x300")

    menu_col = 2
    internat_col = 4
    source_check_lou = os.path.exists("/Users/lousergonne")
    source_check_NLNEW = os.path.exists("/Users/NLNEW")

    source_NLNEW = "/Users/NLNEW/Downloads/Sun-Valley-ttk-theme-master/sun-valley.tcl"
    source_lou = "/Users/lousergonne/Documents/Sun-Valley-ttk-theme-master/sun-valley.tcl"

    if source_check_lou == True:
        source = source_lou
    elif source_check_NLNEW:
        source = source_NLNEW

    root.tk.call("source", source)
    root.tk.call("set_theme", "dark")

    def change_theme():
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            root.tk.call("set_theme", "light")
        else:
            root.tk.call("set_theme", "dark")

    def file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=menu_col)
            raise ValueError("file not compatible")
        return file_txt

    def internat_file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=internat_col)
            raise ValueError("file not compatible")
        return file_txt

    def run_men():
        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a file",
                                                   filetypes=filetypes)
        w = ttk.Label(root, text=f"file: {root.filename}")

        w.grid(row=6, column=menu_col)
        start = time.time()
        originfile_name = root.filename
        menu_contents = file(originfile_name)
        menu_filename = run_menu(menu_contents)
        automate(menu_indesign_template, menu_filename)

        ttk.Label(root, text=f"menu number: {menu_filename}").grid(row=8, column=menu_col)

        end = time.time()
        elapsed_time = end - start
        elapsed_time = round(elapsed_time, menu_col)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=10, column=menu_col)

        log("done")

    def run_inter():
        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a file",
                                                   filetypes=filetypes)

        w = ttk.Label(root, text=f"file: {root.filename}")
        w.grid(row=6, column=internat_col)

        start = time.time()
        originfile_name = root.filename
        internat_contents = internat_file(originfile_name)

        internat_filename, internat_xml_file = run_internat(internat_contents)
        internat_automate(internat_indesign_template, internat_filename, internat_xml_file)
        # internat_automate(internat_indesign_template, internat_filename, folder)

        ttk.Label(root, text=f"internat number: {internat_filename}").grid(row=8, column=internat_col)

        end = time.time()
        elapsed_time = end - start
        elapsed_time = round(elapsed_time, menu_col)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=10, column=internat_col)

        log("done")

    w = ttk.Label(root, text="⠀").grid(row=1, column=1)
    w = ttk.Label(root, text="⠀").grid(row=2, column=2)
    w = ttk.Label(root, text="⠀").grid(row=3, column=3)
    w = ttk.Label(root, text="⠀").grid(row=4, column=4)
    w = ttk.Label(root, text="⠀").grid(row=5, column=5)
    w = ttk.Label(root, text="⠀").grid(row=6, column=6)
    w = ttk.Label(root, text="⠀").grid(row=7, column=7)
    w = ttk.Label(root, text="⠀").grid(row=8, column=8)
    w = ttk.Label(root, text="⠀").grid(row=9, column=9)
    w = ttk.Label(root, text="⠀").grid(row=10, column=10)
    w = ttk.Label(root, text="⠀").grid(row=11, column=11)
    w = ttk.Label(root, text="⠀").grid(row=12, column=12)
    w = ttk.Label(root, text="⠀").grid(row=13, column=13)
    w = ttk.Label(root, text="⠀").grid(row=14, column=14)
    w = ttk.Label(root, text="⠀").grid(row=15, column=15)
    w = ttk.Label(root, text="⠀").grid(row=16, column=16)

    menu_txt = ttk.Label(root, text="open you menu file")
    menu_txt.grid(row=2, column=menu_col)

    menu_filebutton = ttk.Button(root, text="open file", command=run_men)
    menu_filebutton.grid(row=4, column=menu_col)

    internat_txt = ttk.Label(root, text="open your internat file")
    internat_txt.grid(row=2, column=internat_col)

    internat_filebutton = ttk.Button(root, text="open file", command=run_inter)
    internat_filebutton.grid(row=4, column=internat_col)

    button = ttk.Button(root, text="Change theme!", command=change_theme)
    button.grid(row=16, column=3)

    root.mainloop()

overlay()