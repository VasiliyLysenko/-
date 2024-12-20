import seaborn as sns           # Импортируем библиотеку Seaborn для визуализации данных
import matplotlib.pyplot as plt   # Импортируем библиотеку Matplotlib для построения графиков

# Вычисление матрицы корреляции
iris = sns.load_dataset('iris')
correlation_matrix = iris.select_dtypes(include=['float64', 'int64']).corr()  # Загружаем данные и вычисляем корреляцию

# Создание тепловой карты для матрицы корреляции
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика (ширина 10 дюймов, высота 6 дюймов)
sns.heatmap(
    correlation_matrix,                      # Подаем на вход матрицу корреляции
    annot=True,                              # Включаем отображение значений корреляции на графике
    fmt=".2f",                          # Форматируем отображение значений с 2 знаками после запятой
    cmap='coolwarm',                    # Устанавливаем цветовую палитру 'coolwarm'
    square=True)                          # Обеспечиваем квадратную ячейку

# Настройка заголовка графика
plt.title('Тепловая карта корреляции между переменными')
plt.show()  # Показываем график на экране