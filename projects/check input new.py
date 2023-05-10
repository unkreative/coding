from operator import le
import re

text = """

Lundi 17 janvier

potage
Potage du jour
subtitle_potage

plat1 
Ragoût de jeune bovin aux carottes 
Subtitle_plat1
Biohaff Baltes Stegen
plat2 
Subtitle_plat2
Ragoût de tofu fumé aux carottes
accompagnement 
Boulgour
Subtitle_accompagnement

dessert  
Gâteau aux noix
Subtitle_dessert


Mardi 18 janvier 
potage
Potage du jour
subtitle_potage

plat1 
Chili con carne 
Subtitle_plat1

plat2 
Chili sin carne
Subtitle_plat2

accompagnement 
Riz de Camargue 
Subtitle_accompagnement

dessert 
Fruits  
Subtitle_dessert

Mercredi  19 janvier 

potage
Potage du jour 
subtitle_potage

plat1 
Pâtes aux brocolis rôtis, pois chiches et citron
Subtitle_plat1

plat2 
Pâtes, champignons, ricotta et pignons de pin
Subtitle_plat2
Champignons de Glabech (Nommern)
Ricotta de Fromagerie luxembourgeoise
dessert 
Tiramisu à l’orange
Subtitle_dessert
Jeudi 20 janvier 

potage
Potage du jour 
subtitle_potage

plat1 
Bifanas de porc 
Subtitle_plat1
plat2 
Galette de betteraves et quinoa 
Subtitle_plat2
accompagnement 
Pommes de terre
Subtitle_accompagnement
Légumes
Chou blanc
Subtitle_légumes
dessert 
Fruits 
Subtitle_dessert

Vendredi 21 janvier 
potage
Potage du jour 
subtitle_potage
plat1 
Cassoulet de poisson 
Subtitle_plat1
plat2 
Cassoulet végétarien
Subtitle_plat2
haricots lingots, tomates et oignons
accompagnement 
Polenta 
Subtitle_accompagnement
dessert 
Feuilletée aux pommes 
Subtitle_dessert
    """
input = str(text)
def find_plats(input):
    plats_down = ["\npotage", "\nplat1", "\nplat2", "\naccompagnement", "\nLégumes", "\ndessert"]
    plats_up = ["\nfill_string", "\nPlat1", "\nPlat2", "\nAccompagnement", "fill_string", "\nDessert"]

    sub_down = ["\nsubtitle_potage", "\nsubtitle_plat1", "\nsubtitle_plat2", "\nsubtitle_accompagnement", "\nsubtitle_légumes", "\nsubtitle_dessert"]
    sub_up = ["\nSubtitle_potage", "\nSubtitle_plat1", "\nSubtitle_plat2", "\nSubtitle_accompagnement", "\nSubtitle_légumes", "\nSubtitle_dessert"]

    plats = ["potage", "plat1", "plat2", "accompagnement", "Légumes", "dessert"]


    def findall(input, search_item, search_item2, list_num, list_txt):
        input = str(input)
        findall = re.findall(search_item, input)
        findall2 = re.findall(search_item2, input)

        num = len(findall) + len(findall2)
        
        txt = findall
        txt2 = findall2
        txt = ' '.join(str(e) for e in txt) 
        txt2 = ' '.join(str(d) for d in txt2) 
        txt = txt + txt2

        list_num.append(num)
        list_txt.append(txt)

    def if_same(in1, in2):
        int(in1)
        int(in2)
        if in1 - in2 == 0:
            return True  
        else:
            raise ValueError(f"plats are false")


    plats_num_list = []
    plats_text_list = []
    sub_num_list = []
    sub_text_list = []
    results = []

    num1 = 0
    while num1 < 6:
        findall(input, plats_down[num1], plats_up[num1], plats_num_list, plats_text_list)
        num1 += 1

    num1 = 0
    while num1 < 6:
        findall(input, sub_down[num1], sub_up[num1], sub_num_list, sub_text_list)
        num1 += 1

    num1 = 0
    while num1 <= 5:
        value = if_same(plats_num_list[num1], sub_num_list[num1])
        value = f"{plats[num1]} is {value}"
        print(value)
        results.append(value)
        num1 += 1

    print(results)
    return results 

find = find_plats(input)
print(find)