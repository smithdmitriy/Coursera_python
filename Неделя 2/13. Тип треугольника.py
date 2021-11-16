# Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. Выведите одно из четырех слов:
# rectangular для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного 
# треугольника или impossible, если треугольника с такими сторонами не существует (считаем, что вырожденный треугольник
# тоже невозможен).
# 
# Формат ввода
# 
# Вводятся три целых числа.
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примеры
#
# Тест 1
# Входные данные:
# 3
# 4
# 5
# 
# 
# Вывод программы:
# rectangular
# 
# 
# 
# Тест 2
# Входные данные:
# 3
# 5
# 4
# 
# 
# 
# Вывод программы:
# rectangular

a,b,c = int(input()), int(input()), int(input())
if a >= b and a>=c:
	max = a
	nemax1 = b
	nemax2 = c
elif b >= c:
	max = b
	nemax1 = a
	nemax2 = c
else:
	max = c
	nemax1 = a
	nemax2 = b
if max >= nemax1 + nemax2:
	print('impossible')
elif max**2 == nemax1**2 + nemax2**2:
		print('rectangular')
elif max**2 > nemax1**2 + nemax2**2:
		print('obtuse')
else:
		print('acute')

		
	