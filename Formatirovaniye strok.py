# Переменные
team1_num = 5
team2_num = 6
score_2 = 42
team1_time = 18015.2
score_1 = 40
challenge_result = "победа команды Мастера кода"
tasks_total = 82
time_avg = 350.4

# Использование %
team1_message = "В команде Мастера кода участников: %d !" % team1_num
teams_message = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Использование format()
score_2_message = "Команда Волшебники данных решила задач: {} !".format(score_2)
team2_time_message = "Волшебники данных решили задачи за {} с !".format(team1_time)

# Использование f-строк
teams_scores_message = f"Команды решили {score_1} и {score_2} задач."
challenge_result_message = f"Результат битвы: {challenge_result}!"
tasks_message = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

# Вывод результатов
print(team1_message)
print(teams_message)
print(score_2_message)
print(team2_time_message)
print(teams_scores_message)
print(challenge_result_message)
print(tasks_message)