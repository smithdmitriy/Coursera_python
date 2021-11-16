# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
# 
# Формат ввода
# 
# Вводится строка.
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примеры
# 
# Тест 1
# Входные данные:
# In the hole in the ground there lived a hobbit
# 
# Вывод программы:
# In the Hole in tHe ground tHere lived a hobbit
# 
# 
# 
# Тест 2
# Входные данные:
# qwertyhahsdhfghzxcvb
# 
# Вывод программы:
# qwertyhaHsdHfghzxcvb
# 
# 
# 
# Тест 3
# Входные данные:
# asdfghhzxcvb
# 
# Вывод программы:
# asdfghhzxcvb

s = input()
h_first = s.find("h")
h_last = s.rfind("h")

print(
		s[:h_first + 1]
		+
		s[h_first + 1: h_last].replace("h","H")
		+
		s[h_last:]
		)

