import math

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
dessert Verrine de pommes et pain d’épices 

mercredi 24 novembre   	
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

vendredi 26 novembre    	
potage Potage du jour 
plat1 Ragoût de marcassin 
plat2 Ragoût de tofu fumé 
accompagnement Spätzle
Légumes Carottes et navets
dessert Gâteau truffe 

"""

menu = """Lundi 15 novembre  

potage
Potage du jour 
Plat1
Gratin de macaroni à la dinde 

Dindes du Haff a Sewen Meispelt
plat2
Gratin de macaroni aux légumes 
dessert 
Brownie 

Mardi 16 novembre      

potage 
Potage du jour 
plat1
Pot-au-feu de bœuf 

bœuf (Galloway) cuit dans son bouillon avec des légumes 
plat2
Pot-au-feu végétarien 
accompagnement 
Pommes de terre nature 
Légumes
pommes de terre de la variété Linda, à chair ferme
des
Carottes, navets et chou 
Dessert
Muffin à la vanille 

mercredi 17 novembre   

potage 
Potage du jour
plat1
Curry aux lentilles
plat2
Quinoa à la fondue de poireaux 
Accompagnement 
Tortillas bio 
dessert
Salade de fruits

Jeudi 18 novembre  

potage 
Potage du jour 
plat1
Quenelles de brochet sauce Nantua

sauce à base de crustacés
plat2
Steak de chou-fleur sauce Aurore

sauce tomatée
accompagnement 
Riz de Camargue 
Légume  Blettes à l’ail 
blette = Mangold
dessert
Tiramisu

Vendredi 19 novembre 

potage 
Potage du jour 
plat1
Pizza Margherita
plat2
Pizza Béchamel et légumes

Champignons, poireaux et carottes
dessert 
Rouleau à la confiture de myrtilles maison """

#menu = input("menu de cantine: ")

def wordsToList(strn):
    L = strn.split()
    cleanL = []
    abc1 = "abcdefghijklmnopqrstuvwxyz"
    abc = "éáœâà.,’=û^'äöüè()1234567890!" + abc1
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

daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

nmbr = 0
nmbr2 = 0
limit1 = len(menu_list)
limit2 = 5
dates_num = []
dates_txt = []
argument1 = daylow
argument2 = dayupper

while nmbr <= limit1:
    if nmbr2 >= limit2:
        break
    else:
        if menu_list[nmbr] == daylow[nmbr2] or menu_list[nmbr] == dayupper[nmbr2]:
            dates_txt.append(argument1[nmbr2])
            dates_num.append(nmbr)

            nmbr2 += 1

        nmbr += 1

lundi = dates_txt[0]
mardi = dates_txt[1]
mercredi = dates_txt[2]
jeudi = dates_txt[3]
vendredi = dates_txt[4]

lundi = wordsToList(lundi)
mardi = wordsToList(mardi)
mercedi = wordsToList(mercredi)
jeudi = wordsToList(jeudi)
vendredi = wordsToList(vendredi)

def distance(a, b):
    if (a == b):
        return 0
    elif (a < 0) and (b < 0) or (a > 0) and (b >= 0):
        if (a < b):
            return (abs(abs(a) - abs(b)))
        else:
            return -(abs(abs(a) - abs(b)))
    else:
        return math.copysign((abs(a) + abs(b)), b)

n1 = dates_num[0]
n2 = dates_num[1]
n3 = dates_num[2]
n4 = dates_num[3]
n5 = dates_num[4]

number1 = 0
number2 = n2
number3 = n3
number4 = n4
number5 = n5

lundi = []
mardi = []
mercredi = []
jeudi = []
vendredi = []

while number1 < n2:
    lundi.append(menu_list[number1])
    number1 += 1
    
while number2 < n3:
    mardi.append(menu_list[number2])
    number2 += 1

while number3 < n4:
    mercredi.append(menu_list[number3])
    number3 += 1

while number4 < n5:
    jeudi.append(menu_list[number4])
    number4 += 1

while number5 < len(menu_list):
    vendredi.append(menu_list[number5])
    number5 += 1


lundi_txt = []
lundi_number = []

mardi_txt = []
mardi_number = []

mercredi_txt = []
mercredi_number = []

jeudi_txt = []
jeudi_number = []

vendredi_txt = []
vendredi_number = []
    
def list_filter(jour, jour_txt, jour_number):
    plat_ind = 0
    while_stopper = 0
    plat_down_tmpl = ["potage", "plat1", "plat2", "accompagnement", "Légumes", "dessert"]
    plat_up_tmpl = ["potage", "Plat1", "Pat2", "Accompagnement", "Légumes", "Dessert"]
    plat_down = []
    plat_up = []
    
    len_plat = len(plat_down_tmpl)

    #filter which menus are in the list

    while while_stopper < len_plat:
        
        if plat_ind <= len_plat:
            
            if plat_down_tmpl[plat_ind] in jour or plat_up_tmpl[plat_ind] in jour:

                plat_down.append(plat_down_tmpl[plat_ind])
                plat_up.append(plat_up_tmpl[plat_ind])

                plat_ind += 1
            
            else:
                plat_ind += 1
        
        while_stopper += 1
    
    while_stopper = 0
    run_number = 0
    indexnumber = 0
    len_jour = len(jour)
    number = 1
    len_plat = len(plat_down) - number

    #get the details of the plats
    while while_stopper <= len_jour:
        while run_number <= len_plat:
            if jour[indexnumber] == plat_down[run_number] or jour[indexnumber] == plat_up[run_number]:
                jour_txt.append(jour[indexnumber])
                jour_number.append(indexnumber)
                indexnumber = 0
                run_number += 1
            indexnumber += 1
            while_stopper += 1
    return jour_txt
    

llundi = list_filter(lundi, lundi_txt, lundi_number)
print(llundi)
mmardi = list_filter(mardi, mardi_txt, mardi_number)
print(mmardi)
mmercredi = list_filter(mercredi, mercredi_txt, mercredi_number)

jjeudi = list_filter(jeudi, jeudi_txt, jeudi_number)

vvendredi = list_filter(vendredi, vendredi_txt, vendredi_number)

def format_string(jjour):
    while len(jjour) <= 6:
        jjour.append("")
    return jjour

def format_number(jour_number, jour):
    stopper = True
    
    if stopper == True:
        jour_number.append(len(jour))
        stopper = False
        
    while len(jour_number) <= 6:
        jour_number.append(len(jour))
    return jour_number

llundi = format_string(llundi)
mmardi = format_string(mmardi)
mmercredi = format_string(mmercredi)
jjeudi = format_string(jjeudi)
vvendredi = format_string(vvendredi)

lundi_number = format_number(lundi_number, lundi)
mardi_number = format_number(mardi_number, mardi)
mercredi_number = format_number(mercredi_number, mercredi)
jeudi_number = format_number(jeudi_number, jeudi)
vendredi_number = format_number(vendredi_number, vendredi)

def select_string(number1, number2, menuapp, jour):
    while number1 < number2:
        menuapp.append(jour[number1])
        number1 += 1
    return menuapp
    
    return week_date

def show_date(number, app, jour):
    num1 = 0
    num2 = number[0]
    
    while num1 < num2:
        app.append(jour[num1])
        num1 += 1
    return app

def split_slot1(jour, jour_number, jour_slot1):
    
    jour_slot1 = select_string(jour_number[0], jour_number[1], jour_slot1, jour)

    return jour_slot1

def split_slot2(jour, jour_number, jour_slot2):
    
    jour_slot2 = select_string(jour_number[1], jour_number[2], jour_slot2, jour)

    return jour_slot2

def split_slot3(jour, jour_number, jour_slot3):
    
    jour_slot3 = select_string(jour_number[2], jour_number[3], jour_slot3, jour)

    return jour_slot3

def split_slot4(jour, jour_number, jour_slot4):
    
    jour_slot4 = select_string(jour_number[3], jour_number[4], jour_slot4, jour)

    return jour_slot4

def split_slot5(jour, jour_number, jour_slot5):
    
    jour_slot5 = select_string(jour_number[4], jour_number[5], jour_slot5, jour)

    return jour_slot5

def split_slot5(jour, jour_number, jour_slot5):
    
    jour_slot5 = select_string(jour_number[5], jour_number[6], jour_slot5, jour)

    return jour_slot5

def split_slot6(jour, jour_number, jour_slot6):
    
    ljour = len(jour)
    
    jour_slot6 = select_string(jour_number[6], ljour, jour_slot6, jour)

    return jour_slot6

lundi_date = []
lundi_slot1 = []
lundi_slot2 = []
lundi_slot3 = []
lundi_slot4 = []
lundi_slot5 = []
lundi_slot6 = []

mardi_date = []
mardi_slot1 = []
mardi_slot2 = []
mardi_slot3 = []
mardi_slot4 = []
mardi_slot5 = []
mardi_slot6 = []

mercredi_date = []
mercredi_slot1 = []
mercredi_slot2 = []
mercredi_slot3 = []
mercredi_slot4 = []
mercredi_slot5 = []
mercredi_slot6 = []

jeudi_date = []
jeudi_slot1 = []
jeudi_slot2 = []
jeudi_slot3 = []
jeudi_slot4 = []
jeudi_slot5 = []
jeudi_slot6 = []

vendredi_date = []
vendredi_slot1 = []
vendredi_slot2 = []
vendredi_slot3 = []
vendredi_slot4 = []
vendredi_slot5 = []
vendredi_slot6 = []

lundi_date = show_date(lundi_number, lundi_date, lundi)
mardi_date = show_date(mardi_number, mardi_date, mardi)
mercredi_date = show_date(mercredi_number, mercredi_date, mercredi)
jeudi_date = show_date(jeudi_number, jeudi_date, jeudi)
vendredi_date = show_date(vendredi_number, vendredi_date, vendredi)

lundi_slot1 = split_slot1(lundi, lundi_number, lundi_slot1)
lundi_slot2 = split_slot2(lundi, lundi_number, lundi_slot2)
lundi_slot3 = split_slot3(lundi, lundi_number, lundi_slot3)
lundi_slot4 = split_slot4(lundi, lundi_number, lundi_slot4)
lundi_slot5 = split_slot5(lundi, lundi_number, lundi_slot5)
lundi_slot6 = split_slot6(lundi, lundi_number, lundi_slot6)

mardi_slot1 = split_slot1(mardi, mardi_number, mardi_slot1)
mardi_slot2 = split_slot2(mardi, mardi_number, mardi_slot2)
mardi_slot3 = split_slot3(mardi, mardi_number, mardi_slot3)
mardi_slot4 = split_slot4(mardi, mardi_number, mardi_slot4)
mardi_slot5 = split_slot5(mardi, mardi_number, mardi_slot5)
mardi_slot6 = split_slot6(mardi, mardi_number, mardi_slot6)

mercredi_slot1 = split_slot1(mercredi, mercredi_number, mercredi_slot1)
mercredi_slot2 = split_slot2(mercredi, mercredi_number, mercredi_slot2)
mercredi_slot3 = split_slot3(mercredi, mercredi_number, mercredi_slot3)
mercredi_slot4 = split_slot4(mercredi, mercredi_number, mercredi_slot4)
mercredi_slot5 = split_slot5(mercredi, mercredi_number, mercredi_slot5)
mercredi_slot6 = split_slot6(mercredi, mercredi_number, mercredi_slot6)

print(jeudi_number)
print(jeudi)
jeudi_slot1 = split_slot1(jeudi, jeudi_number, jeudi_slot1)
jeudi_slot2 = split_slot2(jeudi, jeudi_number, jeudi_slot2)
jeudi_slot3 = split_slot3(jeudi, jeudi_number, jeudi_slot3)
jeudi_slot4 = split_slot4(jeudi, jeudi_number, jeudi_slot4)
jeudi_slot5 = split_slot5(jeudi, jeudi_number, jeudi_slot5)
jeudi_slot6 = split_slot6(jeudi, jeudi_number, jeudi_slot6)

vendredi_slot1 = split_slot1(vendredi, vendredi_number, vendredi_slot1)
vendredi_slot2 = split_slot2(vendredi, vendredi_number, vendredi_slot2)
vendredi_slot3 = split_slot3(vendredi, vendredi_number, vendredi_slot3)
vendredi_slot4 = split_slot4(vendredi, vendredi_number, vendredi_slot4)
vendredi_slot5 = split_slot5(vendredi, vendredi_number, vendredi_slot5)
vendredi_slot6 = split_slot6(vendredi, vendredi_number, vendredi_slot6)


#filter first item out dslot[number1] (line 104)
#add day and close <>
print("Lol")
date = "Lundi 22 novembre"

days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']

lundi_plats = llundi
print(lundi_plats)
print(llundi)
mardi_plats = mmardi
print(mmardi)
mercredi_plats = mmercredi
jeudi_plats = mmercredi
vendredi_plats = vvendredi


def toxml(date, day, dslot1, dslot2, dslot3, dslot4, dslot5, dslot6, jour_plats):
    print(jour_plats)
    if not len(day):
        print("l")
        return

    fa = open(f"{date}.txt", "a")
    fr = open(f"{date}.txt", "r")

    file = fr.read()

    if """<?xml version="1.0" encoding="UTF-8"?>""" not in file:
        fa.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
    
    n1 = 1
    lplat = len(jour_plats) - n1
    number1 = 0
    indexnum = 0
    print(lplat)
    while number1 <= lplat:
        if jour_plats[number1] != "":
            indexnum += 1
        number1 += 1
    #includ day thing
    #indexnum = times it has to run

    if """<menu>""" not in file:
        fa.write("<menu>\n")
    
    if f"""<{day}>""" not in file:
        fa.write(f"  <{day}>\n")
    
    dslot = (dslot1, dslot2, dslot3, dslot4, dslot5, dslot6)
    #print(dslot)
    numbe1 = 0
    print(indexnum, "indexnum")

    while numbe1 < indexnum:
        cache1 = ""
        cache = dslot[numbe1]
        if not cache:
            print("ne")
            pass
        else:
            cache.pop(0)
            for x in range(len(cache)):
                #print(cache)
                cache1 = cache1 + " " + cache[x]
            
            mod1 = f"""
        <slot{numbe1}>
            <title>{jour_plats[numbe1]}</title>
            <plat>{cache1[1:]}</plat>  
            <undertitle></undertitle>
        </slot{numbe1}>"""   
            fa.write(mod1)
            # print(mod1)

        numbe1 += 1
    if f"""</{day}>""" not in file:
        fa.write(f"\n  </{day}>\n")

    fa.close()
    fr.close()

file_name = 21199999999999999999999999999999999999



lundi_ = toxml(file_name, "lundi", lundi_slot1, lundi_slot2, lundi_slot3, lundi_slot4, lundi_slot5, lundi_slot6, lundi_plats)
mardi_ = toxml(file_name, "mardi", mardi_slot1, mardi_slot2, mardi_slot3, mardi_slot4, mardi_slot5, mardi_slot6, mardi_plats)
mercredi_ = toxml(file_name, "mercredi", mercredi_slot1, mercredi_slot2, mercredi_slot3, mercredi_slot4, mercredi_slot5, mercredi_slot6, mercredi_plats)
jeudi_ = toxml(file_name, "jeudi", jeudi_slot1, jeudi_slot2, jeudi_slot3, jeudi_slot4, jeudi_slot5, jeudi_slot6, jeudi_plats)
vendredi_ = toxml(file_name, "vendredi", vendredi_slot1, vendredi_slot2, vendredi_slot3, vendredi_slot4, vendredi_slot5, vendredi_slot6, vendredi_plats)

fr = open(f"{file_name}.txt", "r")

file = fr.read()

fa = open(f"{file_name}.txt", "a")

if """</menu>""" not in file:
    fa.write("</menu>\n")

fa.close()
fr.close()

print(lundi_, mardi_, mercredi_, jeudi_, vendredi_)
#close <> function