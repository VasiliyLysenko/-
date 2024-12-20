import plotly.graph_objects as go  # Импортируем библиотеку Plotly для создания интерактивных графиков

# Определение меток и значений для круговой диаграммы
labels = ['A', 'B', 'C']            # Категории
values = [4500, 2500, 1050]         # Соответствующие значения для каждой категории

# Создание фигуры круговой диаграммы
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Настройка заголовка круговой диаграммы
fig.update_layout(title='Круговая диаграмма')

# Отображение диаграммы
fig.show()