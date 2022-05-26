def get_choice(comand_line):
    comands_list=comand_line.split(';')
    comands=enumerate(comands_list,1)
    print('\nВведите число, соответствующее номеру пункта меню')
    error = True
    while error:
        greatings=', '.join([f'{x[0]}:{x[1]}' for x in comands])
        print(f'{greatings}')
        inp = input()
        if inp.isdigit() and 0 < int(inp) and int(inp)<len(comands_list)+1:
            error=False
        else:
            print("Вы ввели неверное значение. Повторите ввод")
    return int(inp)

def get_look(db):
    print(db[0],db[1],db[2])
    [print(f'{" ".join(data[0])} {" ".join(data[1])} {" ".join(data[2])}') for data in db]

    #    with open('people.csv') as db:
    #    [print(line.replace('\n','')) for line in db