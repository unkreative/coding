import re

test = """
Lundi DATE MOIS



potage

I

Subtitle_potage

I

Plat 1

I

Subtitle_plat1

I

Plat 2

I

Subtitle_plat2

I

Accompagnement

I

Subtitle_accompagnement

I

Légumes

I

Subtitle_légumes

I

Dessert

I

Subtitle_dessert

I



Mardi DATE MOIS



potage

I

Subtitle_potage

I

Plat 1

I

Subtitle_plat1

I

Plat 2

I

Subtitle_plat2

I

Accompagnement

Ii

Subtitle_accompagnement

I

Légumes

I

Subtitle_légumes

I

Dessert

I

Subtitle_dessert

I



Mercredi DATE MOIS



potage

I

Subtitle_potage

I

Plat 1

I

Subtitle_plat1

I

Plat 2

I

Subtitle_plat2

I

Accompagnement

I

Subtitle_accompagnement

I

Légumes

I

Subtitle_légumes

I

Dessert

I

Subtitle_dessert

I



Jeudi DATE MOIS



potage

I

Subtitle_potage

I

Plat 1

I

Subtitle_plat1

I

Plat 2

I

Subtitle_plat2

I

Accompagnement

I

Subtitle_accompagnement

I

Légumes

I

Subtitle_légumes

I

Dessert

I

Subtitle_dessert

I



Vendredi DATE MOIS



potage

I

Subtitle_potage

I

Plat 1

i

Subtitle_plat1

I

Plat 2

I

Subtitle_plat2

I

Accompagnement

I

Subtitle_accompagnement

I

Légumes

I

Subtitle_légumes

I

Dessert

I

Subtitle_dessert

I
"""

print(test)