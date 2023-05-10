#fonktioneiert um ipad net
#todo:
#filter first item out dslot[number1] (line 104)
#add day and close <>
print("Lol")
date = "Lundi 22 novembre"

days = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']

lundi_plats = ['potage', 'Plat1', 'plat2', 'dessert', '', '', '']
mardi_plats = ['potage', 'plat1', 'plat2', 'accompagnement', 'Dessert', '', '']
mercredi_plats = ['potage', 'plat1', 'plat2', 'Accompagnement', '', '']
jeudi_plats = ['potage', 'plat1', 'plat2', 'accompagnement', 'dessert', '', '']
vendredi_plats = ['potage', 'plat1', 'plat2', 'dessert', '', '', '']

lslot1 = ['potage', 'Potage', 'du', 'jour']
lslot2 = ['Plat1', 'Gratin', 'de', 'macaroni', 'à', 'la', 'dinde', 'Dindes', 'du', 'Haff', 'a', 'Sewen', 'Meispelt']
lslot3 = ['plat2', 'Gratin', 'de', 'macaroni', 'aux', 'légumes']
lslot4 = ['dessert', 'Brownie']
lslot5 = [""]
lslot6 = [""]

maslot1 = ['potage', 'Potage', 'du', 'jour']
maslot2 = ['plat1', 'Potaufeu', 'de', 'bœuf', 'bœuf', '(Galloway)', 'cuit', 'dans', 'son', 'bouillon', 'avec', 'des', 'légumes']
maslot3 = ['plat2', 'Potaufeu', 'végétarien']
maslot4 = ['accompagnement', 'Pommes', 'de', 'terre', 'nature']
maslot5 = ['Dessert', 'Muffin', 'à', 'la', 'vanille']
maslot6 = [""]

meslot1 = ['potage', 'Potage', 'du', 'jour']
meslot2 = ['plat1', 'Curry', 'aux', 'lentilles']
meslot3 = ['plat2', 'Quinoa', 'à', 'la', 'fondue', 'de', 'poireaux']
meslot4 = ['Accompagnement', 'Tortillas', 'bio']
meslot5 = [""]
meslot6 = [""]

jslot1 = ['potage', 'Potage', 'du', 'jour']
jslot2 = ['plat1', 'Quenelles', 'de', 'brochet', 'sauce', 'Nantua', 'sauce', 'à', 'base', 'de', 'crustacés']
jslot3 = ['plat2', 'Steak', 'de', 'choufleur', 'sauce', 'Aurore', 'sauce', 'tomatée']
jslot4 = ['accompagnement', 'Riz', 'de', 'Camargue']
jslot5 = ['dessert', 'Tiramisu']
jslot6 = []

vslot1 = ['potage', 'Potage', 'du', 'jour']
vslot2 = ['plat1', 'Pizza', 'Margherita']
vslot3 = ['plat2', 'Pizza', 'Béchamel', 'et', 'légumes', 'Champignons,', 'poireaux', 'et', 'carottes']
vslot4 = ['dessert', 'Rouleau', 'à', 'la', 'confiture', 'de', 'myrtilles', 'maison']
vslot5 = [""]
vslot6 = [""]

def toxml(date, day, dslot1, dslot2, dslot3, dslot4, dslot5, dslot6, jour_plats):
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
                #print(cache[x])
                cache1 = cache1 + " " + cache[x]
                #print(cache1)
            
            mod1 = f"""
        <slot{numbe1}>
            <title>{jour_plats[numbe1]}</title>
            <plat>{cache1}</plat>  
            <undertitle>allérgenes</undertitle>
        </slot{numbe1}>"""    
            fa.write(mod1)
            print(mod1)

        numbe1 += 1
    if f"""</{day}>""" not in file:
        fa.write(f"\n  </{day}>\n")

    fa.close()
    fr.close()

dte = 2119999999999999999999999



lundi_ = toxml(dte, "lundi", lslot1, lslot2, lslot3, lslot4, lslot5, lslot6, lundi_plats)
mardi_ = toxml(dte, "mardi", maslot1, maslot2, maslot3, maslot4, maslot5, maslot6, mardi_plats)
mercredi_ = toxml(dte, "mercredi", meslot1, meslot2, meslot3, meslot4, meslot5, meslot6, mercredi_plats)
jeudi_ = toxml(dte, "jeudi", jslot1, jslot2, jslot3, jslot4, jslot5, jslot6, jeudi_plats)
vendredi_ = toxml(dte, "vendredi", vslot1, vslot2, vslot3, vslot4, vslot5, vslot6, vendredi_plats)

fr = open(f"{dte}.txt", "r")

file = fr.read()

fa = open(f"{dte}.txt", "a")

if """</menu>""" not in file:
    fa.write("</menu>\n")

fa.close()
fr.close()

print(lundi_)
#close <> function