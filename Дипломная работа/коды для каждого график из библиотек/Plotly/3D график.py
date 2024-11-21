import plotly.graph_objects as go    # Импортируем библиотеку Plotly для создания интерактивных графиков

# Создаем 3D график рассеяния
fig = go.Figure(data=[go.Scatter3d(
    x=[1, 2, 3],  # Координаты по оси X
    y=[4, 5, 6],  # Координаты по оси Y
    z=[7, 8, 9],  # Координаты по оси Z
    mode='markers'  # отображаем только маркеры
)])

# Настройка макета графика, включая заголовок и подписи осей
fig.update_layout(
    title='3D График',
    scene=dict(
        xaxis_title='X',  # Заголовок оси X
        yaxis_title='Y',  # Заголовок оси Y
        zaxis_title='Z'   # Заголовок оси Z
    )
)

# Отображение графика
fig.show()