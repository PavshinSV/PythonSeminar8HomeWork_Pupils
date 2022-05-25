def get_base():
    with open('pupils.csv','r') as pupils_file:
        pupils=[pupil.split(';') for pupil in pupils_file]
    with open('adresses.csv','r') as adresses_file:
        adresses=[adress.split(';') for adress in adresses_file]
    with open('cabinets.csv','r') as cabinets_file:
        cabinetes=[cabinet.split(';') for cabinet in cabinets_file]
    return [pupils,adresses,cabinetes]