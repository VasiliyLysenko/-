import plotly.express as px  # Импортируем Plotly Express для создания графиков

# Загрузка набора данных Iris
iris = px.data.iris()  # Загружаем встроенный набор данных Iris

# Создание интерактивного парного графика
fig = px.scatter_matrix(
    iris,
    dimensions=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],  # Указываем переменные для осей
    color='species',  # Цветовая кодировка по видам ирисов
    title='Интерактивный парный график для набора данных Iris'  # Устанавливаем заголовок
)

fig.show()  # Отображаем график