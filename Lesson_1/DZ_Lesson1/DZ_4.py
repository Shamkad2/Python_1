# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти


quarter_number = int(input("Введите номер четверти: "))

if quarter_number == 1:
    print("x > 0; y > 0")
elif quarter_number == 2:
    print("x < 0; y > 0")
elif quarter_number == 3:
    print("x < 0; y < 0")
elif quarter_number == 4:
    print("x > 0; y < 0")
else:
    print("Нет такой четверти")