import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import docx2txt
from ttkthemes import ThemedTk

def menu(menu1):
    # todo:
    # get menu days index DONE
    # get menu content DONE
    # split menu DONE
    # wrtie xml file DONE
    # create file name DONE
    # tested? YES
    # find a way to insert undertitles NOPE I DONT DO THIS
    # fix bugs DONE

    def check_input(input):
        daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
        dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
        number1 = 0
        while number1 < len(daylow):
            if daylow[number1] not in input and dayupper[number1] not in input:
                raise ValueError('Day not inclouded')
            else:
                number1 += 1

    def check_input2(input):
        platup = ["Plat 1", "Plat 2"]
        platdown = ["plat 1", "plat 2"]
        plat_correct = ["Plat1", "Plat2"]
        number1 = 0
        while number1 < len(platup):
            if platup[number1] in input:
                input.replace(platup[number1], plat_correct[number1])
            
            if platdown[number1] in input:
                input.replace(platup[number1], plat_correct[number1])

            else:
                pass
            number1 += 1
        


    check_input(menu1)
    check_input2(menu1)
    def wordsToList(strn):
        L = strn.split()
        cleanL = []
        abc1 = "abcdefghijklmnopqrstuvwxyz"
        abc = "ûéáœâà.,'ïäöüè()1234567890!" + abc1
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
        return(str1.join(s))
            

    s = menu1
    menu_list = wordsToList(s)


    def find_days(menus, menu_ind, arg):
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

    days = []
    days_index = []
    days = find_days(days, days_index, "2")

    def append_things(number1, number2, appendlist, origin):
        while number1 < number2:
            appendlist.append(origin[number1])
            number1 += 1
        return appendlist

    lundi = []
    mardi = []
    mercredi = []
    jeudi = []
    vendredi = []

    lundi = append_things(days[0], days[1], lundi, menu_list)
    mardi = append_things(days[1], days[2], mardi, menu_list)
    mercredi = append_things(days[2], days[3], mercredi, menu_list)
    jeudi = append_things(days[3], days[4], jeudi, menu_list)
    vendredi = append_things(days[4], len(menu_list), vendredi, menu_list)

    # these are the menus sorted by plats

    def find_plats(indicator, list_plats, index_plats):
        index_plats.clear()
        plat_down_tmpl = ["potage", "plat1", "plat2", "accompagnement", "Légumes", "dessert"]
        plat_up_tmpl = ["potage", "Plat1", "Plat2", "Accompagnement", "Légumes", "Dessert"]
        plats_final = ["potage", "plat 1", "plat 2", "accompagnement", "légumes", "dessert"]

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


    # for finding the plat and index in the list of menu

    lundi_plats = []
    lundi_plats_index = []

    mardi_plats = []
    mardi_plats_index = []

    mercredi_plats = []
    mercredi_plats_index = []

    jeudi_plats = []
    jeudi_plats_index = []

    vendredi_plats = []
    vendredi_plats_index = []

    lundi_plats = find_plats(lundi, lundi_plats, lundi_plats_index)
    mardi_plats = find_plats(mardi, mardi_plats, mardi_plats_index)
    mercredi_plats = find_plats(mercredi, mercredi_plats, mercredi_plats_index)
    jeudi_plats = find_plats(jeudi, jeudi_plats, jeudi_plats_index)
    vendredi_plats = find_plats(vendredi, vendredi_plats, vendredi_plats_index)

    # assign menus to slot

    def select_string(number1, number2, menuapp, jour):
        while number1 < number2:
            menuapp.append(jour[number1])
            number1 += 1
        return menuapp

    def show_date(number, app, jour):
        num1 = 0
        num2 = number[0]
        
        while num1 < num2:
            app.append(jour[num1])
            num1 += 1
        return app

    def splitslots(day, day_indexes, app1, app2, app3, app4, app5, app6):
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

            number1 += 1 

    lundi_date = []
    mardi_date = []
    mercredi_date = []
    jeudi_date = []
    vendredi_date = []

    lundi_slot1 = []
    lundi_slot2 = []
    lundi_slot3 = []
    lundi_slot4 = []
    lundi_slot5 = []
    lundi_slot6 = []

    mardi_slot1 = []
    mardi_slot2 = []
    mardi_slot3 = []
    mardi_slot4 = []
    mardi_slot5 = []
    mardi_slot6 = []

    mercredi_slot1 = []
    mercredi_slot2 = []
    mercredi_slot3 = []
    mercredi_slot4 = []
    mercredi_slot5 = []
    mercredi_slot6 = []

    jeudi_slot1 = []
    jeudi_slot2 = []
    jeudi_slot3 = []
    jeudi_slot4 = []
    jeudi_slot5 = []
    jeudi_slot6 = []

    vendredi_slot1 = []
    vendredi_slot2 = []
    vendredi_slot3 = []
    vendredi_slot4 = []
    vendredi_slot5 = []
    vendredi_slot6 = []

    lundi_date = show_date(lundi_plats_index, lundi_date, lundi)
    mardi_date = show_date(mardi_plats_index, mardi_date, mardi)
    mercredi_date = show_date(mercredi_plats_index, mercredi_date, mercredi)
    jeudi_date = show_date(jeudi_plats_index, jeudi_date, jeudi)
    vendredi_date = show_date(vendredi_plats_index, vendredi_date, vendredi)

    run_lundi = splitslots(lundi, lundi_plats_index, lundi_slot1, lundi_slot2, lundi_slot3, lundi_slot4, lundi_slot5, lundi_slot6)
    run_mardi = splitslots(mardi, mardi_plats_index, mardi_slot1, mardi_slot2, mardi_slot3, mardi_slot4, mardi_slot5, mardi_slot6)
    run_mercredi = splitslots(mercredi, mercredi_plats_index, mercredi_slot1, mercredi_slot2, mercredi_slot3, mercredi_slot4, mercredi_slot5, mercredi_slot6)
    run_mardi = splitslots(jeudi, jeudi_plats_index, jeudi_slot1, jeudi_slot2, jeudi_slot3, jeudi_slot4, jeudi_slot5, jeudi_slot6)
    run_mardi = splitslots(vendredi, vendredi_plats_index, vendredi_slot1, vendredi_slot2, vendredi_slot3, vendredi_slot4, vendredi_slot5, vendredi_slot6)

    def toxml(xml, day_plats, day_slot1, day_slot2, day_slot3, day_slot4, day_slot5, day_slot6):

        #to write the xml file, but in list form
        
        number1 = 0
        day_slots = [day_slot1, day_slot2, day_slot3, day_slot4, day_slot5, day_slot6]
        indexnum = len(day_plats)

        while number1 < indexnum:
            
            cache = []
            cache.clear()
            c = day_slots[number1]
            c.pop(0)
            cache = " ".join(str(x) for x in c)
            if not cache:
                pass
            else:
                mod1 = f"""
            <slot{number1}>
                <title>{day_plats[number1]}</title>
                <plat>{cache}</plat>  
                <undertitle></undertitle>
            </slot{number1}>\n"""    
            xml.append(mod1)
            number1 += 1

    def split(word):
        return [char for char in word]

    def month_string_to_number(string):
        m = {
            'janv': "01",
            'févr': "02",
            'mars': "03",
            'avri':"04",
            'mai':"05",
            'juin':"06",
            'juil':"07",
            'août':"08",
            'sept':"09",
            'octo':10,
            'nove':11,
            'déce':12
            }
        s = string.strip()[:4].lower()

        try:
            out = m[s]
            return out
        except:
            raise ValueError('Not a month')

    def create_file_name(day1):
        app = []
        year = time.strftime("%Y")
        year = year.lstrip("2")
        year = year.lstrip("0")
        print(year)
        month = day1[2]
        
        month = month_string_to_number(month)
        month = str(month)
        day = day1[1]
        if len(day) < 2:
            day = "0" + day
        app = year + month + day
        return app

    file_name = create_file_name(lundi_date)

    # file_name = 2199999999999
    lundi_xml = []
    mardi_xml = []
    mercredi_xml = []
    jeudi_xml = []
    vendredi_xml = []

    run_lundi = toxml(lundi_xml, lundi_plats, lundi_slot1, lundi_slot2, lundi_slot3, lundi_slot4, lundi_slot5, lundi_slot6)
    run_mardi = toxml(mardi_xml, mardi_plats, mardi_slot1, mardi_slot2, mardi_slot3, mardi_slot4, mardi_slot5, mardi_slot6)
    run_mercredi = toxml(mercredi_xml, mercredi_plats, mercredi_slot1, mercredi_slot2, mercredi_slot3, mercredi_slot4, mercredi_slot5, mercredi_slot6)
    run_jeudi = toxml(jeudi_xml, jeudi_plats, jeudi_slot1, jeudi_slot2, jeudi_slot3, jeudi_slot4, jeudi_slot5, jeudi_slot6)
    run_vendredi = toxml(vendredi_xml, vendredi_plats, vendredi_slot1, vendredi_slot2, vendredi_slot3, vendredi_slot4, vendredi_slot5, vendredi_slot6)

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

    run_xml = writexml(file_name, lundi_xml, mardi_xml, mercredi_xml, jeudi_xml, vendredi_xml, lundi_date, mardi_date, mercredi_date, jeudi_date, vendredi_date)
    print(file_name)
    print("Done")
    return file_name

root = ThemedTk(theme='elegance')
root.title('menu')
root.geometry("300x200")
print(root.get_themes())

def opfile():
    filetypes = (
        ('All files', '*.*'),
        ('word files', '*.docx'),
        ('text files', '*.txt')
    )

    root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a txt file", filetypes=filetypes)    

    fileroot = Label(root,text="origin file: " + root.filename)
    fname = root.filename

    fileroot.pack()
    if ".txt" in fname:    
        f = open(f"{root.filename}", "r")
        file_txt = f.read()

    elif ".docx" in fname:
        file_txt = docx2txt.process(fname)
    else:
        error = Label(root, text="file not compatible")
        error.pack()
        raise ValueError("file not compatible")
    
    men = menu(file_txt)

    placeholder3 = Label(root, text="")
    placeholder3.pack()
    label2 = Label(root, text="file name: " + men)
    label2.pack()

label1 = Label(root, text="select your file:").pack()

filebutton = Button(root, text="open file", command=opfile).pack()
root.mainloop()