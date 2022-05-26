def get_base():
    with open('pupils.csv','r') as pupils_file:
        pupils=[pupil.replace('\n','').split(';') for pupil in pupils_file]
    with open('adresses.csv','r') as adresses_file:
        adresses=[adress.replace('\n','').split(';') for adress in adresses_file]
    with open('cabinets.csv','r') as cabinets_file:
        cabinetes=[cabinet.replace('\n','').split(';') for cabinet in cabinets_file]
    return [pupils,adresses,cabinetes]

def get_new_data():
    return

def get_data_remove():
    return

def get_export():
    return