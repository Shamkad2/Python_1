# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071



n = int(input("Введите число N: "))
i = 0
x = 0
lst = []
while i <= n - 1:
    i += 1
    b = (1 + (1 / i)) ** i
    lst.append(b)
    x = x + b
print(f"Для n = {n}: сумма = {round(x, 2)}")