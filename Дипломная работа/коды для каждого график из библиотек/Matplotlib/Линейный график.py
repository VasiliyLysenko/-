import matplotlib.pyplot as plt  # Импортируем библиотеку Matplotlib для визуализации данных
import pandas as pd               # Импортируем библиотеку Pandas для работы с данными
import seaborn as sns            # Импортируем Seaborn для удобной работы с графиками

# Загрузка набора данных Iris
iris = sns.load_dataset('iris')

# Создание линейного графика
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика (ширина, высота)
plt.plot(iris['petal_length'],  # Данные для оси X (длина лепестка)
         iris['petal_width'],   # Данные для оси Y (ширина лепестка)
         marker='o',            # Указываем маркер для точек
         linestyle='-',         # Указываем стиль линии
         color='blue')          # Указываем цвет линии

# Добавление заголовка и меток осей
plt.title('Зависимость между длиной и шириной лепестка')
plt.xlabel('Длина лепестка (см)')
plt.ylabel('Ширина лепестка (см)')
plt.grid(True)  # Включаем отображение сетки

# Отображаем график на экране
plt.show()