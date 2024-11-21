import seaborn as sns                # Импортируем библиотеку Seaborn для визуализации данных
import matplotlib.pyplot as plt        # Импортируем Matplotlib для построения графиков
import numpy as np                    # Хотя в данном случае NumPy не используется, его можно импортировать для возможных дальнейших операций

# Загружаем набор данных Iris
iris = sns.load_dataset('iris')

# Создаем коробчатую диаграмму (boxplot)
sns.boxplot(x='species', y='sepal_length', data=iris)

# Устанавливаем заголовок для графика
plt.title('Коробчатая диаграмма')

# Отображаем график
plt.show()