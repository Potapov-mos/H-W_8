def get_op():
    op = int(input(" 1 - Добавить ученика \n 2 - Добавить предмет \n 3 - Добавить оценку \n 4 - Показать весь список \n 5 - Показать ученика \n 6 - Выход\n"))
    return op

def input_student():
    name = input("Введите имя фамилию: ")
    return name

def input_less():
    less = input("Введите предмет: ")
    return less

def get_mark():
    name = input("Введите имя фамилию: ")
    less = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, less, mark

def input_student_table():
    name = input("Введите имя фамилию ученика для просмотра оценок: ")
    return name