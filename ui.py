def get_choice(comand_line):
    comands_list = comand_line.split(';')
    comands = enumerate(comands_list, 1)
    print('\nВведите число, соответствующее номеру пункта меню')
    error = True
    while error:
        greatings = ', '.join([f'{x[0]}:{x[1]}' for x in comands])
        print(f'{greatings}')
        inp = input()
        if inp.isdigit() and 0 < int(inp) and int(inp) < len(comands_list) + 1:
            error = False
        else:
            print("Вы ввели неверное значение. Повторите ввод")
    return int(inp)


def get_look(db):
     for pupil in db[0]:
        id_find = 0
        pupil_id = 0
        if pupil[0] != 'id':
            #print(pupil[0])
            pupil_id = int(pupil[0])
            not_finded = True
            while not_finded:
                id_find += 1
                if id_find==len(db[2]):
                    break
                if id_find == len(db[2]) or int(db[2][id_find][1]) == pupil_id:
                    not_finded = False
            if not_finded:
                pattern = f'{pupil[1]} {pupil[2]} {pupil[3]} {pupil[4]} {pupil[5]} {pupil[6]}'
            else:
                pattern = f'{pupil[1]} {pupil[2]} {pupil[3]} {pupil[4]} {pupil[5]} {pupil[6]} {db[2][id_find][1]} {db[2][id_find][2]} {db[2][id_find][3]} {db[2][id_find][4]}'
            print(f'\n{pattern}')
            for adress in db[1]:
                if adress[1].isdigit() and adress[1]==pupil[0]:
                    pattern=f'\t{adress[2]}\t{adress[3]}\t{adress[4]}\t{adress[5]}\t{adress[6]}'
                    print(pattern)