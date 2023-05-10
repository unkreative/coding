# todo:
# get menu days index DONE
# get menu content 

menu1 = """
Lundi 22 novembre  	
potage 	Potage du jour
Plat1 Spaghetti bolognaise 
plat2 	Spaghetti sauce végétarienne 
dessert 	Cake au yaourt 

Mardi 23 novembre      	
potage Potage du jour 
plat1 Roulade de bœuf au jus lié 
	bœuf Galloway de Gallolux Lintgen 
plat2 Galette de millet et de poireaux sauce curry 
accompagnement Riz de Camargue 
Légumes Chou rouge aux pommes 
dessert Verrine de pommes et pain d’épices 

Mercredi 24 novembre   	
potage Potage du jour 
plat1 Gratin de chicons 
plat2 Roulées de poireaux et de choux
Accompagnement 	Purée de pommes de terre
dessert Salade de fruits 

Jeudi 25 novembre  	
potage Potage du jour
plat1 Gromperekichelcher
Légumes Compote de pommes 
dessert Tarte aux myrtilles 

Vendredi 26 novembre    	
potage Potage du jour 
plat1 Ragoût de marcassin 
plat2 Ragoût de tofu fumé 
accompagnement Spätzle
Legumes Carottes et navets
dessert Gâteau truffe 

"""


# menu = input("menu de cantine: ")

def wordsToList(strn):
    L = strn.split()
    cleanL = []
    abc1 = "abcdefghijklmnopqrstuvwxyz"
    abc = "ûéáœâà.,'äöüè()1234567890!" + abc1
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

s = menu1
menu_list = wordsToList(s)


def find_days(menus, menu_ind, arg):
    daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

    number1 = 0
    number2 = 0

    len_menu = len(daylow)
    print(len_menu)

    while number2 <= len_menu:
        if daylow[number2] in menu_list or dayupper[number2] in menu_list:
            print("daylow num: ", daylow[number2])
            print("menus: ", menus)

            menus.append(daylow[number2])

            print(menus)

            id = dayupper[number2]

            indexx = menu_list.index(id)
            print(indexx)
            menu_ind.append(indexx)
            print(menu_ind)
            print("nmber2: ", number2)

            number2 += 1

            if number2 == len_menu:
                print("aha")
                break

    print("number1: ", number1)

    # print(menus)
    # print(menu_ind)
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
    plat_down_tmpl = ["potage", "plat1", "plat2", "accompagnement", "Légume", "dessert"]
    plat_up_tmpl = ["potage", "Plat1", "Pat2", "Accompagnement", "Légumes", "Dessert"]

    number2 = 0
    plat_len = len(plat_down_tmpl)

    while number2 < plat_len: 
        if plat_down_tmpl[number2] in indicator or plat_up_tmpl[number2] in indicator:

            list_plats.append(plat_down_tmpl[number2])

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
    appendd = (app1, app2, app3, app4, app5, app6)
    len_index = len(day_indexes)
    number1 = 0
    day_indexes.append(len(day))
    n1 = 1
    print("index: ", len_index)
    while number1 < len_index:
        number2 = number1 + n1

        if number1 == 0:
            app1 = select_string(day_indexes[number1], day_indexes[number2], app1, day)
            # print(app1)

        if number1 == 1:
            app2 = select_string(day_indexes[number1], day_indexes[number2], app2, day)
            # print(app2)

        if number1 == 2:
            app3 = select_string(day_indexes[number1], day_indexes[number2], app3, day)
            # print(app3)
        
        if number1 == 3:
            app4 = select_string(day_indexes[number1], day_indexes[number2], app4, day)
            # print(app4)

        if number1 == 4:
            app5 = select_string(day_indexes[number1], day_indexes[number2], app5, day)
            # print(app5)

        if number1 == 5:
            app6 = select_string(day_indexes[number1], day_indexes[number2], app6, day)
            # print(app6)

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
