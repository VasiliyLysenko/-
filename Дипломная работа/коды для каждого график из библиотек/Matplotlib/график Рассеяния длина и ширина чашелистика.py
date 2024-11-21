import matplotlib.pyplot as plt  # Импортируем библиотеку Matplotlib для визуализации данных
import pandas as pd               # Импортируем библиотеку Pandas для работы с данными
import seaborn as sns            # Импортируем Seaborn для удобной работы с графиками

# Загрузка набора данных Iris
iris = sns.load_dataset('iris')

# Создание графика рассеяния
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика (ширина 10 дюймов, высота 6 дюймов)
scatter = plt.scatter(
    iris['sepal_length'],              # Данные для оси X (длина чашелистика)
    iris['sepal_width'],               # Данные для оси Y (ширина чашелистика)
    c=iris['species'].astype('category').cat.codes,  # Кодируем виды ирисов для цветовой окраски
    cmap='viridis',                    # Используем цветовую карту 'viridis'
    alpha=0.7                         # Устанавливаем прозрачность точек
)

# Настройка заголовка и меток осей
plt.title('График рассеяния: Длина и ширина чашелистика')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')

# Добавление цветовой шкалы
plt.colorbar(scatter, ticks=[0, 1, 2], label='Вид ириса', format='%d')  # Добавляем colorbar для обозначения видов

plt.grid(True)  # Включаем отображение сетки
plt.show()      # Отображаем график на экране