import plotly.express as px  # Импортируем Plotly Express для создания графиков

# Загрузка набора данных Iris
iris = px.data.iris()  # Загружаем встроенный набор данных Iris

# Создание интерактивного 3D-графика
fig = px.scatter_3d(
    iris,
    x='sepal_length',  # Ось X - длина чашелистика
    y='sepal_width',   # Ось Y - ширина чашелистика
    z='petal_length',  # Ось Z - длина лепестка
    color='species',       # Цветовая кодировка по видам ирисов
    title='3D-график: Длина и ширина чашелистика'   # Заголовок графика
)

fig.show()  # Отображаем график