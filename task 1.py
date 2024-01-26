"""
Решение первого задания предпроф экзамена.
Программа считывает данные из CSV файла, ищет совпадение по исходным данным о проекте и выдаёт оценку ученика.
После подсчитывает средний балл и заменяет в таблице результаты None на среднее значение по классу, после чего
сохраняет файл.
"""

from csv import reader, writer

table = open('students.csv', 'r')
data = reader(table)
data = list(data)
table.close()

score = 0
counter = 0
for i in range(len(data)):
    if 'Матыгуллин Адель' in data[i][1]:
        print(f'Ты получил: {data[i][-1]} за проект - {data[i][0]}')
    if data[i][-1].isdigit():
        score += int(data[i][-1])
        counter += 1

score = round(score / counter, 3)

for i in range(len(data)):
    if data[i][-1] == 'None':
        data[i][-1] = str(score)

table = open('students_new.csv', 'w')
writing = writer(table, delimiter=',', quotechar=';')
writing.writerows(data)
table.close()
