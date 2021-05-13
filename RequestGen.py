import sys
import os
import time

cwdir = os.getcwd()
blank_space = "_"*20
delivery_blank = f"""
                    [ ] převezmu osobně 
                    [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                    [ ] žádám zaslat na adresu místa trvalého pobytu
                    [ ] žádám zaslat na jinou adresu: {blank_space}"""

def election_type():
    election_type_dict = {"1": "Volbách do Poslanecké sněmovny Parlamentu ČR",
                          "2": "Volbách do Senátu Parlamentu ČR",
                          "3": "Volbách do krajských zastupitelstev",
                          "4": "Volbách do Evropského parlamentu",
                          "5": "Volbě prezidenta republiky"}
    while True:
        try:
            election_type_in = input(
                """Pro ktery typ voleb?
                [1]: Volby do Poslanecke snemovny
                [2]: Volby do Senatu
                [3]: Volby do krajskeho zastupitelstva
                [4]: Volby do Evropskeho parlamentu
                [5]: Volba prezidenta republiky
                """)
            if election_type_in == "":
                el_type = blank_space
                break
            el_type = election_type_dict.get(election_type_in)

            if el_type is None:
                print("Zadejte platnou volbu z nabizenych moznosti!")
                continue
            break

        except ValueError:
            print("Zadejte platnou volbu z nabizenych moznosti!")
            continue

    return el_type


def delivery_addr():
    del_addr = input("""Doplnte adresu pro doruceni volebniho prukazu: """)

    return del_addr


def delivery_type():
    del_addr = blank_space
    delivery_dict = {"1": f"""
                     [x] převezmu osobně  
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu 
                     [ ] žádám zaslat na jinou adresu: {del_addr}""",
                     "2": f"""
                     [ ] převezmu osobně 
                     [x] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {del_addr}""",
                     "3": f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [x] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {del_addr}""",
                     "4": f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [x] žádám zaslat na jinou adresu: {del_addr}"""
                     }

    while True:
        try:
            delivery_input = input(
                """Jakym zpusobem ma byt prukaz dorucen?
                [1] převezmu osobně
                [2] převezme jiná osoba s plnou mocí
                [3] žádám doručit na trvalou adresu
                [4] žádám doručit na jinou adresu
                """)

            if delivery_input == "4":
                del_type = f"""
                                    [ ] převezmu osobně 
                                    [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                                    [ ] žádám zaslat na adresu místa trvalého pobytu
                                    [x] žádám zaslat na jinou adresu: {delivery_addr()}"""
                break
            del_type = delivery_dict.get(delivery_input, delivery_blank)
        except ValueError:
            print("Zadejte nekterou z nabizenych moznosti!")
            continue
        else:
            break
    return del_type


def birth_date():
    while True:
        try:
            bd = input("Vase datum narozeni: ") or blank_space
            time.strptime(bd, "%d/%m/%Y")
        except ValueError:
            print("Datum je v chybnem formatu!")
            continue
        else:
            break
    return bd


def election_date():
    while True:
        try:
            el_date = input("Termin konani voleb (Vlozte ve formatu dd/mm/rrrr): ") or blank_space
            time.strptime(el_date, "%d/%m/%Y")
        except ValueError:
            print("Datum je v chybnem formatu!")
            continue
        else:
            break
    return el_date


#def form_review():

def blank_form():
    blank_text = f"""
                    Obecní úřad 

                    {blank_space} 

                    {blank_space}


                                        ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 

                          pro hlasovaní ve {blank_space}{blank_space} ve dnech {blank_space} 



                   Žádám obecní úřad {blank_space}{blank_space} o vydání voličského průkazu pro hlasování ve {blank_space}{blank_space} 

                   konaných ve dnech {blank_space}

                   neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a).

                   Jméno a příjmení žadatele
                   (voliče):                  {blank_space}{blank_space} 

                   Datum narození:            {blank_space}{blank_space}

                   Trvalý pobyt:              {blank_space}{blank_space}

                   K tomu sděluji, že voličský průkaz:

                   {delivery_blank}


                                                               {blank_space}{blank_space}
                                                              podpis voliče - žadatele"""

    while True:
        try:
            reply = input(f"Chcete vygenerovat prazdny formular? y/n\n").lower().strip()
            if reply[0] == "y":
                with open("Zadost.txt", "w") as bl_form:
                    bl_form.write(blank_text)
                print(f"Zadost byla uspesne ulozena v {cwdir} !")
                sys.exit()

            if reply[0] == "n":
                req_form()
            else:
                print("Vyberte jednu z moznosti|")
                continue
        except IndexError:
            print("Vyberte jednu z moznosti!")
            blank_form()
        except PermissionError:
            print("Program nema opravneni pro zapis!")
            sys.exit()


def req_form():
    var_office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
    var_full_name = input("Vase cele jmeno: ") or blank_space
    var_addr_of_res = input("Vase trvale bydliste: ") or blank_space
    var_election_type = election_type()
    var_election_date = election_date()
    var_birth_date = birth_date()
    var_delivery_type = delivery_type()

    req_text = f"""
                Obecní úřad 
                
                {var_office} 
                
                
                
                                  ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 
               
                      pro hlasovaní ve {var_election_type} ve dnech {var_election_date} 
               
               
               Žádám obecní úřad {var_office} o vydání voličského průkazu pro hlasování ve {var_election_type} 
               
               konaných ve dnech {var_election_date}
               
               neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a).
               
               Jméno a příjmení žadatele
               (voliče):                  {var_full_name} 
               
               Datum narození:            {var_birth_date} 
               
               Trvalý pobyt:              {var_addr_of_res}
               
               K tomu sděluji, že voličský průkaz:
               
               {var_delivery_type}
               
               
                                                           {blank_space}
                                                      podpis voliče - žadatele"""
    review_menu_dict = {
        1: var_office,
        2: var_election_type,
        3: var_election_date,
        4: var_full_name,
        5: var_birth_date,
        6: var_addr_of_res,
        7: var_delivery_type
        }

    print(req_text)

    while True:
        try:
            req_check = input("Je zadost takto vyplnena spravne? (y/n)\n").lower().strip()
            if req_check[0] == 'y':
                print("OK! Ukladam zadost.")
                break
            elif req_check[0] == 'n':
                review_menu = int(input(f"""Co si prejete opravit?
                            [1]:{review_menu_dict[1]}
                            [2]:{review_menu_dict[2]}
                            [3]:{review_menu_dict[3]}
                            [4]:{review_menu_dict[4]}
                            [5]:{review_menu_dict[5]}
                            [6]:{review_menu_dict[6]}
                            [7]:{review_menu_dict[7]}
                            """))
                if review_menu == 2:
                    print("Zadejte spravny udaj.\n")
                    nu_el_type = election_type()
                    review_menu_dict[review_menu] = nu_el_type
                elif review_menu == 3:
                    print("Zadejte spravny udaj.\n")
                    nu_el_date = election_date()
                    review_menu_dict[review_menu] = nu_el_date
                elif review_menu == 5:
                    print("Zadejte spravny udaj.\n")
                    nu_bd = birth_date()
                    review_menu_dict[review_menu] = nu_bd
                elif review_menu == 7:
                    print("Zadejte spravny udaj.\n")
                    nu_del_type = delivery_type()
                    review_menu_dict[review_menu] = nu_del_type
                else:
                    review_menu_dict[review_menu] = input("Zadejte spravny udaj.\n")

                print(f"""
                            Obecní úřad 

                            {review_menu_dict[1]} 



                                              ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 

                                  pro hlasovaní ve {review_menu_dict[2]} ve dnech {review_menu_dict[3]} 


                           Žádám obecní úřad {review_menu_dict[1]} o vydání voličského průkazu pro hlasování ve {review_menu_dict[2]} 
                           konaných ve dne(ch) {review_menu_dict[3]}
                           neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a).

                           Jméno a příjmení žadatele
                           (voliče):                  {review_menu_dict[4]} 
                           Datum narození:            {review_menu_dict[5]} 
                           Trvalý pobyt:              {review_menu_dict[6]}

                           K tomu sděluji, že voličský průkaz:
                           {review_menu_dict[7]}


                                                                       {blank_space}{blank_space}
                                                                      podpis voliče - žadatele"""

                      )

                continue
            else:
                print("Zadejte jednu z uvedenych moznosti!")
                continue
        except ValueError:
            print("Zadejte jednu z uvedenych moznosti!")
            continue

    try:
        with open(f"Zadost.txt", "w") as req:
            req.write(req_text)
    except PermissionError:
        print("Program nema povoleni pro zapis!")

    print(f"Zadost byla uspesne ulozena v {cwdir} !")
    sys.exit()


try:
    blank_form()

except PermissionError as pr:
    print("Nastal problem!")
    print(pr)