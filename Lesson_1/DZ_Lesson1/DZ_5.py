# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# --------------------
# out
# 5.099




import math  

x1 = int(input("Введите координату X первой точки A: "))
y1 = int(input("Введите координату y первой точки A: "))
x2 = int(input("Введите координату X второй точки B: "))
y2 = int(input("Введите координату y второй точки B: "))

print(f"Длина отрезка {round(float(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))), 3)}")