# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки 
# шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
# 
# Формат ввода
# 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
# клетки, потом для второй клетки.
# 
# Формат вывода
# 
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
# 
# Примеры
#
# Тест 1
# Входные данные:
# 4
# 4
# 5
# 5
# 
# Вывод программы:
# YES

x1,y1,x2,y2,=int(input()), int(input()), int(input()), int(input())
if abs(x1-x2) <=1 and abs(y1-y2)<=1:
	print('YES')
else: 
	print('NO')