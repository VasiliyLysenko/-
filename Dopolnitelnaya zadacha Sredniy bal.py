# Даны список из оценок и множество из студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем пустой словарь

dict_students = {}

# Переводим множество в список для извлечения значений по индексу
list_students = list(students)

# Создаем переменные для каждого студента с их средним балом

a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])

# Добавляем пары в словарь и вывод на экран

dict_students.update({'Aaron': a,
                      'Bilbo': b,
                      'Johnny': c,
                      'Khendrik': d,
                      'Steve': e})
print(dict_students)
