# Дана строка. Удалите из этой строки все символы @.
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
# Bilbo.Baggins@bagend.hobbiton.shire.me
# 
# Вывод программы:
# Bilbo.Bagginsbagend.hobbiton.shire.me
# 
# 
# 
# Тест 2
# Входные данные:
# dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh
# 
# Вывод программы:
# dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh
# 
# 
# 
# Тест 3
# Входные данные:
# @
# 
# Вывод программы:
	
s = input()
print(s.replace("@",""))
