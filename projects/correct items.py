import re

input = """
Lundi 31-01	
potage	Potage du jour
Plat 1	Spaghetti al ragù bianco
sauce bolognaise blanche
plat 2	Spaghetti végétarien aux légumes
dessert 	Duo de crème (vanille et chocolat)

Mardi    01-02	
potage 	Potage du jour
plat 1	Gratin mexicain
plat 2	Curry aux lentilles
accompagnement 	Tacos
dessert	Fruit

mercredi 02-02	
potage 	Potage du jour 
plat 1	Pizza buns au salami, tomates et fromage Berdorfer
plat 2	Pizza buns à la sauce béchamel, légumes et fromage Berdorfer
légumes 	Salade
dessert	Millefeuille

Jeudi 03-02	
potage 	Potage du jour 
plat 1	Morue, poireaux et émincé de pommes de terre au four
plat 2	Tartiflette revisitée
Émincé de pommes de terre au four, fromage, carottes et oignons
dessert	Brownie

vendredi 04-02	
potage 	Potage du jour 
plat 1	Bouchée à la reine 
plat 2	Bouchée aux légumes 
accompagnement 	Riz de Camargue 
légumes 	Champignons 
dessert 	Fruit


    """

def check_input2(input):
    plat1_correct = "\nplat1"
    plat2_correct = "\nplat2"
    légumes_correct = "\nLégumes"
    plat1_num = re.findall("\nplat 1", input)
    plat2_num = re.findall("\nplat 2", input)
    légumes_num = re.findall("\nlégumes", input)

    for x in plat1_num:
        input = input.replace(plat1_num[0], plat1_correct)

    for x in plat2_num:
        input = input.replace(plat2_num[0], plat2_correct)

    for x in légumes_num:
        input = input.replace(légumes_num[0], légumes_correct)

    print(input)
    return input
