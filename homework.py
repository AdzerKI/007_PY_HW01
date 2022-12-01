# README Приношу свои извинения что не был на семинарах, семейные обстоятельства, трагедия, 
# сейчас наверстываю все задания к сегодняшнему уроку все лекции семинары и ДЗ


# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

x = int(input("Enter a day: "))

if x > 7 or x < 1:
    print(f"Not a day")
elif 0 < x < 6:
    print(f"{x} -> No")
else:
    print(f"{x} -> Yes")

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True

for n in range(0, 8):
    num = bin(n)
    num = num.replace('b', '0')
    X = int(num[-3])
    Y = int(num[-2])
    Z = int(num[-1])
    result = result and (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))

print(result)


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 or y == 0:
    print("x or y == 0")
elif x > 0 and y > 0:
    print(f"x={x}, y={y} -> 1")
elif x > 0 and y < 0:
    print(f"x={x}, y={y} -> 4")
elif x < 0 and y < 0:
    print(f"x={x}, y={y} -> 3")
else:
    print(f"x={x}, y={y} -> 2")


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Тут беру целочисленные, предполагая что 0,000...1 и выше

x = int(input("Enter quater: "))

if x < 1 or x > 4:
    print("1 < quater > 4")
elif x == 1:
    print(f"x=0,000...1 and above, y=0,000...1 and above")
elif x == 4:
    print(f"x=0,000...1 and above, y=-0,000...1 and below")
elif x == 3:
    print(f"x=-0,000...1 and below, y=-0,000...1 and below")
else:
    print(f"x=-0,000...1 and below, y=0,000...1 and above")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

xa = int(input("Enter xa: "))
ya = int(input("Enter ya: "))
xb = int(input("Enter xb: "))
yb = int(input("Enter yb: "))

#AB = √(xb - xa)2 + (yb - ya)2
result = math.sqrt(math.pow((xb - xa),2) + math.pow((yb - ya),2))

print(f"A({xa,ya}); B({xb},{yb}) - > {round(result, 2)}")
