import seaborn as sns                # Импортируем библиотеку Seaborn для создания высококачественных графиков
import matplotlib.pyplot as plt        # Импортируем библиотеку Matplotlib для построения графиков
import numpy as np                    # Импортируем NumPy для работы с массивами и генерации случайных данных

# Генерируем случайные данные размером 8x10 для тепловой карты
data = np.random.rand(8, 10)        # Создаем массив из 8 строк и 10 столбцов случайных чисел от 0 до 1

# Создаем тепловую карту
sns.heatmap(data, cmap='YlGnBu', annot=True,  fmt=".2f", linewidths=.5)      # cmap задает цветовую палитру (от светло-зеленого до темно-синего)

# Устанавливаем заголовок для графика
plt.title('Тепловая карта')           # Заголовок графика

# Отображаем график
plt.show()                            # Выводим тепловую карту на экран