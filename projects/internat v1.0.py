import docx2txt
import re
import time
from datetime import timedelta
from datetime import date

internat_file_lou = '/Users/lousergonne/Downloads/220321 menus internat.docx'
input = docx2txt.process(internat_file_lou)

def get_year():
    todays_date = date.today()
    year = todays_date.year
    month = todays_date.month
    day = todays_date.day

    if month == 12 and day >= 13:
        year = year + 1
    return year



def check_input(input):
    daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    number1 = 0
    while number1 < len(daylow):
        if daylow[number1] not in input and dayupper[number1] not in input:
            raise ValueError('Day not inclouded')
        else:
            number1 += 1

    
        return input

def wordsToList(strn):
    L = strn.split()
    cleanL = []
    abc1 = "abcdefghijklmnopqrstuvwxyzâôûéáœâàëöÿç"
    abc = "=:;«»’°\n|'ïäöüè/%+^¨&<>§ëöÿÏÖÜË('^)1234567890!-_" + abc1
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
def append_things(number1, number2, appendlist, origin):
    while number1 < number2:
        appendlist.append(origin[number1])
        number1 += 1
    return appendlist
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


def find_plats(indicator, list_plats, index_plats):
    global id
    index_plats.clear()
    plat_down_tmpl = ["\npotage", "\nsubtitle_potage", "\nplat1", "\nsubtitle_plat1", "\nplat2", "\nsubtitle_plat2",
                      "\naccompagnement", "\nsubtitle_accompagnement", "\nLégumes", "\nsubtitle_légumes", "\ndessert",
                      "subtitle_dessert"]
    plat_up_tmpl = ["potage", "Subtitle_potage", "Plat1", "Subtitle_plat1", "Plat2", "Subtitle_plat2", "Accompagnement",
                    "Subtitle_accompagnement", "Légumes", "Subtitle_légumes", "Dessert", "Subtitle_dessert"]
    plats_final = ["\npotage", "\nSubtitle_potage", "\nplat 1", "\nSubtitle_plat1", "\nplat 2", "\nSubtitle_plat2",
                   "\naccompagnement", "\nSubtitle_accompagnement", "\nlégumes", "\nSubtitle_légumes", "\ndessert",
                   "\nSubtitle_dessert"]

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

def select_string(number1, number2, menuapp, jour):
    while number1 < number2:
        menuapp.append(jour[number1])
        number1 += 1
    return menuapp

def check_input4(input):
    input = str(input)

    if input.count("&") > 0:
        input = input.replace("&", "&amp;")
    
    if input.count("<") > 0:
        input = input.replace("<", "&lt;")

    if input.count(">") > 0:
        input = input.replace(">", "&gt;")
    return input
 





def cleanup(day1, day2, day3, day4):
    replace = ["potage","Potage", "plat1", "Plat1", "plat2","Plat2", "accompagnement", "Accompagnement","légumes", "Légumes", "dessert", "Dessert", "subtitle_potage","Subtitle_potage", "subtitle_plat1", "Subtitle_plat1", "subtitle_plat2",  "Subtitle_plat2",  "subtitle_accompagnement", "Subtitle_accompagnement", "subtitle_légumes","Subtitle_légumes", "subtitle_dessert", "Subtitle_dessert", "Subtitle_"]
    days = [day1, day2, day3, day4]
    for x in days:
        for y in replace:
            if y in x:
                x.remove(y)
            else:
                pass



def writexml(file_name, xml, date):
    fwrite = open(f"{file_name}.xml", "a")

    fwrite.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
    fwrite.write("""<internats_menu>\n""")


    number1 = 0
    while number1 < 4:

        fwrite.write(f"""       <date>{date}</date>""")
        fwrite.write(f"{xml[number1]}")

        number1 += 1
    fwrite.write("""</internats_menu>\n""")
    fwrite.close()




def internats_menu(input):
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
    filename = f"{internat_day1}-{internat_day2}-internat"
    final_month = f"menu du {internat_day1} au {internat_day2} {internat_month} {year}"

    cleanup(internat_lundi, internat_mardi, internat_mercredi, internat_jeudi)

    days = [internat_lundi, internat_mardi, internat_mercredi, internat_jeudi]
    ndays  = ["lundi", "mardi", "mercredi", "jeudi"]
    num1 = 0
    xml =  []
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
            xx =  str(day[num5])
            uppercase = xx[0].isupper()
            if uppercase == False:
                pass
            else:
                day[num5] = f"\n{xx}"
            num5 += 1

        cache  = ' '.join([str(item) for item in day])

        print("cache: ", cache)

        module2 = f"""
        <slot{num1}>
            <title>{nday}</title>
            <plat>{cache}</plat>
        </slot{num1}>\n"""

        print(module2)
        xml.append(module2)
        num1  += 1

    writexml(filename, xml, final_month)

internats_menu(input)

