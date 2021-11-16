# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. Определите, можно ли разместить одну из этих
# коробок внутри другой, при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.
# 
# Формат ввода
# 
# Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.
# 
# Формат вывода
# 
# Программа должна вывести одну из следующих строчек:
# 
# Boxes are equal, если коробки одинаковые,
# 
# The first box is smaller than the second one, если первая коробка может быть положена во вторую,
# 
# The first box is larger than the second one, если вторая коробка может быть положена в первую,
# 
# Boxes are incomparable, во всех остальных случаях.
# 
# Примеры
#
# Тест 1
# Входные данные:
# 1
# 2
# 3
# 3
# 2
# 1
# 
# Вывод программы:
# Boxes are equal
# 
# 
# 
# Тест 2
# Входные данные:
# 2
# 2
# 3
# 3
# 2
# 1
# 
# Вывод программы:
# The first box is larger than the second one

a1, b1, c1, a2, b2, c2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
while a1>=b1 or b1>=c1:
	if a1>b1:
		a1,b1=b1,a1
	if b1>c1:
		b1,c1=c1,b1	
while a2>=b2 or b2>=c2:
	if a2>b2:
		a2,b2=b2,a2
	if b2>c2:
		b2,c2=c2,b2
print(a1,b1,c1)
print(a2,b2,c2)
if a1==a2 and b1==b2 and c1==c2:
	print('Boxes are equal')		
elif a1>=a2 and b1>=b2 and c1>=c2:
	print('The first box is larger than the second one')
else:
	print('The first box is smaller than the second one')
	
