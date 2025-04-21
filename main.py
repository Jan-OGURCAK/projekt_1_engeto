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
    "no_texts": len(TEXTS),
    "no_words": 0,
    "tilte_case": 0,
    "up_case": 0,
    "lo_case": 0,
    "no_numbers": 0,
    "sum_numbers": 0,
    "text_idx": 0,
    "selected_text": None,
    "input_error": None}

data_graf = {}

def user_OK(users):
    """
        Funkce vyhodnocuje zadane parametry 'Username' a 'Password'
        zadane vstupne parametry porovnava s predavanym slovnikem 'users'

        Parametry:
        :navrat: navtratova boolean hodnota user nalezen?

        :data_global["input_error"]: Predpripraveny string s chybovym hlasenim

    """
    navrat = False

    user_name = input("Username: ")
    user_passw = input("Password: ")

    valid_password = users.get(user_name)

    if (user_passw == valid_password): 
        
        navrat = True
        print("-" * 40)
        print("Vítej v aplikaci,", user_name)
        print(f"máme připtaveno {data_global['no_texts']} texty na analýzu.")
        print("-" * 40)   

    elif (valid_password is None):
        data_global["input_error"] = f'Užívatel s loginem "{user_name}" nebyl nalezen!'
    
    else:
        data_global["input_error"] = "Zadané heslo není platné!"   

    return navrat

def vyber_textu_OK():

    """
        Funkce vyhodnocuje vstup z klavesnice a vybere text se kterym se bude pracovat

        Parametry:
        :navrat: navtratova boolean hodnota 'vyber textu OK?

        :data_global["text_idx"]: Globalni promenna int s indexem vybraneho textu

        :data_global["input_error"]: Predpripraveny string s chybovym hlasenim
        

    """
    vyber_OK = False

    vstup_txt = input(f"Zadej číslo mezi 1 a {data_global['no_texts']} pro výběr: ")

    if (vstup_txt.isnumeric()): # Je to cislo
    
        vstup_int = int(vstup_txt)

        if (0 < vstup_int <= data_global["no_texts"]): # A v platnem rozsahu
            
            data_global["text_idx"] = vstup_int -1
            vyber_OK = True
    
    if(not vyber_OK): # Doslo k chybe vstupu
        
        data_global["input_error"] = f"Byla ocekávána číselná hodnota v limitu 1 až {data_global["no_texts"]} !"

    return vyber_OK


def priprav_vetu():
    """
        Funkce vybere zvolemou vetu a
            - Vybere pouze alfanumeriske znaky
            - Odstrani prebytecne znaky ' '

        Parametry:
        :'data_global["text_idx"]': Globalni parametr int: - poradi vety v slovniku 'TEXTS'

        :'cista_veta': navratovy parametr str: - vybrana a vycistena veta
        
    """
    cista_veta = ""

    data_global["selected_text"] = TEXTS[data_global["text_idx"]] # Vyber 
    
    for znak in data_global["selected_text"]: # Vyberu pouze alfanumerika + " " 
        if (znak.isalnum() or (znak == " ")): cista_veta += znak

    while (cista_veta.find("  ") >= 0): # Odstraneni vicenasobnych mezer
        cista_veta = cista_veta.replace("  ", " ")

    return cista_veta

def analyza(cista_veta): # Vlasni analyza
    """
        Funkce provede vlastni analyzu

        Parametry:
        :'cista_veta' - predavany paremetr str: veta na zpracovani
        :'data_global["xxxx"]' - soubor statistickych parametru

        :'data_graf[delka_slova]' - soubor parametru int: - pocty slov dle delky pro graf
    """

    slova = cista_veta.split(" ") # Vytvoreni listu slov

    for index, slovo in enumerate(slova): # A vyhodnocujem...
            
        data_global["no_words"] += 1  # Napocet pocet slov slova

        delka_slova = len(slovo)

        if (data_graf.get(delka_slova) is None):
            data_graf[delka_slova] = 0

        data_graf[delka_slova] += 1 # Napocet pro graf dle delky 

        if (slovo.isnumeric()): # Je to cislo?

            data_global["no_numbers"] += 1 # Napocet cisel

            data_global["sum_numbers"] += int(slovo) # Napocet suma cisel

        else: # tak je to tedy string!
            
            if (slovo.isupper()): # Napocet vsecno velkym
                data_global["up_case"] += 1
            elif (slovo.istitle()): # Napocet prvni znak velkym
                data_global["tilte_case"] += 1

            if (slovo.islower()): # Napocet vsechno malym
                data_global["lo_case"] += 1
            
def vytvor_radek(delka_slova,poc_vyskytu):
    """
        Funkce vytvori radek grafu cetnosti slov dle delky

        Parametry:

        :'delka_slova': - int: delka slova

        :'poc_vyskytu': - int: koliktat se dana delka slova vyskytuje v textu

        :'navrat': - str: - navratovy parametr s hotovym radkem grafu

    """
    navrat = ""
    pomI = 0

    navrat = str(delka_slova) # Prefix =============================
    pomI = 3 - len(navrat)
    navrat = pomI * " " + navrat + "|"
    navrat += poc_vyskytu * "*" # Sloupecek ==================
    navrat += (20 - poc_vyskytu) * " " + "|"
    navrat += str(poc_vyskytu)

    return navrat


def vytvor_vystup():
    """
        Funkce vytvori graficky vystup programu

        Parametry:
        :'data_global["xxxx"]': - int: slovnik statistickych parametru vlastnosti slov

        :'data_graf[xxx]': int: - list statistik slov dle delky


    """
    # Vypis statistik

    print("-" * 40) # Podtrhnem...

    print(f"There are {data_global["no_words"]} words in the selected text.") # A vypiseme
    print(f"There are {data_global["tilte_case"]} titlecase words.") 
    print(f"There are {data_global["up_case"]} uppercase words.")   
    print(f"There are {data_global["lo_case"]} lowercase words.")   
    print(f"There are {data_global["no_numbers"]} numeric strings.")   
    print(f"The sum of all the numbers {data_global["sum_numbers"]}")

    print("-" * 40) # Podtrhnem...

    print("LEN|  OCCURENCES        |NR.")

    print("-" * 40) # Podtrhnem...

    aktivni_klice = list(data_graf.keys())
    aktivni_klice.sort() # Vytvorim list aktivnich klicu

    for klic in aktivni_klice: # A vytvorim grafickou prezentaci

        poc_vyskytu = data_graf[klic]

        if (poc_vyskytu > 0): print(vytvor_radek(klic,poc_vyskytu))

# =========================================================
# =================== Vlastni program =====================
# =========================================================

if (user_OK(users) and vyber_textu_OK()):

    analyza(priprav_vetu())
    vytvor_vystup()

else:

    print(2 * "\n")

    print(data_global["input_error"], 2 * "\n")

    print("Program byl ukončen!", end="\n")

    print("Zkuste program znovu spustit s jinými parametry, popřípadě informujte správce systému.", 2* "\n")




   

