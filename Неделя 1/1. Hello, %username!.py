# Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов. Изображение одного пингвина
# имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается
# вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду
# разработки.
# =================================
# Формат ввода
#
# Вводится натуральное число.
# =================================
# Формат вывода
#
# Выведите ответ на задачу.
# =================================
# Примечания
#
# В задачах нашего курса не нужно проверять ограничения входных данных: гарантируется, что введут данные,
# соответствующие условию. Т. е. например в этой задаче введенное число N точно будет не меньше 1 и не больше 9.
# Напоминаем, что во всех задачах этого курса решения должны выдавать в точности требуемый ответ. В частности, не надо
# выводить призыв к вводу вроде "Введите количество пингвинов". Пожалуйста, протестируйте свое решение на примерах
# ввода/вывода, а также придумайте свои удовлетворяющие условию примеры и протестируйте свое решение на них.
# Учтите, что вывод данных на экран производится построчно, а не попингвинно.
# Не забудьте, что для вывода бекслеша надо написать два бекслеша подряд.
# Эта задача относительно сложная. Вы можете пока что ее пропустить, и вернуться позже.
# =================================
# Примеры
#
# Тест 1
# Входные данные:
# 3
#
# Вывод программы:
#    _~_       _~_       _~_
#   (o o)     (o o)     (o o)
#  /  V  \   /  V  \   /  V  \
# /(  _  )\ /(  _  )\ /(  _  )\
#   ^^ ^^     ^^ ^^     ^^ ^^
#
#
#
# Тест 2
# Входные данные:
# 1
#
# Вывод программы:
#    _~_
#   (o o)
#  /  V  \
# /(  _  )\
#   ^^ ^^

kolvo = input()
i = 1
s1 = "   _~_"
s2 = "  (o o)"
s3 = " /  V  \\"
s4 = "/(  _  )\\"
s5 = "  ^^ ^^"
while i < int(kolvo):
    s1 = s1 + "       _~_"
    s2 = s2 + "     (o o)"
    s3 = s3 + "   /  V  \\"
    s4 = s4 + " /(  _  )\\"
    s5 = s5 + "     ^^ ^^"
    i = i + 1
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
