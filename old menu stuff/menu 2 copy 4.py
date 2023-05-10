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


s = menu
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

#print(lundi)

Platlist = ["potage", "plat1", "plat2", "accompagnement", "Légumes", "dessert"]
Platlista = ["potage", "Plat1", "Plat2", "Accompagnement", "légumes", "Dessert"]

number1 = 0
number1a = 0
limit1 = len(lundi)
limit1a = 5
argument1 = Platlist
argument1a = Platlista
lundi_txt = []
lundi_number = []
lim1 = limit1 - 1

while number1 < limit1:
        if number1a > limit1a:
            break
        else:       
            if lundi[number1] == argument1[number1a] or lundi[number1] == argument1a[number1a]:
                lundi_txt.append(argument1[number1a])
                lundi_number.append(number1)
                
                #print(lundi_txt, lundi_number)
    
                number1a += 1


            elif number1 > lim1:
                number1a += 1
                number1 -= 10
        #print(number1)

        number1 += 1


#print(" ")
#print((lundi_txt, lundi_number))
#print(" ")
#print(lundi)
#print(" ")

mardi_txt = []
mardi_number = []

number2 = 0
run_number = 0
indexnum = 0

a = ["potage", "plat1", "plat2", "accompagnement", "Legume", "dessert"]
b = ["potage", "Plat1", "Pat2", "Accompagnement", "Legumes", "Dessert", ""]


while number2 < len(mardi):
    while run_number < len(a):
        if mardi[indexnum] == a[run_number] or mardi[indexnum] == b[run_number]:
            
            mardi_txt.append(mardi[indexnum])

            mardi_number.append(indexnum)

            #print((mardi_txt, mardi_number))
            #print(run_number)
            #print(indexnum)
            
            indexnum = indexnum - indexnum
            indexnum += 1
            
            run_number += 1

            

        indexnum += 1
        number2 += 1
           
#print(mardi)
print("-----")

mercredi_txt = []
mercredi_number = []

number3 = 0
number3a = 0
number3b = 0
run_number2 = 0
indexnum2 = 0

aa = ["potage", "plat1", "plat2", "accompagnement", "Legume", "dessert"]
bb = ["potage", "Plat1", "Pat2", "Accompagnement", "Legumes", "Dessert"]

a = []
b = []

#print()
#print(mercredi)
#print()

la = len(aa)

#print((len(aa)))

#got lrblem heree

while number3b < la:
    #print("step 1")
    
    if number3a <= la:
        #print("step 2")
        #print(number3a)
        if aa[number3a] in mercredi or bb[number3a] in mercredi:
            #print("step 3")
            
            a.append(aa[number3a])
            b.append(bb[number3a])
        
            #print(number3a)
            #print(number3a)
            #print("a")
        
            number3a += 1
            #print(a)
            #print(b)
        
        
        else:

            number3a += 1
            
    number3b += 1
    



#print(a)
#print(b)

num1 = 1
lm = len(mercredi)
la = len(a) - num1

while number3 <= lm:
    while run_number2 <= la:
        #just for visualisation and debug

        #print(" ")
        #print("indexnum: ", indexnum2)
        #print("run number: ", run_number2)
        #print("len mercredi: ", len(mercredi))
        #print("len a: ", len(a), "len b: ", len(b))
        
        if mercredi[indexnum2] == a[run_number2] or mercredi[indexnum2] == b[run_number2]:
            
            mercredi_txt.append(mercredi[indexnum2])

            mercredi_number.append(indexnum2)

            #print(mercredi_txt, mercredi_number)
            #print(run_number2)
            #print(indexnum2)
            
            indexnum2 = indexnum2 - indexnum2
            indexnum2 += 1
            
            run_number2 += 1

        
        indexnum2 += 1
        number3 += 1
           
print(mercredi)
print()
print(mercredi_txt)
print()
print(mercredi_number)

jeudi_txt = []
jeudi_number = []

print("-----")
#ö
#print(jeudi)

number4 = 0
number4a = 0
number4b = 0
run_number4 = 0
indexnum4 = 0

aa4 = ["potage", "plat1", "plat2", "accompagnement", "Legume", "dessert"]
bb4 = ["potage", "Plat1", "Pat2", "Accompagnement", "Legumes", "Dessert"]

a4 = []
b4 = []

#print()
#print(mercredi)
#print()

la = len(aa4)

#print((len(aa)))

#got lrblem heree

while number4b < la:
    
    #print("step 1")
    
    if number4a <= la:
        #print("step 2")
        #print(number4a)
        if aa4[number4a] in jeudi or bb4[number4a] in jeudi:
            #print("step 3")
            
            a4.append(aa4[number4a])
            b4.append(bb4[number4a])
        
            #print(number4a)
            #print(number4a)
            #print("a")
        
            number4a += 1
            #print(a)
            #print(b)
        
        
        else:

            number4a += 1
            
    number4b += 1
    



#print(a)
#print(b)

num4 = 1
lj = len(jeudi)
la = len(a4) - num4

while number4 <= lj:
    while run_number4 <= la:
        #just for visualisation and debug

        #print(" ")
        #print("indexnum: ", indexnum2)
        #print("run number: ", run_number2)
        #print("len mercredi: ", len(mercredi))
        #print("len a: ", len(a), "len b: ", len(b))
        
        if jeudi[indexnum4] == a4[run_number4] or jeudi[indexnum4] == b4[run_number4]:
            
            jeudi_txt.append(jeudi[indexnum4])

            jeudi_number.append(indexnum4)

            #print(mercredi_txt, mercredi_number)
            #print(run_number2)
            #print(indexnum2)
            
            indexnum4 = indexnum4 - indexnum4
            indexnum4 += 1
            
            run_number4 += 1

        
        indexnum4 += 1
        number4 += 1
           
#print(jeudi)
print()
print(jeudi_txt)
print()
print(jeudi_number)

print("-----")
#ö
#print(vendredi)

vendredi_txt = []
vendredi_number = []

number5 = 0
number5a = 0
number5b = 0
run_number5 = 0
indexnum5 = 0

aa5 = ["potage", "plat1", "plat2", "accompagnement", "Legume", "dessert"]
bb5 = ["potage", "Plat1", "Pat2", "Accompagnement", "Legumes", "Dessert"]

a5 = []
b5 = []

#print()
#print(mercredi)
#print()

la = len(aa5)

#print((len(aa)))

while number5b < la:
    
    #print("step 1")
    
    if number5a <= la:
        #print("step 2")
        #print(number4a)
        if aa5[number5a] in vendredi or bb5[number5a] in vendredi:
            #print("step 3")
            
            a5.append(aa5[number5a])
            b5.append(bb5[number5a])
        
            #print(number4a)
            #print(number4a)
            #print("a")
        
            number5a += 1
            #print(a)
            #print(b)
        
        
        else:

            number5a += 1
            
    number5b += 1
    



#print(a)
#print(b)

num5 = 1
lv = len(vendredi)
la = len(a5) - num5

while number5 <= lv:
    while run_number5 <= la:
        #just for visualisation and debug

        #print(" ")
        #print("indexnum: ", indexnum2)
        #print("run number: ", run_number2)
        #print("len mercredi: ", len(mercredi))
        #print("len a: ", len(a), "len b: ", len(b))
        
        if vendredi[indexnum5] == a5[run_number5] or vendredi[indexnum5] == b4[run_number5]:
            
            vendredi_txt.append(vendredi[indexnum5])
            
            vendredi_number.append(indexnum5)

            #print(mercredi_txt, mercredi_number)
            #print(run_number2)
            #print(indexnum2)
            
            indexnum5 = indexnum5 - indexnum5
            indexnum5 += 1
            
            run_number5 += 1

        
        indexnum5 += 1
        number5 += 1
           
#print(jeudi)
print()
print(vendredi_txt)
print()
print(vendredi_number)

