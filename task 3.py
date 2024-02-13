""" Решение 3 задания предпроф экзамена.
Программа читает файл данных и ищет среди всех проектов заданный при вводе.
Потом она выдаёт на вывод имя и фамилию в необходимом формате
 """

# Считываем данные из таблицы и записываем в список
file = open('students.csv', encoding='utf-8')
students_data = list(file)
file.close()

# Приводим все строки в считанной таблице в нужный для нас вид
for i in range(1, len(students_data)):
    students_data[i] = students_data[i].split(',')

while True:
    # Ждём ввод от пользователя с номером проекта
    project_number = input()
    # При вводе СТОП мы завершаем работу прорграммы
    if project_number == "СТОП":
        break
    # Ищем необходимый проект
    done = 0
    counter = -1
    for i in range(1, len(students_data)):
        if students_data[i][0] == project_number:
            # Готовим данные к правильному выводу
            # Находим фамилию и имя из полученного списка
            full_name = students_data[i][1]
            full_name = full_name.split()
            name = full_name[1]
            second_name = full_name[0]
            print(f"Проект №{project_number} делал(а): {name[0]}. {second_name}")
            print(f"он(а) получил(а) оценку - {students_data[i][-1][:-1]}")
            done = 1
            break
    # Если проект не был найден, то мы пишем об этом пользователю
    if done == 0:
        print("Ничего не найдено.")
