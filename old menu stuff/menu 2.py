import math

m = """Lundi 15 novembre  

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

pommes de terre de la variété Linda, à chair ferme
des
Carottes, navets et chou 
dessert
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


# menu = input("menu de cantine: ")

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


s = m
menu_list = wordsToList(s)

L = menu_list

lenn = len(menu_list)
l_num = []
l_txt = []

daylow = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
dayupper = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

nmbr = 0
nmbr2 = 0
limit1 = lenn
limit2 = 5
list_num = []
list_txt = []
argument1 = daylow
argument2 = dayupper

while nmbr <= limit1:
    if nmbr2 >= limit2:
        print("done")
        break
    else:
        if L[nmbr] == argument1[nmbr2] or L[nmbr] == argument2[nmbr2]:
            list_txt.append(argument1[nmbr2])
            list_num.append(nmbr)

            nmbr2 += 1

        nmbr += 1

print(list_txt)
print(list_num)

lundi = list_txt[0]
mardi = list_txt[1]
mercredi = list_txt[2]
jeudi = list_txt[3]
vendredi = list_txt[4]

#print("l", lundi, "l")

lsplit = wordsToList(lundi)

masplit = wordsToList(mardi)
mesplit = wordsToList(mercredi)
jesplit = wordsToList(jeudi)
vsplit = wordsToList(vendredi)


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


n1 = list_num[0]
n2 = list_num[1]
n3 = list_num[2]
n4 = list_num[3]
n5 = list_num[4]

nbr1 = 0
nbr2 = n2
nbr3 = n3
nbr4 = n4
nbr5 = n5

lundi = []
mardi = []
mercredi = []
jeudi = []
vendredi = []

while nbr1 < n2:
    lundi.append(L[nbr1])
    nbr1 += 1
    

while nbr2 < n3:
    mardi.append(L[nbr2])
    nbr2 += 1

while nbr3 < n4:
    mercredi.append(L[nbr3])
    nbr3 += 1

while nbr4 < n5:
    jeudi.append(L[nbr4])
    nbr4 += 1

while nbr5 < lenn:
    vendredi.append(L[nbr5])
    nbr5 += 1

vl = len(lundi)
vma = len(mardi)
vme = len(mercredi)
vj = len(jeudi)
vv = len(vendredi)

#print(lundi)

Platlist = ["potage", "plat1", "plat2", "accompagnement", "legumes", "dessert"]
Platlista = ["potage", "Plat1", "Plat2", "Accompagnement", "des", "Dessert"]

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


            elif number1 >= lim1:
                number1a += 1
                number1 -= 10
        #print(number1)

        number1 += 1


print(" ")
print(lundi_txt, lundi_number)
print(" ")
print(lundi)
print(" ")

number2 = 0
number2a = 0
limit2 = len(mardi)
print(limit2)
limit2a = 6
argument2 = Platlist
argument2a = Platlista
mardi_txt = []
mardi_number = []

lim2 = limit2 - 1

times_run = 0

while number2 < limit2:
        if times_run >= limit2a:
            print("not done")
            break

        else:       
            if mardi[number2] == Platlist[number2a] or mardi[number1] == Platlista[number2a]:
                mardi_txt.append(Platlista[number2a])
                mardi_number.append(number2)
                
                print(mardi_txt, mardi_number)
                #print(number2a)
                #print(times_run)
                times_run += 1
            
                lenlist = len(mardi_txt)
                print(lenlist)
                
                number2a += 1

            elif len(mardi_txt) < limit2:
                number2 += 1
                
            else:
                number2a
                
                times_run += 1
                
                number2 += 1
                
                number2 -= limit2
        
        #print(number2)



print(" ")
print(mardi_txt, mardi_number)
print(" ")
print(mardi)
print(" ")
print(" ")
