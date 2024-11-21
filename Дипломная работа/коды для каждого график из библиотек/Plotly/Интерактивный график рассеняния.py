import plotly.express as px  # Импортируем Plotly Express для создания графиков
import pandas as pd          # Импортируем Pandas для работы с данными

# Загрузка набора данных Iris
iris = px.data.iris()  # Загружаем встроенный набор данных Iris

# Создание интерактивного графика рассеяния
fig = px.scatter(
    iris,
    x='petal_length',  # Ось X - длина лепестка
    y='petal_width',   # Ось Y - ширина лепестка
    color='species',   # Цветовая кодировка по видам ирисов
    title='Интерактивный график рассеяния: Длина и ширина лепестка',
    labels={
        'petal_length': 'Длина лепестка (см)',
        'petal_width': 'Ширина лепестка (см)'
    }
)

fig.show()  # Отображаем график