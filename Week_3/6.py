# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет 
# X рублей Y копеек. Определите размер вклада через год. При решении этой задачи нельзя пользоваться 
# условными инструкциями и циклами.
# 
# Формат ввода
# 
# Программа получает на вход целые числа P, X, Y.
# 
# Формат вывода
# 
# Программа должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
# 
# Примеры
# 
# Тест 1
# Входные данные:
# 12
# 179
# 0
# 
# Вывод программы:
# 200 48
# 
# 
# 
# Тест 2
# Входные данные:
# 13
# 179
# 0
# 
# Вывод программы:
# 202 27
# 
# 
# 
# Тест 3
# Входные данные:
# 10
# 100
# 0
# 
# Вывод программы:
# 110 0


P, X, Y = int(input()), int(input()), int(input())
S =X+Y/100
S=S+S*P/100
print(int((round(S,0))),int((round(S%1,2)*100)),sep=" ")