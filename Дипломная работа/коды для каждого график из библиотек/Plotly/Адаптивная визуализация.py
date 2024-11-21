import plotly.express as px  # Импортируем библиотеку Plotly Express для визуализации данных
import pandas as pd          # Импортируем библиотеку Pandas для работы с данными

# Загружаем набор данных Iris из библиотеки Plotly Express
df = px.data.iris()

# Создаем диаграмму разброса с использованием данных Iris
fig = px.scatter(df,
                 x='sepal_width',      # Задаем ширину чашелистика для оси X
                 y='sepal_length',     # Задаем длину чашелистика для оси Y
                 color='species',      # Задаем цвет маркеров в зависимости от вида ириса
                 title='Адаптивный график Iris')  # Заголовок графика

# Отображаем график на экране
fig.show()