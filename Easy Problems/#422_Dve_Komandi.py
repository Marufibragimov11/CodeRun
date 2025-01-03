"""
                                             422. Две команды
Студенты, разбившись на две команды, решали контест по программированию. Каждый студент решил не менее 1 и не более
N задач. Известно, что первая команда суммарно решила A задач, а вторая — B задач.
Определите, могло ли быть в первой команде больше студентов, чем во второй.

Формат ввода
Каждый тест состоит из трёх строк, где вводятся параметры теста, каждый в отдельной строке, — A,B,N(0≤A,B≤10000,1≤N≤10000).

Формат вывода
Выведите Yes, если в первой команде могло быть больше студентов, чем во второй, и No в противном случае.

Примечание
В первом тесте студенты первой команды решили 10 задач суммарно, а студенты второй команды решили 8 задач суммарно.
В первой команде могло быть 10 студентов, решивших по одной задаче, а во второй команде всего 8 студентов,
решивших по одной задаче, поэтому ответ Yes. Во втором тесте студенты первой команды решили 3 задачи,
а вторая команда решила 10 задач. Учитывая, что каждый студент решил не более 3 задач,
второй команде нужно было как минимум 4 студента. А значит, в ней точно больше студентов,
чем в первой команде, и ответ No.

Пример 1

Ввод   |   Вывод
10     |   Yes
8      |
2      |

Пример 2
Ввод   |   Вывод
3      |   No
10     |
3      |
"""


def more_students_in_first_team(A, B, N):
    min_students_team2 = (B + N - 1) // N

    if A > min_students_team2:
        return "Yes"
    else:
        return "No"


A = 10
B = 8
N = 2
print(more_students_in_first_team(A, B, N))

A = 3
B = 10
N = 3
print(more_students_in_first_team(A, B, N))
