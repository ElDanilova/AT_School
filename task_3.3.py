def season (n):
    n = int(n)
    if n == 1 or n == 2 or n == 12:
        return ("зима")
    elif n == 3 or n == 4 or n == 5:
        return ("весна")
    elif n == 6 or n == 7 or n == 8:
        return ("лето")
    elif n == 9 or n == 10 or n == 11:
        return ("осень")

# Программа
print("Добро пожаловать! Перед вами программа, определяющая время года по введённому месяцу.")
m = input("Введите номер месяца: ")
print("Это", season(m))