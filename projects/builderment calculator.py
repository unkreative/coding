
from functools import total_ordering
from numpy import mat

resources = [
    "copper ore",
    "iron ore",
    "wood log",
    "stone",
    "coal",
    "wolframite"
]

wood_plank = {
    "name": "wood plank",
    "itemspermin": 15,
    "building": "workshop",
    "value": 1,
    "ingredientlist": [{"name": "wood log", "amount": 1}]
}
wood_frame = {
    "name": "wood frame",
    "itemspermin": 7.5,
    "building": "workshop",
    "value": 4,
    "ingredientlist": [{"name": "wood plank", "amount": 4}],
}
copper_wire = {
    "name": "copper wire",
    "itemspermin": 30,
    "building": "workshop",
    "value": 2,
    "ingredientlist": [{"name": "copper ingot", "amount": 1.5}],
}

heat_sink = {
    "name": "heat sink",
    "itemspermin": 10,
    "building": "workshop",
    "value": 5,
    "ingredientlist": [{"name": "copper ingot", "amount": 5}],
}
iron_gear = {
    "name": "iron gear",
    "itemspermin": 15,
    "building": "workshop",
    "value": 2,
    "ingredientlist": [{"name": "iron ingot", "amount": 2}],
}
iron_plating = {
    "name": "iron plating",
    "itemspermin": 20,
    "building": "workshop",
    "value": 2,
    "ingredientlist": [{"name": "iron ingot", "amount": 2}],
}
steel_rod = {
    "name": "steel rod",
    "itemspermin": 15,
    "building": "workshop",
    "value": 35,
    "ingredientlist": [{"name": "steel", "amount": 3}],
}
sand = {
    "name": "sand",
    "itemspermin": 40,
    "building": "workshop",
    "value": 1,
    "ingredientlist": [{"name": "stone", "amount": 1}],
}
condenser_lens = {
    "name": "condenser lens",
    "itemspermin": 20,
    "building": "workshop",
    "value": 12,
    "ingredientlist": [{"name": "glass", "amount": 3}],
}
carbon_fiber = {
    "name": "carbon fiber",
    "itemspermin": 7.5,
    "building": "workshop",
    "value": 24,
    "ingredientlist": [{"name": "graphite", "amount": 4}],
}
coupler = {
    "name": "coupler",
    "itemspermin": 6,
    "building": "workshop",
    "value": 24,
    "ingredientlist": [{"name": "tungsten carbide", "amount": 1}],
}
iron_ingot = {
    "name": "iron ingot",
    "itemspermin": 30,
    "building": "furnace",
    "value": 1,
    "ingredientlist": [{"name": "iron ore", "amount": 1}],
}
copper_ingot = {
    "name": "copper ingot",
    "itemspermin": 30,
    "building": "furnace",
    "value": 1,
    "ingredientlist": [{"name": "copper ore", "amount": 1}],
}
silicone = {
    "name": "silicone",
    "itemspermin": 20,
    "building": "furnace",
    "value": 2,
    "ingredientlist": [{"name": "sand", "amount": 2}],
}
glass = {
    "name": "glass",
    "itemspermin": 10,
    "building": "furnace",
    "value": 4,
    "ingredientlist": [{"name": "sand", "amount": 4}],
}
tungsten_ore = {
    "name": "tungsten ore",
    "itemspermin": 30,
    "building": "furnace",
    "value": 5,
    "ingredientlist": [{"name": "wolframite", "amount": 5}],
}
electromagnet = {
    "name": "electromagnet",
    "itemspermin": 7.5,
    "building": "machine shop",
    "value": 14,
    "ingredientlist": [
        {"name": "copper wire", "amount": 6},
        {"name": "iron ingot", "amount": 2},
    ],
}
logic_circuit = {
    "name": "logic circuit",
    "itemspermin": 10,
    "building": "machine shop",
    "value": 10,
    "ingredientlist": [
        {"name": "copper wire", "amount": 3},
        {"name": "silicone", "amount": 2},
    ],
}
metal_frame = {
    "name": "metal frame",
    "itemspermin": 5,
    "building": "machine shop",
    "value": 12,
    "ingredientlist": [
        {"name": "wood frame", "amount": 1},
        {"name": "iron plating", "amount": 4},
    ],
}
battery = {
    "name": "battery",
    "itemspermin": 2.5,
    "building": "machine shop",
    "value": 150,
    "ingredientlist": [
        {"name": "electromagnet", "amount": 8},
        {"name": "graphite", "amount": 8},
    ],
}
rotor = {
    "name": "rotor",
    "itemspermin": 10,
    "building": "machine shop",
    "value": 40,
    "ingredientlist": [
        {"name": "iron plating", "amount": 2},
        {"name": "steel rod", "amount": 1},
    ],
}
nano_wire = {
    "name": "nano wire",
    "itemspermin": 5,
    "building": "machine shop",
    "value": 60,
    "ingredientlist": [
        {"name": "glass", "amount": 4},
        {"name": "carbon fiber", "amount": 2},
    ],
}
graphite = {
    "name": "graphite",
    "itemspermin": 15,
    "building": "forge",
    "value": 6,
    "ingredientlist": [
        {"name": "wood log", "amount": 3},
        {"name": "coal", "amount": 3},
    ],
}
steel = {
    "name": "steel",
    "itemspermin": 7.5,
    "building": "forge",
    "value": 12,
    "ingredientlist": [
        {"name": "iron ore", "amount": 6},
        {"name": "graphite", "amount": 1},
    ],
}
concrete = {
    "name": "concrete",
    "itemspermin": 7.5,
    "building": "forge",
    "value": 40,
    "ingredientlist": [
        {"name": "sand", "amount": 10},
        {"name": "steel rod", "amount": 1},
    ],
}
tungsten_carbide = {
    "name": "tungsten carbide",
    "itemspermin": 12,
    "building": "forge",
    "value": 16,
    "ingredientlist": [
        {"name": "tungsten ore", "amount": 2},
        {"name": "graphite", "amount": 1},
    ],
}
computer = {
    "name": "computer",
    "itemspermin": 7.5,
    "building": "industrial factory",
    "value": 60,
    "ingredientlist": [
        {"name": "heat sink", "amount": 3},
        {"name": "metal frame", "amount": 1},
        {"name": "logic circuit", "amount": 3},
    ],
}
electric_motor = {
    "name": "electric motor",
    "itemspermin": 3,
    "building": "industrial factory",
    "value": 250,
    "ingredientlist": [
        {"name": "iron gear", "amount": 4},
        {"name": "rotor", "amount": 2},
        {"name": "battery", "amount": 1},
    ],
}
electron_microscope = {
    "name": "electron microscope",
    "itemspermin": 2.5,
    "building": "manufacturer",
    "value": 300,
    "ingredientlist": [
        {"name": "condenser lens", "amount": 4},
        {"name": "electromagnet", "amount": 8},
        {"name": "metal frame", "amount": 2},
        {"name": "nano wire", "amount": 2},
    ],
}
turbocharger = {
    "name": "turbocharger",
    "itemspermin": 4,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "iron gear", "amount": 8},
        {"name": "logic circuit", "amount": 4},
        {"name": "nano wire", "amount": 2},
        {"name": "coupler", "amount": 4},
    ],
}
super_computer = {
    "name": "super computer",
    "itemspermin": 2,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "computer", "amount": 2},
        {"name": "heat sink", "amount": 8},
        {"name": "turbocharger", "amount": 1},
        {"name": "coupler", "amount": 8},
    ],
}
atomic_locator = {
    "name": "atomic locator",
    "itemspermin": 2,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "concrete", "amount": 24},
        {"name": "copper wire", "amount": 50},
        {"name": "electron microscope", "amount": 2},
        {"name": "super computer", "amount": 2},
    ],
}
earth_token = {
    "name": "earth token",
    "itemspermin": 1.428571429,
    "building": "earth transporter",
    "value": 250,
    "ingredientlist": [{"name": "matter duplicator", "amount": 1}],
}
energy_cube = {
    "name": "energy cube",
    "itemspermin": 2,
    "building": "machine shop",
    "value": 250,
    "ingredientlist": [
        {"name": "battery", "amount": 2},
        {"name": "industrial frame", "amount": 1},
    ],
}
gyroscope = {
    "name": "gyroscope",
    "itemspermin": 5,
    "building": "machine shop",
    "value": 250,
    "ingredientlist": [
        {"name": "copper wire", "amount": 12},
        {"name": "rotor", "amount": 2},
    ],
}
industrial_frame = {
    "name": "industrial frame",
    "itemspermin": 3,
    "building": "industrial factory",
    "value": 250,
    "ingredientlist": [
        {"name": "concrete", "amount": 6},
        {"name": "metal frame", "amount": 2},
        {"name": "tungsten carbide", "amount": 8},
    ],
}
magnetic_field_generator = {
    "name": "magnetic field generator",
    "itemspermin": 1.5,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "electromagnet", "amount": 10},
        {"name": "industrial frame", "amount": 1},
        {"name": "nano wire", "amount": 10},
        {"name": "stabilizer", "amount": 1},
    ],
}
matter_compressor = {
    "name": "matter compressor",
    "itemspermin": 2,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "electric motor", "amount": 2},
        {"name": "tank", "amount": 1},
        {"name": "turbocharger", "amount": 2},
        {"name": "industrial frame", "amount": 1},
    ],
}
matter_duplicator = {
    "name": "matter duplicator",
    "itemspermin": 2 / 3,
    "building": "manufacturer",
    "value": 250,
    "ingredientlist": [
        {"name": "atomic locator", "amount": 4},
        {"name": "energy cube", "amount": 5},
        {"name": "particle glue", "amount": 100},
        {"name": "quantum entangler", "amount": 2},
    ],
}
particle_glue = {
    "name": "particle glue",
    "itemspermin": 20,
    "building": "workshop",
    "value": 250,
    "ingredientlist": [
        {"name": "matter compressor", "amount": 0.1}
    ],
}
quantum_entangler = {
    "name": "quantum entangler",
    "itemspermin": 1,
    "building": "machine shop",
    "value": 250,
    "ingredientlist": [
        {"name": "magnetic field generator", "amount": 1},
        {"name": "stabilizer", "amount": 2},
    ],
}
stabilier = {
    "name": "stabilizer",
    "itemspermin": 2.5,
    "building": "industrial factory",
    "value": 250,
    "ingredientlist": [
        {"name": "computer", "amount": 1},
        {"name": "electric motor", "amount": 1},
        {"name": "gyroscope", "amount": 2},
    ],
}
tank = {
    "name": "tank",
    "itemspermin": 6,
    "building": "industrial factory",
    "value": 250,
    "ingredientlist": [
        {"name": "concrete", "amount": 4},
        {"name": "glass", "amount": 2},
        {"name": "tungsten carbide", "amount": 4},
    ],
}
item_list = ['copper wire', 'wood frame', 'atomic locator', 'battery', 'carbon fiber', 'computer', 'concrete', 'condenser lens', 'copper ingot', 'coupler', 'earth token', 'electric motor', 'electromagnet', 'electron microscope', 'energy cube', 'glass', 'graphite', 'gyroscope', 'heat sink', 'industrial frame', 'iron gear', 'iron ingot', 'iron plating', 'logic circuit', 'magnetic field generator', 'matter compressor', 'matter duplicator', 'metal frame', 'nano wire', 'particle glue', 'quantum entangler', 'rotor', 'sand', 'silicone', 'stabilier', 'steel', 'steel rod', 'super computer', 'tank', 'tungsten carbide', 'tungsten ore', 'turbocharger', 'wood plank']
item_list2 = [copper_wire, wood_frame, atomic_locator, battery, carbon_fiber, computer, concrete, condenser_lens, copper_ingot, coupler, earth_token, electric_motor, electromagnet, electron_microscope, energy_cube, glass, graphite, gyroscope, heat_sink, industrial_frame, iron_gear, iron_ingot, iron_plating, logic_circuit, magnetic_field_generator, matter_compressor, matter_duplicator, metal_frame, nano_wire, particle_glue, quantum_entangler, rotor, sand, silicone, stabilier, steel, steel_rod, super_computer, tank, tungsten_carbide, tungsten_ore, turbocharger, wood_plank]

def craft_something():
    print()
    item = input("enter your item: ")
    var = select_var(item)

    item_name  =  var["name"]
    print(f"{item_name} recipe: ")
    for x in var["ingredientlist"]:

        print(x["name"], "", x["amount"]) 
    print()
    print("items per min: ", var["itemspermin"])       
    print("value: ", var["value"])


def calculate_eart_tokens():
    copper = input("copper mines: ")
    iron = input("iron mines: ")
    wood = input("wood mines: ")
    stone = input("stone mines: ")
    coal = input("coal mines: ")
    wolframite = input("wolframite mines: ")

def select_var(item, result=''):
    item = str(item)
    item[0].lower()
    print(item)
    #print("aaa")
    num1 = 0
    # print(type(item))
    while num1 < len(item_list):
        if item_list[num1] == item:
            result = item_list2[num1]
            # print(result)
            break
        num1 += 1
    # print("result: ", result)
    return result

def things_required_item():
    item = input("enter your item: ")
    
    var = select_var(item)

    # print(var)
    recipes = var["ingredientlist"]
    for x in recipes:
        var1 = x["name"]

        var3 = select_var(var1)
        print(var3)
        print(var3, "a")
        var2 = var1["ingredientlist"]
        print("var2: ", var2)
        var2 = var2["name"]
        print(var1)
        for y in resources:
            if y == var2:
                pass
            else:
                print("aa")


def require():
    # item = input("enter your item: ")
    item = "tank"

    selected = select_var(item)
    print("start val: ", selected, "\n")
    materials = []
    for x in selected["ingredientlist"]:
        print("first loop: ", x)
        materials.append(x)
    print("materials after one step", materials)
    num1 = 0

    while num1 <= len(materials):
        
        new_mat = materials[num1]
        
        new = new_mat["name"]
        print()

        new = select_var(new)

        print("new variable",new)

        j = new["ingredientlist"]
        
        print("selected ingredients", j)
        
        print("lesgo")
        
        for x in j:
            print(x)
            
            materials.append(x)
            
            print("new materials", materials)
        num1 += 1
    print()
    print(materials)
    print()


def get_ingredients(item, items, total_materials):
    start_value = select_var(item)

    for item in start_value["ingredientlist"]:
        print(item)
        g = item["name"]
        items.append(g)
        total_materials.append(item)

def check_if_basic_material(material):
    for resource in resources:
        if material == resource:
            return True
        
    return False



def get_materials():
    needed_amount = []
    item = "tank"
    # item = input("item: ")
    ingredient_list1 = []
    total_list = []
    get_ingredients(item, ingredient_list1, total_list)
    print("ingredients_list: ", ingredient_list1)
    print("total_list: ", total_list)

    for ingredient in ingredient_list1:
        boo = check_if_basic_material(ingredient)
        if boo == True:
            break

        ingredient_list2 = []
        
        get_ingredients(ingredient, ingredient_list2, total_list)
        for ingredient2 in ingredient_list2:
            ingredient_list3 = []
            get_ingredients(ingredient2, ingredient_list3, total_list)
            print(ingredient_list3)
    
    print(total_list)
    print()
    for x in total_list:
        print(x)

    origins = []
    num1 = 0
    while num1 < len(total_list):
        it = total_list[num1]
        it = it["name"]

        arg = check_if_basic_material(it)

        if arg == True:
            origins.append(num1)

        num1 += 1
    print(origins)
    return total_list


def get(material):
    ingredient_list1 = []
    total_list = []
    get_ingredients(material, ingredient_list1, total_list)
    print("material: ", material)
    print("ingredients: ")
    
    tree = {}
    num1 = 0

    while num1 < len(ingredient_list1):
        print(ingredient_list1[num1])
        items = []
        tree[num1] = ingredient_list1[num1]
        get_ingredients(tree[num1], items, total_list)
        num2 = 0
        while num2 < len(items):
            print(items[num2])
            it = []
            tree[num1][it] = items[num2]       
        num1 += 1
    
    print(tree)

    
material = "matter duplicator"



def get_meds(material, lst1, tot_lst):
    get_ingredients(material, lst1, tot_lst)

def get(material, lst1, tot_lst):
    get_meds(material, lst1, tot_lst)
    print()

    print(lst1)
    print()
    for x in lst1:
        if x in resources:
            pass
        else:
            print("x:", x)
            get_meds(str(x), lst1, tot_lst)

lsta = []
tlist = []
get(material, lsta, tlist)
