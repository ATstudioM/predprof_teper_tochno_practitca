"""

"""

from random import randint, choice, shuffle
from csv import writer


def generate_password(lenght):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    numbers = '0123456789'
    password = []
    big_letters = randint(2, 4)
    small_letters = randint(1, 3)
    for _ in range(big_letters):
        password.append(choice(letters).upper())
    for _ in range(small_letters):
        password.append(choice(letters))
    for _ in range(lenght - small_letters - big_letters):
        password.append(choice(numbers))
    shuffle(password)
    result = ''
    for i in password:
        result += i
    return result


def generate_login(name):
    if len(name) >= 3:
        login = name[0] + "_" + name[1][0] + name[2][0]
    else:
        login = name[0] + "_" + name[1][0]
    return login


# Считываем данные из таблицы и записываем в список
file = open('students.csv')
students_data = list(file)
file.close()

# Приводим все строки в считанной таблице в нужный для нас вид
for i in range(0, len(students_data)):
    students_data[i] = students_data[i].split(',')
    students_data[i][-1] = students_data[i][-1][:1]


students_data[0].append('login')
students_data[0].append('password')


for i in range(1, len(students_data)):
    students_data[i].append(generate_login(students_data[i][1]))
    students_data[i].append(generate_password(8))

# Запись в новую таблицу
table = open('students_with_password.csv', 'w')
writing = writer(table, delimiter=',', quotechar=';')
writing.writerows(students_data)
table.close()
