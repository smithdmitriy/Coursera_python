# Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение второго по величине 
# элемента в этой последовательности, то есть элемента, который будет наибольшим, если из последовательности удалить
# одно вхождение наибольшего элемента.
# 
# Формат ввода
# 
# Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит,
# а служит как признак ее окончания).
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
# Вывод программы:
# 7
# 
# 
# 
# Тест 2
# Входные данные:
# 2
# 1
# 0
# 
# Вывод программы:
# 1
# 
# 
# 
# Тест 31 (дополнительный пример)
# Входные данные:
# 1
# 2
# 2
# 3
# 3
# 0
# 
# Вывод программы:
# 3

n=1
max1=0
max2=0
while n!=0:
	n=int(input())
	if n>=max2:
		max2=n
	if n>=max1:
		max2=max1
		max1=n
print()
print(max2)