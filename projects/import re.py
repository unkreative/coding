import re
men = """

Lundi 17 janvier

potage
Potage du jour
Subtitle_potag

plat1 
Ragoût de jeune bovin aux carottes 
Subtitle_plat1_
Biohaff Baltes Stegen
plat2 
Subtitle_plat2_
Ragoût de tofu fumé aux carottes
accompagnement 
Boulgour
Subtitle_accompagnement_

dessert  
Gâteau aux noix
Subtitle_dessert_


Mardi 18 janvier 
potage
Potage du jour
Subtitle_potag

plat1 
Chili con carne 
Subtitle_plat1_

plat2 
Chili sin carne
Subtitle_plat2_

accompagnement 
Riz de Camargue 
Subtitle_accompagnement_

dessert 
Fruits  
Subtitle_dessert_

Mercredi  19 janvier 

potage
Potage du jour 
Subtitle_potag

plat1 
Pâtes aux brocolis rôtis, pois chiches et citron
Subtitle_plat1_

plat2 
Pâtes, champignons, ricotta et pignons de pin
Subtitle_plat2_
Champignons de Glabech (Nommern)
Ricotta de Fromagerie luxembourgeoise
dessert 
Tiramisu à l’orange
Subtitle_dessert_
Jeudi 20 janvier 

potage
Potage du jour 
Subtitle_potag

plat1 
Bifanas de porc 
Subtitle_plat1_
plat2 
Galette de betteraves et quinoa 
Subtitle_plat2_
accompagnement 
Pommes de terre
Subtitle_accompagnement_
Légumes 
Chou blanc 
Subtitle_légumes_
dessert 
Fruits 
Subtitle_dessert_

Vendredi 21 janvier 

potage
Potage du jour 
Subtitle_potag
plat1 
Cassoulet de poisson 
Subtitle_plat1_
plat2 
Cassoulet végétarien
Subtitle_plat2_
haricots lingots, tomates et oignons
accompagnement 
Polenta 
Subtitle_accompagnement_
dessert 
Feuilletée aux pommes 
Subtitle_dessert_
"""
value = re.findall("potage", men)
value = len(value)
print(value)

value2 = re.findall("Subtitle_potag", men)
value2 = len(value2)
print(value2)