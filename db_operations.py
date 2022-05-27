import copy
import ui


def get_adress():
    city = input('Введите Город: ')
    street = input('Введите Улицу: ')
    house = input('Введите номер дома: ')
    room = input('Введите номер квартиры: ')
    status = input('Введите статус адреса: ')
    return [city, street, house, room, status]


def get_fio():
    second_name = input('Введите Фамилию: ')
    first_name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    birth_date = input('Введите Дату рождения: ')
    return [second_name, first_name, patronymic, birth_date]


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

    if len(data) == 0:
        new_id = 1
    else:
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
    pupil_is_in_base = False
    second_name = input('Введите Фамилию ученика: ')
    first_name = input('Введите Имя ученика: ')
    patronymic = input('Введите Отчество ученика: ')
    birth_date = input('Введите дату рождения ученика (ДД.ММ.ГГГГ): ')
    in_base_id = 0
    for pupil in db[0]:
        if pupil[0].isdigit():
            if pupil[1].lower() == second_name.lower() and pupil[2].lower() == first_name.lower() and pupil[
                3].lower() == patronymic.lower() and pupil[4] == birth_date:
                pupil_is_in_base = True
                in_base_id = int(pupil[0])

    if pupil_is_in_base:
        print('Такой ученик существует.')
        get_find(db, second_name + " " + first_name + " " + patronymic + " " + birth_date)
        no_option = True
        for i in range(1, len(db[2])):
            if int(db[2][i][1]) == in_base_id:
                no_option = False
        if no_option:
            print('У этого ученика отсутствует информация о месте в классе и варианте!')
            row = input('Введите Ряд на котором сидит ученик: ')
            collumn = input('Введите Номер парты: ')
            option = input('Введите номер Варианта: ')

            indexes_of_cabinet = get_new_index(db[2])

            new_pupil_cabinet = [str(indexes_of_cabinet), str(in_base_id), str(row), str(collumn), option]
            with open('cabinets.csv', 'a') as cabinets:
                cabinets.writelines(f"{';'.join(new_pupil_cabinet)}\n")

        add_adres = input('Хотите добавить адрес? Y/N: ')
        if add_adres == 'Y':
            adr = get_adress()
            adr_id = get_new_index(db[1])
            new_adress = [str(adr_id), str(in_base_id), adr[0], adr[1], str(adr[2]), str(adr[3]), adr[4]]
            with open('adresses.csv', 'a') as adress:
                adress.writelines(f"{';'.join(new_adress)}\n")
    else:
        pupil_class = input('Введите Класс ученика: ')
        status = input('Введите Статус ученика (Отличник/Хорошист/Ударник/Двоечник): ')
        pupil_row = input('Введите Ряд ученика: ')
        pupil_column = input('Введите Парту ученика: ')
        pupil_option = input('Введите Вариант ученика: ')
        adr = get_adress()

        adr_id = get_new_index(db[1])

        indexes_of_pupils = get_new_index(db[0])

        indexes_of_cabinet = get_new_index(db[2])

        new_pupil = [str(indexes_of_pupils), second_name, first_name, patronymic, birth_date, str(pupil_class), status]
        with open('pupils.csv', 'a') as pupil_db:
            pupil_db.writelines(f"{';'.join(new_pupil)}\n")

        new_pupil_cabinet = [str(indexes_of_cabinet), str(indexes_of_pupils), str(pupil_row), str(pupil_column),
                             pupil_option]
        with open('cabinets.csv', 'a') as cabinets:
            cabinets.writelines(f"{';'.join(new_pupil_cabinet)}\n")

        new_adress = [str(adr_id), str(indexes_of_pupils), adr[0], adr[1], str(adr[2]), str(adr[3]), adr[4]]
        with open('adresses.csv', 'a') as adress:
            adress.writelines(f"{';'.join(new_adress)}\n")


def get_data_remove(db):
    pupil = get_fio()
    pupil_id = 0
    not_find = True
    index = 0
    while not_find and index < len(db[0]) - 1:
        index += 1
        if db[0][index][1] == pupil[0] and db[0][index][2] == pupil[1] and db[0][index][3] == pupil[2] and db[0][index][
            4] == pupil[3]:
            not_find = False
            pupil_id = index
            pupil_index = db[0][index][0]
    if not_find:
        print('По введенным данным ученик не найден. Проверьте данные и повторите процедуру.')
    else:
        menu = ['Удалить ученика;Удалить адрес;Удалить данные о месте и варианте']
        choice = ui.get_choice(menu[0])
        if choice == 1:
            db[0].pop(pupil_id)
            length = len(db[1]) - 1
            for index in range(length, 0, -1):
                if db[1][index][1] == pupil_index:
                    db[1].pop(index)
            length = len(db[2]) - 1
            for index in range(length, 0, -1):
                if db[2][index][1] == pupil_index:
                    db[2].pop(index)
            with open('pupils.csv', 'w') as file:
                [file.writelines(f'{";".join(pup)}\n') for pup in db[0]]
            with open('cabinets.csv', 'w') as file:
                [file.writelines(f'{";".join(pup)}\n') for pup in db[2]]
            with open('adresses.csv', 'w') as file:
                [file.writelines(f'{";".join(pup)}\n') for pup in db[1]]

        if choice == 2:
            length = len(db[1])
            temp = []
            list = []
            for i in range(0, length):
                if db[1][i][1] == pupil_index:
                    temp.append(db[1][i])
                    list=copy.deepcopy(temp)
                    list[-1].append(i)
            [print(f'{j + 1}: {list[j][2]}, {list[j][3]}, {list[j][4]}-{list[j][5]}, {list[j][6]}') for j in
             range(0, len(list))]
            not_valid = True
            remove_str = ''
            while not_valid:
                remove_str = input('Введите номер адреса (цифра в первом столбце) подлежащий удалению: ')
                if remove_str.isdigit() and (0 < int(remove_str) and int(remove_str) < len(list) + 1):
                    not_valid = False
            db[1].pop(list[int(remove_str) - 1][-1])
            with open('adresses.csv', 'w') as file:
                [file.writelines(f'{";".join(pup)}\n') for pup in db[1]]
        if choice == 3:
            for i in range(1,len(db[2])):
                if db[2][i][1]==pupil_index:
                    db[2].pop(i)
            with open('cabinets.csv', 'w') as file:
                [file.writelines(f'{";".join(pup)}\n') for pup in db[2]]


def get_find(db, string=''):
    no_one_find = True
    if string == '':
        desired = input('Введите данные для поиска через пробел: ').split(' ')
    else:
        desired = string.split(' ')
    for pupil in db[0]:
        source = ''
        for i in range(1, len(pupil)):
            source += pupil[i] + " "
        for clases in db[2]:
            if clases[1] == pupil[0]:
                for i in range(2, len(clases)):
                    source += clases[i] + " "
        first_string = True
        for adress in db[1]:
            adres_string = ''
            if adress[1] == pupil[0]:
                for i in range(2, len(adress)):
                    adres_string += "\t" + adress[i]
            all_match = True
            for item in desired:
                if item.lower() not in (source + adres_string).lower():
                    all_match = False
            if all_match:
                if first_string:
                    print(source)
                    first_string = False
                    no_one_find = False
                if len(adres_string) > 0:
                    print(f'\t{adres_string}')
    if no_one_find:
        print(f'\nПо введенным условиям ничего не найдено\n')


def get_export(db):
    path=input('Введите имя файла: ')
    file=open(path + '.csv', 'a')
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
                pattern1 = f'{pupil[1]};{pupil[2]};{pupil[3]};{pupil[4]};{pupil[5]};{pupil[6]}'
            else:
                pattern1 = f'{pupil[1]};{pupil[2]};{pupil[3]};{pupil[4]};{pupil[5]};{pupil[6]};{db[2][id_find][2]};{db[2][id_find][3]};{db[2][id_find][4]}'
            #print(f'\n{pattern}')
            file.writelines(pattern1)
            no_adress=True
            for adress in db[1]:
                if adress[1].isdigit() and adress[1] == pupil[0]:
                    if not no_adress:
                        file.writelines(pattern1)
                    no_adress=False
                    pattern = f';{adress[2]};{adress[3]};{adress[4]};{adress[5]};{adress[6]}\n'
                    file.writelines(pattern)

            if no_adress:
                file.writelines(f'\n')
        else:
            pattern1 = f'{pupil[1]};{pupil[2]};{pupil[3]};{pupil[4]};{pupil[5]};{pupil[6]};{db[2][0][2]};{db[2][0][3]};{db[2][0][4]}'
            file.writelines(pattern1)
            pattern = f';{db[1][0][2]};{db[1][0][3]};{db[1][0][4]};{db[1][0][5]};{db[1][0][6]}\n'
            file.writelines(pattern)
    file.close()