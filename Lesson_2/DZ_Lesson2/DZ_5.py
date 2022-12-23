# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]




from random import randrange

num = int(input())
nums_list = list(range(num))
result_list = []

print(nums_list)

for i in range(num):
    b, c = randrange(num), randrange(num)
    nums_list[b], nums_list[c] = nums_list[c], nums_list[b]

print(nums_list)