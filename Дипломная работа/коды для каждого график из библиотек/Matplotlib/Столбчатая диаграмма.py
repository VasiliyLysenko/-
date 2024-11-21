import matplotlib.pyplot as plt  # Импортируем библиотеку Matplotlib для визуализации данных
import pandas as pd  # Импортируем библиотеку Pandas для работы с данными
import seaborn as sns  # Импортируем Seaborn для удобной работы с графиками

# Загрузка набора данных Iris
iris = sns.load_dataset('iris')

# Вычисление средней ширины чашелистика по видам ирисов
avg_sepal_width = iris.groupby('species')['sepal_width'].mean().reset_index()

# Создание столбчатой диаграммы
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика (ширина, высота)
plt.bar(avg_sepal_width['species'],  # Названия видов ирисов для оси X
        avg_sepal_width['sepal_width'],  # Средняя ширина чашелистика для оси Y
        color='lightgreen')  # Задаем цвет столбцов

# Добавление заголовка и меток осей
plt.title('Средняя ширина чашелистика по видам ирисов')
plt.xlabel('Вид ириса')
plt.ylabel('Средняя ширина чашелистика (см)')
plt.xticks(rotation=15)  # Поворачиваем метки по оси X для удобства чтения
plt.grid(axis='y')  # Включаем отображение сетки по оси Y

# Отображаем график на экране
plt.show()
