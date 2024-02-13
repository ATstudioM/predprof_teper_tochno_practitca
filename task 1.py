"""
Решение первого задания предпроф экзамена.
Программа считывает данные из CSV файла, ищет совпадение по исходным данным о проекте и выдаёт оценку ученика.
После подсчитывает средний балл и заменяет в таблице результаты None на среднее значение по классу, после чего
сохраняет файл.
"""

from csv import reader, writer

# Читаем файл
table = open('students.csv', 'r', encoding='utf-8')
data = reader(table)
data = list(data)
table.close()

score = 0
counter = 0
empty_marks = dict()

# Находим оценку для Хадарова Владимира, а заодно ищем всех учеников без оценок. Их классы мы записываем в
# Словарь empty_marks
for i in range(1, len(data)):
    if 'Хадаров Владимир' in data[i][1]:
        print(f'Ты получил: {data[i][-1]} за проект - {data[i][0]}')
    if not data[i][-1].isdigit():
        empty_marks[data[i][3]] = [0, 0]

# Добавляем в словарь оценки одноклассников
for i in range(1, len(data)):
    if data[i][3] in empty_marks and data[i][-1].isdigit():
        empty_marks[data[i][3]][0] += int(data[i][-1])
        empty_marks[data[i][3]][1] += 1

# Замена всех None на среднее значение по классу
for i in range(1, len(data)):
    if not data[i][-1].isdigit():
        data[i][-1] = str(round(empty_marks[data[i][3]][0] / empty_marks[data[i][3]][1], 3))

# Запись в новую таблицу
table = open('students_new.csv', 'w', encoding='utf-8')
writing = writer(table, delimiter=',', quotechar=';')
writing.writerows(data)
table.close()
