# Исследуйте функции:
# f = (x ** 2 + 3) / (3 * (x + 1))

# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0



from sympy import *
from jupyter import *
from matplotlib import *

def f():
    x = Symbol('x')
    return (x**2 + 3)/(3*(x + 1)) # возвращает эту строку
    
def ff(xx):
    return float((xx**2 + 3)/(3*(xx + 1))) # возвращает значение функции в точке xx
    
y = solve(f()) #возвращает список с корнями уравнения (корни комплексные нужно перевести их во флоат).
print('корни: \n', y)

df=diff(f()) # получаем дифференциал этого уравнения
print('дифференциал уравнения: ', df)
korni = solve(df) #получаем корни этого уравнения
print('корни ДИФФ: ', korni)

# 2.	Найти интервалы, на которых функция возрастает

print('интервалы, на которых функция возрастает: ', solve(df>0))
# 3.	Найти интервалы, на которых функция убывает

print('интервалы, на которых функция убывает: ', solve(df<0))

# 5.	Определить промежутки, на котором f > 0

print('промежутки, на котором f > 0 :', solve(f()>0))

# 6.	Определить промежутки, на котором f < 0

print('промежутки, на котором f < 0 :', solve(f()<0))

# 4.	Построить график

import matplotlib.pyplot
list_y=[]
for i in range(-100, 101): # берём короткий отрезок по оси х, от -10 до 10
    x5=i
    y5= ff(x5)
    list_y.append(y5)
print('дискретные точки х и y для отрисовки графика: \n', list_y, "\n") # получили дискретные точки х и y для отрисовки графика


matplotlib.pyplot.plot(range(-100,101), list_y) # передали эти точки в функцию,
matplotlib.pyplot.show() # которая строит по ним график