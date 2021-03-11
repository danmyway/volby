def ReqForm():
    blank_space = "_"*20
    office = blank_space
    full_name = blank_space
    birth_date = blank_space
    addr_of_res = blank_space
    election_type = blank_space
    election_date = blank_space


    req_text = "Obecní úřad {office}".format(office=input("Adresa obecniho uradu "))



    try:
        with open("Zadost.txt", "w") as req:
            req.write(req_text)
    except OSError as e:
        print(e)

ReqForm()