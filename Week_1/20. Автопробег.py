# Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день на A метров, а за ночь спускаясь
# на B метров. На какой день улитка доползет до вершины шеста?
# =================================
# Формат ввода
#
# Программа получает на вход целые H, A, B. Гарантируется, что A > B ≥ 0.
# =================================
# Формат вывода
#
# Программа должна вывести одно натуральное число.
# =================================
# Примеры
#
# Тест 1
# Входные данные:
# 10
# 3
# 2
#
# Вывод программы:
# 8
h,a,b = int(input()), int(input()), int(input())
p = 0
p1 = 0
d = 0
while p1 < h:
    d = d + 1
    p = p + a
    print("День ", d, "Позиция ", p)
    p1 = p
    p = p - b
else:
    print(d)


