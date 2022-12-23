# 4. Напишите программу, которая принимает на вход 2 числа. Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!





n = int(input("Введите число N: "))
posiz1 = int(input("Введите номер первой позиции: "))
posiz2 = int(input("Введите номер второй позиции: "))
print(*range(-n, n+1))
sum = 1
k = 0
for i in range(-n, n + 1):
    k = k + 1
    if (k == posiz1) or (k == posiz2):
        sum = sum * i
print(sum)