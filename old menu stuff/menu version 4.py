import math

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
Rouleau à la confiture de myrtilles maison
"""
menu = """
Lundi 22 novembre  	
potage	Potage du jour
Plat 1	Spaghetti bolognaise 
plat 2	Spaghetti sauce végétarienne 
dessert 	Cake au yaourt 

Mardi 23 novembre      	
potage 	Potage du jour 
plat 1	Roulade de bœuf au jus lié 
	bœuf Galloway de Gallolux Lintgen 
plat 2	Galette de millet et de poireaux sauce curry 
accompagnement 	Riz de Camargue 
légumes 	Chou rouge aux pommes 
dessert	Verrine de pommes et pain d’épices 

mercredi 24 novembre   	
potage 	Potage du jour 
plat 1	Gratin de chicons 
plat 2	Roulées de poireaux et de choux
Accompagnement 	Purée de pommes de terre
dessert	Salade de fruits 

Jeudi 25 novembre  	
potage 	Potage du jour
plat 1	Gromperekichelcher
légumes 	Compote de pommes 
dessert	Tarte aux myrtilles 

vendredi 26 novembre    	
potage 	Potage du jour 
plat 1	Ragoût de marcassin 
plat 2	Ragoût de tofu fumé 
accompagnement 	Spätzle
légumes 	Carottes et navets
dessert 	Gâteau truffe 
"""

#menu = input("menu de cantine: ")

def wordsToList(strn):
    L = strn.split()
    cleanL = []
    abc1 = "abcdefghijklmnopqrstuvwxyz"
    abc = "éáœâà.,'è()1234567890!" + abc1
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
        #print("done")
        break
    else:
        if menu_list[nmbr] == daylow[nmbr2] or menu_list[nmbr] == dayupper[nmbr2]:
            dates_txt.append(argument1[nmbr2])
            dates_num.append(nmbr)

            nmbr2 += 1

        nmbr += 1

#print(dates_txt)
#print(dates_num)

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

print(vendredi)
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
    
    print(plat_down)
    print(plat_up)
    
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
    return jour_txt, jour_number

    
vndredi = list_filter(vendredi, vendredi_txt, vendredi_number)
print(vndredi)
print(vendredi_txt)
print(vendredi_number)
