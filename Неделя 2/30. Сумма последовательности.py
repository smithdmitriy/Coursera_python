# Определите сумму всех элементов последовательности, завершающейся числом 0.
# 
# Формат ввода
# 
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, а
# служит как признак ее окончания).
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примеры
#
# Тест 1
# Входные данные:
# 1
# 7
# 9
# 0
# 
# 
# Вывод программы:
# 17
# 
# 
# 
# 
# Тест 2
# Входные данные:
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 0
# 
# 
# Вывод программы:
# 9
# 
# 
# 
# 
# Тест 3
# Входные данные:
# 34
# 2345
# 2345
# 2345
# 2345
# 345
# 3
# 345
# 3
# 345
# 1
# 3
# 424
# 5
# 453
# 0
# 
# 
# Вывод программы:
# 11341


n=1
s=0
while n!=0:
	n=int(input())
	s=s+n
print()
print(s)