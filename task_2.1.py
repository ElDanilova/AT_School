# Вводная о программе
print("Добро пожаловать в консольный калькулятор!\nЭта программа работает с целыми числами и умеет складывать, вычитать, делить и умножать.\n")

# Запускаем бесконечный калькулятор
while True:

    # Переводим первый ввод в целое число
    while True:
        try:
            num1 = int(input("Введите первый операнд - целое число: "))
            break
        except ValueError:
            print("Это не целое число.")

    # Переводим второй ввод в целое число
    while True:
        try:
            num2 = int(input("Введите второй операнд - целое число: "))
            break
        except ValueError:
            print("Это не целое число.")

    # Определяем операцию над числами
    op_dic = ("+", "-", "*", "/")
    while True:
        op = input("Введите совершаемую над числами операцию в виде команды: + , - , / , * \n")
        fl = False
        for i in op_dic:
            if op == i:
                fl = True
                break
        if not fl:
            print("Вы ввели неизвестную команду.")
        else:
            break

    # Производим вычисления
    fl2 = True
    calc = 0
    if op == "+":
        calc = num1 + num2
    elif op == "-":
        calc = num1 - num2
    elif op == "*":
        calc = num1 * num2
    else:
        try:
            calc = num1 / num2
        except ZeroDivisionError:
            fl2 = False
            print("Деление на ноль невозможно!")

    # Вывод результата
    if fl2:
        print("Результат операции", num1, op, num2,"=",calc)

    # Продолжение цикла
    num_or_stop = input("Для продолжения вычеслений нажмите Enter. \nДля завершения вычислений введите команду 'stop'.\n")
    if num_or_stop == "stop" or num_or_stop == "Stop" or num_or_stop == "STOP":
        print("Вы вышли из калькулятора.")
        break