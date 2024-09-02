'''
Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
'''
import Homework12_4
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            first = Homework12_4.Runner('Вася', -5)
            for _ in range(10):
                first.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(first.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            second = Homework12_4.Runner(['Илья'], 5)
            for _ in range(10):
                second.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(second.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = Homework12_4.Runner('Test Runner_1')
        runner2 = Homework12_4.Runner('Test Runner_2')
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
