import sys


def req_form():
    try:
        blank_space = "_"*20
        office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
        full_name = input("Vase cele jmeno: ") or blank_space
        birth_date = input("Vase datum narozeni: ") or blank_space
        addr_of_res = input("Vase trvale bydliste: ") or blank_space
        election_type_dict = {1: "Volbach do Poslanecke snemovny Parlamentu CR", 2: "Volbach do Senatu Parlamentu CR",
                     3: "Volbach do krajskych zastupitelstev", 4: "Volbach do Evropskeho parlamentu",
                     5: "Volbe prezidenta republiky"}
        election_type = election_type_dict[int(str(input(
        """Pro ktery typ voleb?
        \n[1]: Volby do Poslanecke snemovny
        \n[2]: Volby do Senatu
        \n[3]: Volby do krajskeho zastupitelstva
        \n[4]: Volby do Evropskeho parlamentu
        \n[5]: Volba prezidenta republiky"""
        )))] or blank_space
        election_date = input("Termin konani voleb: ") or blank_space
    except ValueError as e:
        print(e)
        raise("No integer input.")

    req_text = f"""Obecní úřad 
               \n{office} 
               \n 
               \n 
               \n 
               \nZADOST O VYDANI VOLICSKEHO PRUKAZU 
               \n
               \n pro hlasovani ve {election_type} ve dnech {election_date} 
               \n 
               \n 
               \nJmeno a prijmeni zadatele: {full_name} 
               \n
               \n Datum narozeni: {birth_date} 
               \n
               \nTrvaly pobyt: {addr_of_res}"""

    try:
        with open("Zadost.txt", "w") as req:
            req.write(req_text)
    except IOError:
        raise("Exciting! Exiting...")


try:
    req_form()
except IOError as e:
    print(e)