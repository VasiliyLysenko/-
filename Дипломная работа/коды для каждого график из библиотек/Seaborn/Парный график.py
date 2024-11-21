import seaborn as sns               # Импортируем библиотеку Seaborn для создания визуализаций
import matplotlib.pyplot as plt       # Импортируем Matplotlib для построения графиков

# Загружаем набор данных Iris
iris = sns.load_dataset('iris')

# Создаем парный график (pairplot) с указанием цвета в зависимости от вида
sns.pairplot(iris, hue='species')

# Добавляем заголовок к графику, используя plt.suptitle для настройки заголовка целой фигуры
plt.suptitle('Парный график для данных Iris', y=1.02)  # y смещает заголовок вверх

# Отображаем график
plt.show()