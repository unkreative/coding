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
Legumes Chou rouge aux pommes 
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
Legumes Compote de pommes 
dessert Tarte aux myrtilles 

vendredi 26 novembre    	
potage Potage du jour 
plat1 Ragoût de marcassin 
plat2 Ragoût de tofu fumé 
accompagnement Spätzle
Legumes Carottes et navets
dessert Gâteau truffe 
"""

menu1 = """Lundi 15 novembre  

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
Legumes
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
Legumes
Blettes à l’ail 

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
    abc = "éáœâà.,'äöüè()1234567890!" + abc1
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
    elif (a < 0) and (b < 0) or (a > 0) and (b >= 0):  # fix: b >= 0 to cover case b == 0
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

print(dates_num)
print(dates_txt)
print()

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
    plat_down_tmpl = ["potage", "plat1", "plat2", "accompagnement", "Legume", "dessert"]
    plat_up_tmpl = ["potage", "Plat1", "Pat2", "Accompagnement", "Legumes", "Dessert"]
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

mmardi = list_filter(mardi, mardi_txt, mardi_number)

mmercredi = list_filter(mercredi, mercredi_txt, mercredi_number)

jjeudi = list_filter(jeudi, jeudi_txt, jeudi_number)

vvendredi = list_filter(vendredi, vendredi_txt, vendredi_number)

#print(lundi)
#print(mardi)
#print(mercredi)
#print(jeudi)
#print(vendredi)

#print(llundi)
#print(mmardi)
#print(mmercredi)
#print(jjeudi)
#print(vvendredi)

def format_string(jjour):
    while len(jjour) <= 6:
        jjour.append(" ")
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

print(llundi)
print(mmardi)
print(mmercredi)
print(jjeudi)
print(vvendredi)
print()

def select_string(number1, number2, menuapp, jour):
    while number1 < number2:
        menuapp.append(jour[number1])
        number1 += 1
    return menuapp


def split_date(jour, jour_week, jour_number):
    
    week_date = select_string(0, 3, jour_week, jour)
    
    return week_date

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


jour_week = []

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


print(lundi_number)

#datte = split_date(jour_week, lundi, lundi_number)

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


print(lundi_slot1)
print(lundi_slot2)
print(lundi_slot3)
print(lundi_slot4)
print(lundi_slot5)
print(lundi_slot6)
print()

print(mardi_slot1)
print(mardi_slot2)
print(mardi_slot3)
print(mardi_slot4)
print(mardi_slot5)
print(mardi_slot6)
print()

print(mercredi_slot1)
print(mercredi_slot2)
print(mercredi_slot3)
print(mercredi_slot4)
print(mercredi_slot5)
print(mercredi_slot6)
print()

print(jeudi_slot1)
print(jeudi_slot2)
print(jeudi_slot3)
print(jeudi_slot4)
print(jeudi_slot5)
print(jeudi_slot6)
print()

print(vendredi_slot1)
print(vendredi_slot2)
print(vendredi_slot3)
print(vendredi_slot4)
print(vendredi_slot5)
print(vendredi_slot6)

#print(datte)