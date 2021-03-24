import sys, os, time

cwdir = os.getcwd()
##file_path = input("Cesta pro umisteni souboru zadosti: ") or ""
blank_space = "_" * 20

delivery_blank = f"""
                    [ ] převezmu osobně 
                    [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                    [ ] žádám zaslat na adresu místa trvalého pobytu
                    [ ] žádám zaslat na jinou adresu: {blank_space}"""
req_text = f"""
                Obecní úřad 
               {blank_space} 



                                  ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 

                      pro hlasovaní ve {blank_space} ve dnech {blank_space} 


               Žádám obecní úřad {blank_space} o vydání voličského průkazu pro hlasování ve {blank_space} 
               konaných ve dne(ch) {blank_space}
               neboť nebudu moci volit ve volebním okrsku, v jehož seznamu voličů jsem zapsán(a).

               Jméno a příjmení žadatele
               (voliče):                  {blank_space} 
               Datum narození:            {blank_space} 
               Trvalý pobyt:              {blank_space}

               K tomu sděluji, že voličský průkaz:
               {delivery_blank}


                                                           {blank_space}
                                                          podpis voliče - žadatele"""


def blank_form():
    try:
        reply = input(f"Chcete vygenerovat prazdny formular? y/n").lower().strip()
        if reply[0] == "y":
            with open("Zadost.txt", "w") as bl_form:
                bl_form.write(req_text)
            print(f"Zadost byla uspesne ulozena v {cwdir} !")
            exit()

        if reply[0] == "n":
            req_form()
        else:
            return blank_form()
    except ValueError as e:
        print(e)
    except IndexError:
        print("Vyberte jednu z moznosti!")
        blank_form()
    except KeyboardInterrupt:
        print("Program byl ukoncen uzivatelem.")


def req_form():
    office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
    full_name = input("Vase cele jmeno: ") or blank_space
    while True:
        try:
            birth_date = input("Vase datum narozeni: ") or blank_space
            time.strptime(birth_date, "%d/%m/%Y")
        except ValueError:
            print("Datum je v chybnem formatu!")
            continue
        else:
            break
    addr_of_res = input("Vase trvale bydliste: ") or blank_space
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
                election_type = blank_space
                break
            election_type = election_type_dict.get(election_type_in)

            if election_type is None:
                print("Zadejte platnou volbu z nabizenych moznosti!")
                continue
            break

        except ValueError:
            print("Zadejte platnou volbu z nabizenych moznosti!")
            continue

    while True:
        try:
            election_date = input("Termin konani voleb (Vlozte ve formatu dd/mm/rrrr): ") or blank_space
            time.strptime(election_date, "%d/%m/%Y")
        except ValueError:
            print("Datum je v chybnem formatu!")
            continue
        else:
            break

    delivery_addr = blank_space
    delivery_dict = {1: f"""
                     [x] převezmu osobně  
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu 
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     2: f"""
                     [ ] převezmu osobně 
                     [x] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     3: f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [x] žádám zaslat na adresu místa trvalého pobytu
                     [ ] žádám zaslat na jinou adresu: {delivery_addr}""",
                     4: f"""
                     [ ] převezmu osobně 
                     [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                     [ ] žádám zaslat na adresu místa trvalého pobytu
                     [x] žádám zaslat na jinou adresu: {delivery_addr}"""
                     }
    while True:
        try:
            delivery_input = int(input(
                """Jakym zpusobem ma byt prukaz dorucen?
                [1] převezmu osobně
                [2] převezme jiná osoba s plnou mocí
                [3] žádám doručit na trvalou adresu
                [4] žádám doručit na jinou adresu
                """))

            if delivery_input == 4:
                delivery_addr = input("""Doplnte adresu pro doruceni volebniho prukazu: """)
                delivery_type = f"""
                    [ ] převezmu osobně 
                    [ ] převezme osoba, která se prokáže plnou mocí s mým úředně ověřeným podpisem
                    [ ] žádám zaslat na adresu místa trvalého pobytu
                    [x] žádám zaslat na jinou adresu: {delivery_addr}"""
                break
            delivery_type = delivery_dict.get(delivery_input, delivery_blank)
        except ValueError:
            print("Zadejte nekterou z nabizenych moznosti!")
            continue
        else:
            break

    req_text = f"""
                Obecní úřad 
               {office} 
                
                
                
                                  ŽÁDOST O VYDÁNÍ VOLEBNÍHO PRŮKAZU 
               
                      pro hlasovaní ve {election_type} ve dnech {election_date} 
               
               
               Žádám obecní úřad {office} o vydání voličského průkazu pro hlasování ve {election_type} 
               konaných ve dne(ch) {election_date}
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
        with open(f"Zadost.txt", "w") as req:
            req.write(req_text)
    except ValueError:
        pass

    print(f"Zadost byla uspesne ulozena v {cwdir} !")
try:
    blank_form()
except IOError as e:
    print(e)
except KeyboardInterrupt:
    print("Program byl ukoncen uzivatelem.")
