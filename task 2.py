""" Решение 2 задания предпроф экзамена.
Программа читает файл данных, сортирует его по графе score с помощью вставок.
Она выводит первых 3х победителей, которые учатся в 10 классе.
 """

# Считываем данные из таблицы и записываем в список
file = open('students.csv', encoding='utf-8')
students_data = list(file)
file.close()

# Находим всех учеников из 10 класса, с которых нужно будет потом сортировать
# Их мы записываем в новый список
students_from_ten_grade = list()

for i in students_data:
    i = i.split(',')
    i[-1] = i[-1][:-1]
    if '10' in i[3] and i[-1] != 'None':
        students_from_ten_grade.append(i)

# Сортируем вставками получившийся список данных
for i in range(1, len(students_from_ten_grade)):
    if int(students_from_ten_grade[i][-1]) > int(students_from_ten_grade[i - 1][-1]):
        # Если эллементу необходима сортировка, то его перемещают на необходимую позицию с помощью вставки
        position = i
        while position != 0 and int(students_from_ten_grade[position][-1]) > \
                int(students_from_ten_grade[position - 1][-1]):
            # Обмен соседних элементов списка
            to_sort_elements = students_from_ten_grade[position]
            students_from_ten_grade[position] = students_from_ten_grade[position - 1]
            students_from_ten_grade[position - 1] = to_sort_elements
            position -= 1

# Формируем вывод, согласно требуемому формату из условия задачи
print("10 класс:")
for i in range(3):
    # Находим фамилию и имя из полученного списка
    full_name = students_from_ten_grade[i][1]
    full_name = full_name.split()
    name = full_name[1]
    second_name = full_name[0]
    print(f"{str(i + 1)} место: {name[0]}. {second_name}")
