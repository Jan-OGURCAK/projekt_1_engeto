"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ján OGURČÁK
email: jan.ogurcak@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''']

users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

data_global = {
    "pocet_vet": len(TEXTS),
    "pocet_slov": 0,
    "zacatek_velkym": 0,
    "psano_velkym": 0,
    "psano_malym": 0,
    "pocet_cisel": 0,
    "suma_cisel": 0,
    "veta_idx": 0,
    "veta": None,
    "chyba_vstupu": None}

data_graf = []

def user_OK(users):

    navrat = False

    user_name = input("username: ")
    user_passw = input("password: ")

    valid_password = users.get(user_name)

    if (user_passw == valid_password): 
        
        navrat = True
        print("-" * 40)
        print("Welcome to the app,", user_name)
        print(f"We have {data_global['pocet_vet']} texts to be analyzed.")
        print("-" * 40)   

    else:
            
        data_global["chyba_vstupu"] ="unregistered user, terminating the program.."


    return(navrat)

def vyber_textu_OK():
    vyber_OK = False

    vstup = input(f"Enter a number btw. 1 and {data_global['pocet_vet']} to select: ")


    if (vstup.isnumeric()):
    
        vstup = int(vstup)

        pocet_vet = len(TEXTS)

        if (0 < vstup <= data_global["pocet_vet"]):
            
            data_global["veta_idx"] = vstup -1
            vyber_OK = True
    
    if(not vyber_OK): data_global["chyba_vstupu"] = "Bad choice, terminating the program.. "

    return(vyber_OK)


def priprav_vetu():
    cista_veta = ""

    data_global["veta"] = TEXTS[data_global["veta_idx"]] # Vyber 
    
    for znak in data_global["veta"]: # Vyberu pouze alfanumerika + " " 
        if (znak.isalnum() or (znak == " ")): cista_veta += znak

    while (cista_veta.find("  ") >= 0): # Odstraneni vicenasobnych mezer
        cista_veta = cista_veta.replace("  ", " ")

    return(cista_veta)

def analyza(cista_veta): # Vlasni analyza

    slova = cista_veta.split(" ") # Vytvoreni listu slov

    for index, slovo in enumerate(slova): # A vyhodnocujem...
            
        data_global["pocet_slov"] += 1  # Napocet pocet slov slova
        data_graf[len(slovo)] += 1 # Napocet pro graf dle delky 

        if (slovo.isnumeric()): # Je to cislo?

            data_global["pocet_cisel"] += 1 # Napocet cisel

            data_global["suma_cisel"] += int(slovo) # Napocet suma cisel

        else: # tak je to tedy string!
            
            if (slovo.isupper()): # Napocet vsecno velkym
                data_global["psano_velkym"] += 1
            elif (slovo[0:1].isupper()): # Napocet prvni znak velkym
                data_global["zacatek_velkym"] += 1

            if (slovo.islower()): # Napocet vsechno malym
                data_global["psano_malym"] += 1
            
def vytvor_radek(delka_slova,poc_vyskytu):
    navrat = ""
    pomI = 0

    navrat = str(delka_slova) # Prefix =============================
    pomI = 3 - len(navrat)
    navrat = pomI * " " + navrat + "|"
    navrat += poc_vyskytu * "*" # Sloupecek ==================
    navrat += (20 - poc_vyskytu) * " " + "|"
    navrat += str(poc_vyskytu)

    return(navrat)


def vytvor_vystup(data_global, data_graf):

    # Vypis statistik

    print("-" * 40) # Podtrhnem...

    print(f"There are {data_global["pocet_slov"]} words in the selected text.") # A vypiseme
    print(f"There are {data_global["zacatek_velkym"]} titlecase words.") 
    print(f"There are {data_global["psano_velkym"]} uppercase words.")   
    print(f"There are {data_global["psano_malym"]} lowercase words.")   
    print(f"There are {data_global["pocet_cisel"]} numeric strings.")   
    print(f"The sum of all the numbers {data_global["suma_cisel"]}")

    print("-" * 40) # Podtrhnem...

    print("LEN|  OCCURENCES        |NR.")

    print("-" * 40) # Podtrhnem...

    for delka_slova, poc_vyskytu in enumerate(data_graf):

        if (poc_vyskytu > 0): print(vytvor_radek(delka_slova,poc_vyskytu))

# =========================================================
# =================== Vlastni program =====================
# =========================================================

for count in range(0,20):
    data_graf.append(0)

if (user_OK(users) and vyber_textu_OK()):

    priprav_vetu()
    analyza(priprav_vetu())
    vytvor_vystup(data_global, data_graf)

else:

    print(data_global["chyba_vstupu"])





   

