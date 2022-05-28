import db_operations as db
import ui


def run():
    while True:
        data = db.get_base()  # data[0] - ученики, data[1] - адреса, data[2] - место в классе
        #print(data)
        menu = ['Просмотр базы;Добавление сведений;Удаление сведений;Поиск;Экспорт Базы']
        choice = ui.get_choice(menu[0])
        if choice == 1:
            ui.get_look(data)
        elif choice == 2:
            db.get_new_data(data)
        elif choice == 3:
            db.get_data_remove(data)
        elif choice ==4:
            db.get_find(data)
        elif choice ==5:
            db.get_export(data)
        else:
            print('Ошибка ввода - сообщите разработчику')