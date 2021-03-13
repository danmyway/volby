import sys


def req_form():
    blank_space = "_"*20
    office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
    full_name = input("Vase cele jmeno: ") or blank_space
    birth_date = input("Vase datum narozeni: ") or blank_space
    addr_of_res = input("Vase trvale bydliste: ") or blank_space
    election_type_dict = {1: "Volbách do Poslanecké sněmovny Parlamentu ČR", 2: "Volbách do Senátu Parlamentu ČR",
                     3: "Volbách do krajských zastupitelstev", 4: "Volbách do Evropského parlamentu",
                     5: "Volbě prezidenta republiky"}
    election_type = election_type_dict.get(int(input(
        """Pro ktery typ voleb?
        \n[1]: Volby do Poslanecke snemovny
        \n[2]: Volby do Senatu
        \n[3]: Volby do krajskeho zastupitelstva
        \n[4]: Volby do Evropskeho parlamentu
        \n[5]: Volba prezidenta republiky
        \n: """
            )), blank_space)
    election_date = input("Termin konani voleb: ") or blank_space
    delivery_dict = {1: f"""[x] převezmu osobně  
                     \n[ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     \n[ ] žádám zaslat na adresu místa trvalého pobytu 
                     \n[ ] žádám zaslat na jinou adresu: {blank_space}""",
                     2: f"""[ ] převezmu osobně 
                     \n[x] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     \n[ ] žádám zaslat na adresu místa trvalého pobytu
                     \n[ ] žádám zaslat na jinou adresu: {blank_space}""",
                     3: f"""[ ] převezmu osobně 
                     \n[ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     \n[x] žádám zaslat na adresu místa trvalého pobytu
                     \n[ ] žádám zaslat na jinou adresu: {blank_space}""",
                     4: f"""[ ] převezmu osobně 
                     \n[ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     \n[ ] žádám zaslat na adresu místa trvalého pobytu
                     \n[x] žádám zaslat na jinou adresu: """

                     }
    delivery_type = delivery_dict.get(int(input(
        """Jakym zpusobem ma byt prukaz dorucen?
        \n[1] převezmu osobně
        \n[2] převezme jiná osoba s plnou mocí
        \n[3] žádám doručit na trvalou adresu
        \n[4] žádám doručit na jinou adresu""")),
        f"""[ ] převezmu osobně 
        \n[ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
        \n[ ] žádám zaslat na adresu místa trvalého pobytu
        \n[ ] žádám zaslat na jinou adresu: {blank_space}"""
        )

    req_text = f"""Obecní úřad 
               \n{office} 
               \n 
               \n 
               \n 
               \nŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 
               \n
               \npro hlasovaní ve {election_type} ve dnech {election_date}, neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a). 
               \n 
               \n 
               \nJméno a příjmení žadatele
               \n(voliče):                  {full_name} 
               \nDatum narození:            {birth_date} 
               \nTrvalý pobyt:              {addr_of_res}
               \nK tomu sděluji, že voličský průkaz:\n{delivery_type}"""

    try:
        with open("Zadost.txt", "w") as req:
            req.write(req_text)
    except IOError:
        raise("You might have fucked up! Exiting...")


try:
    req_form()
except IOError as e:
    print(e)