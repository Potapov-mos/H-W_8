# Создать информационную систему позволяющую работать с учениками школы
# функции
# Добавление нового студента (Поля - имя, фамилия)
# Добавление предмета (добавляется всем ученикам сразу)
# Добавление оценки ученику по предмету (выбираем ученика(из существующих),
# выбираем предмет(из сущ.),пишем оценку )
# Показ списка учеников (имена фамилия)
# Показ листа оценок конкретного ученика
# Выход из программы
# Достаточно хранить данные в переменной


import view

main_dct = {}
name_list = []
lessons_list = []

def start():
    while True:
        print(main_dct)
        op = view.get_op()
        if op == 1:
            name = view.input_student()
            if name not in name_list:
                name_list.append(name)
                main_dct[name] = {}
                for less in lessons_list:
                    main_dct[name][less] = []
        if op == 2:
            less = view.input_less()
            if less not in lessons_list:
                lessons_list.append(less)
                for name in name_list:
                    main_dct[name][less] = []
        if op == 3:
            name, less, mark = view.get_mark()
            main_dct[name][less].append(mark)
        if op == 4:
            print(main_dct)
        if op == 5:
            name = view.input_student_table()
            print(main_dct[name])
        if op == 6:
            break
