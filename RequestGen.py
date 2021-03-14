import sys


def req_form():
    blank_space = "_"*20
    office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
    full_name = input("Vase cele jmeno: ") or blank_space
    birth_date = input("Vase datum narozeni: ") or blank_space
    addr_of_res = input("Vase trvale bydliste: ") or blank_space
    election_type_dict = {"1": "Volbách do Poslanecké sněmovny Parlamentu ČR",
                          "2": "Volbách do Senátu Parlamentu ČR",
                          "3": "Volbách do krajských zastupitelstev",
                          "4": "Volbách do Evropského parlamentu",
                          "5": "Volbě prezidenta republiky"}
    election_type = election_type_dict.get(input(
        """Pro ktery typ voleb?
        [1]: Volby do Poslanecke snemovny
        [2]: Volby do Senatu
        [3]: Volby do krajskeho zastupitelstva
        [4]: Volby do Evropskeho parlamentu
        [5]: Volba prezidenta republiky
        """), blank_space)
    election_date = input("Termin konani voleb: ") or blank_space

    delivery_addr = blank_space
    delivery_dict = {"1": f"""
                     [x] převezmu osobně  
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu 
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     "2": f"""
                     [ ] převezmu osobně 
                     [x] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     "3": f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [x] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     "4": f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [x] žádám zaslat na jinou adresu: {delivery_addr}"""
                     }

    delivery_input = input(
            """Jakym zpusobem ma byt prukaz dorucen?
            [1] převezmu osobně
            [2] převezme jiná osoba s plnou mocí
            [3] žádám doručit na trvalou adresu
            [4] žádám doručit na jinou adresu
            """)
    delivery_blank = f"""
                        [ ] převezmu osobně 
                        [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                        [ ] žádám zaslat na adresu místa trvalého pobytu
                        [ ] žádám zaslat na jinou adresu: {delivery_addr}"""
    if delivery_input == "4":
        delivery_addr = input("""Doplnte adresu pro doruceni volebniho prukazu: """)
        delivery_type = f"""
                    [ ] převezmu osobně 
                    [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                    [ ] žádám zaslat na adresu místa trvalého pobytu
                    [x] žádám zaslat na jinou adresu: {delivery_addr}"""
    else:
        delivery_type = delivery_dict.get(delivery_input, delivery_blank)

    req_text = f"""
                Obecní úřad 
               {office} 
                
                
                
                                  ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 
               
                      pro hlasovaní ve {election_type} ve dnech {election_date} 
               
               
               Žádám obecní úřad {office} o vydání voličského průkazu pro hlasování ve {election_type} 
               konaných ve dnech {election_date}
               neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a).
               
               Jméno a příjmení žadatele
               (voliče):                  {full_name} 
               Datum narození:            {birth_date} 
               Trvalý pobyt:              {addr_of_res}
               
               K tomu sděluji, že voličský průkaz:
               {delivery_type}
               
               
                                                           {blank_space}
                                                          podpis voliče - žadatele"""
    try:
        with open("Zadost.txt", "w") as req:
            req.write(req_text)
    except ValueError:
        pass
try:
    req_form()
except IOError as e:
    print(e)
