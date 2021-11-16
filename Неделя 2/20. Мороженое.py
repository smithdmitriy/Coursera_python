# В кафе мороженое продают по три шарика и по пять шариков. Можно ли купить ровно k шариков мороженого?
# 
# Формат ввода
# 
# Вводится число k (целое,положительное)
# 
# Формат вывода
# 
# Программа должна вывести слово YES, если при таких условиях можно набрать ровно k шариков (не больше и не меньше), 
# в противном случае - вывести NO.
# 
# Примеры
#
# Тест 1
# Входные данные:
# 2
# 
# Вывод программы:
# NO
# 
# 
# 
# Тест 2
# Входные данные:
# 3
# 
# Вывод программы:
# YES

k = int(input())
i=1
while i<=k//3 and k>2:
	if (k%3*i)%5==0 or (k%5*i)%3==0:
		print('YES')
		break
	if i==k//3:
		print('NO')
		break
	i=i+1
else:
	print('NO')

		


	
	
		
		
