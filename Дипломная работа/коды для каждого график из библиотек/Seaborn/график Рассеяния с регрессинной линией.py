import seaborn as sns           # Импортируем библиотеку Seaborn для визуализации данных
import matplotlib.pyplot as plt   # Импортируем библиотеку Matplotlib для построения графиков

# Создание графика рассеяния с регрессионной линией
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика (ширина 10 дюймов, высота 6 дюймов)
sns.regplot(
    x='petal_length',         # Ось X - длина лепестка
    y='petal_width',          # Ось Y - ширина лепестка
    data=sns.load_dataset('iris'),  # Данные из набора данных Iris
    scatter_kws={'s': 50},              # Устанавливаем размер маркеров в рассеянии
    line_kws={'color': 'red'}          # Устанавливаем цвет регрессионной линии (красный)
)

# Настройка заголовка и меток осей
plt.title('График рассеяния: Длина и ширина лепестка с регрессионной линией')
plt.xlabel('Длина лепестка (см)')
plt.ylabel('Ширина лепестка (см)')
plt.grid(True)               # Включаем отображение сетки

# Отображаем график на экране
plt.show()