import ui


def get_adress():
    city = input('Введите Город: ')
    street = input('Введите Улицу: ')
    house = input('Введите номер дома: ')
    room = input('Введите номер квартиры: ')
    status = input('Введите статус адреса: ')
    return [city, street, house, room, status]


def get_base():
    with open('pupils.csv', 'r') as pupils_file:
        pupils = [pupil.replace('\n', '').split(';') for pupil in pupils_file]
    with open('adresses.csv', 'r') as adresses_file:
        adresses = [adress.replace('\n', '').split(';') for adress in adresses_file]
    with open('cabinets.csv', 'r') as cabinets_file:
        cabinetes = [cabinet.replace('\n', '').split(';') for cabinet in cabinets_file]
    return [pupils, adresses, cabinetes]

def get_new_index(datas):
    data = [int(datas[x][0]) for x in range(1, len(datas))]

    if len(data) == max(data):
        new_id = max(data) + 1
    else:
        data.sort()
        in_order = True
        id = 0
        while in_order:
            if data[id] < data[id + 1] - 1:
                in_order = False
                new_id = data[id] + 1
            id += 1
    return new_id

def get_new_data(db):
    pupil_is_in_base=False
    second_name = input('Введите Фамилию ученика: ')
    first_name = input('Введите Имя ученика: ')
    patronymic = input('Введите Отчество ученика: ')
    birth_date = input('Введите дату рождения ученика (ДД.ММ.ГГГГ): ')
    for pupil in db[0]:
        if pupil[0].isdigit():
            if pupil[1].lower() == second_name.lower() and pupil[2].lower() == first_name.lower() and pupil[
                3].lower() == patronymic.lower() and pupil[4] == birth_date:
                pupil_is_in_base=True

    if pupil_is_in_base:
        print('Такой ученик существует.')
        get_find(db, second_name + " " + first_name + " " + patronymic + " " + birth_date)
        add_adres = input('Хотите добавить адрес? Y/N: ')
        if add_adres == 'Y':
            adr = get_adress()
            adr_id=get_new_index(db[1])
            new_adress=[str(adr_id), str(pupil[0]), adr[0], adr[1], str(adr[2]), str(adr[3]), adr[4]]
            with open('adresses.csv','a') as adress:
                adress.writelines(';'.join(new_adress))
    else:
        pupil_class = input('Введите Класс ученика: ')
        status = input('Введите Статус ученика (Отличник/Хорошист/Ударник/Двоечник): ')
        pupil_row = input('Введите Ряд ученика: ')
        pupil_column = input('Введите Парту ученика: ')
        pupil_option = input('Введите Вариант ученика: ')
        adr = get_adress()

        adr_id=get_new_index(db[1])

        indexes_of_pupils = get_new_index(db[0])

        indexes_of_cabinet = get_new_index(db[2])

        new_pupil=[str(indexes_of_pupils),second_name,first_name,patronymic,birth_date,str(pupil_class),status]
        with open('pupils.csv', 'a') as pupil_db:
            pupil_db.writelines(f"{';'.join(new_pupil)}\n")

        new_pupil_cabinet=[str(indexes_of_cabinet),str(indexes_of_pupils),str(pupil_row),str(pupil_column),pupil_option]
        with open('cabinets.csv', 'a') as cabinets:
            cabinets.writelines(f"{';'.join(new_pupil_cabinet)}\n")

        new_adress = [str(adr_id), str(indexes_of_pupils), adr[0], adr[1], str(adr[2]), str(adr[3]), adr[4]]
        with open('adresses.csv', 'a') as adress:
            adress.writelines(f"{';'.join(new_adress)}\n")

def get_data_remove():
    return


def get_find(db, string=''):
    if string == '':
        desired = input('Введите данные для поиска через пробел: ').split(' ')
    else:
        desired = string.split(' ')
    for pupil in db[0]:
        id_find = 0
        pupil_id = 0
        if pupil[0] != 'id':
            pupil_id = int(pupil[0])
            not_finded = True
            while not_finded:
                id_find += 1
                if id_find == len(db[2]):
                    break
                if id_find == len(db[2]) or int(db[2][id_find][1]) == pupil_id:
                    not_finded = False
            if not_finded:
                pattern = f'{pupil[1]} {pupil[2]} {pupil[3]} {pupil[4]} {pupil[5]} {pupil[6]}'
                sourse = ' '.join(pupil)
            else:
                pattern = f'{pupil[1]} {pupil[2]} {pupil[3]} {pupil[4]} {pupil[5]} {pupil[6]} {db[2][id_find][1]} {db[2][id_find][2]} {db[2][id_find][3]} {db[2][id_find][4]}'
                sourse = ' '.join(pupil) + ' '.join(db[2][id_find])

            match = True
            for element in desired:
                if element not in sourse:
                    match = False
            if match:
                print(pattern)
                for adress in db[1]:
                    if adress[1].isdigit() and adress[1] == pupil[0]:
                        pattern = f'\t{adress[2]}\t{adress[3]}\t{adress[4]}\t{adress[5]}\t{adress[6]}'
                        print(pattern)


def get_export():
    return
