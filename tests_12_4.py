'''Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:

Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
Test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
'''

from rt_with_exceptions import Runner
import logging
import unittest

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="UTF-8",
    format="%(asctime)s | %(levelname)s | %(message)s")
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Создаём объект Runner с отрицательной скоростью
            runner = Runner(name="Вася", speed=-5)

            # Логируем успешное выполнение теста
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            # Создаём объект Runner с ошибочным именем
            runner = Runner(name=123, speed=5)

            # Логируем успешное выполнение теста
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning('Неверный тип имени для Runner', exc_info=True)

if __name__ == "__main__":
    unittest.main()