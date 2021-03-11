import sys

def ReqForm():

    blank_space = "_"*20
    office = input("Adresa obecniho uradu v miste Vaseho volebniho okrsku: ") or blank_space
    full_name = input("Vase cele jmeno: ") or blank_space
    birth_date = input("Vase datum narozeni: ") or blank_space
    addr_of_res = input("Vase trvale bydliste: ") or blank_space
    election_type = blank_space
    election_date = blank_space


    req_text = "Obecní úřad " \
               "\n{}" \
               "\n" \
               "\n" \
               "\nZADOST O VYDANI VOLICSKEHO PRUKAZU" \
               "\npro hlasovani ve volbach" \
               "\n" \
               "\n" \
               "\nJmeno a prijmeni zadatele: {}" \
               "\nDatum narozeni: {}" \
               "\nTrvaly pobyt: {}".format(office, full_name, birth_date, addr_of_res)



    try:
        with open("Zadost.txt", "w") as req:
            req.write(req_text)
    except OSError as e:
        print(e)
        raise
    sys.exit(99)

ReqForm()