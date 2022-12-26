# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76


from random import uniform


def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Количество произвольных чисел в списке не может быть отрицательным!")
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Минимальная дробная часть: {num_min}, Максимальная дробная часть: {num_max}. Разница: {result}")
    return result


all_list = list_rand_nums(int(input("Введите количество произвольных чисел в списке: ")))
print(f'Наш список,состоящий из произвольных вещественных чисел: {all_list}')
print(f'Разница между максимальным и минимальным значением дробной части элементов - {dif_max_min(all_list)}')