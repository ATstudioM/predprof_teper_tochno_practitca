""""""

from csv import writer


def genereate_hash(name):
    """
    Функция просчитывает хэш по формуле из задания
    :param name:
    Строка, сождержащая информацию об имени, фамилии и отчестве человека
    :return:
    Целое число, которое является хэшем
    """
    p = 67
    m = 10 ** 9 + 9
    alphabet = '!абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    name = name.replace(' ', '')
    value = 0
    for i in range(len(name)):
        value = (value + alphabet.find(name[i]) * p ** i) % m
    return value


# Считываем данные из таблицы и записываем в список
file = open('students.csv', encoding='utf-8')
students_data = list(file)
file.close()

# Приводим все строки в считанной таблице в нужный для нас вид
for i in range(0, len(students_data)):
    students_data[i] = students_data[i].split(',')
    students_data[i][-1] = students_data[i][-1][:1]

# Меняем id учащихся на новый хэш
for i in range(1, len(students_data)):
    students_data[i][0] = genereate_hash(students_data[i][1])

# Записываем всё в новую таблицу
table = open('students_with_hash.csv', 'w')
writing = writer(table, delimiter=',', quotechar=';')
writing.writerows(students_data)
table.close()