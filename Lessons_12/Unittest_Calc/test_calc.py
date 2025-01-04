# Понятия и термины в Юнит-тестировании:
# Фикстура - это отдельный метод в котором реализовано определённое тестовое действие и вывод результата.
# Тест-Кейс - это отдельный класс с набором действий/тестов/фикстур.
# Тест-Сьют - это отдельный класс с набором Тест-Кейсов для объединения тестов в группы.
# Тест-ранер - компонент, который отвечает за запуск тестирования и всю логику/структуру тестирования.
import calc
import unittest


class CalcTest(unittest.TestCase):
    def setUp(self):  # метод setUp - функция, которая выполняется перед каждой фикстурой
        print('UpSetup')
    # setUp - то что происходит перед каждым кейсом

    @classmethod
    def setUpClass(cls):  # метод setUpClass - функция, которая выполняется 1 раз в самом начале запуска теста (используется с декоратором @classmethod)
        print('UpMegaSetup')
    # setUpClass - то что происходит перед каждым тест-кейсом

    def tearDown(self):  # метод tearDown - функция, которая выполняется после каждой фикстуры
        print('DownSetup')
    # tearDown - то что происходит после каждого кейса

    @classmethod
    def tearDownClass(cls):  # метод tearDownClass - функция, которая выполняется 1 раз в самом конце теста (используется с декоратором @classmethod)
        print('DownMegaSetup')
    # tearDownClass - то что происходит после каждого тест-кейса

    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calc.add(2, 2), 4)

    def test_sub(self):
        """
        Test for sub function in calculator
        :return:
        """
        self.assertEqual(calc.sub(2, 2), 0)

    def test_mul(self):
        """
        Test for mul function in calculator
        :return:
        """
        self.assertEqual(calc.mul(2, 2), 4)

    def test_div(self):
        """
        Test for div function in calculator
        :return:
        """
        self.assertEqual(calc.div(2, 2), 1)

    def test_test(self):  # Другие функции сравнения
        # self.assertIsNone('')  # Проверка на пустоту
        self.assertIsNotNone('abc')  # Проверка на не пустоту
        self.assertIn('a', 'abc')   # Проверка на содержание
        self.assertTrue(True)   # Проверка на Истину
        self.assertFalse(False)   # Проверка на Лож
        # self.assertRaises(1 / 0)   # Проверка на вызов ошибки
        self.assertAlmostEquals(0.0000001, 0.0000001)   # Сравнение с точностью до 7 знака после точки
        # А также больше/меньше и т.п.


if __name__ == '__main__':
    unittest.main()
