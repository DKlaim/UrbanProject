import unittest
import calc
from random import randint


class NewCalcTest(unittest.TestCase):
    @unittest.skip('Причина: принудительное исключение теста')  # Пропуск тестов
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    @unittest.skipIf(randint(0, 1) == 0, 'Причина: условие == True')  # обратное skipIf - skipUnless
    def test_pow(self):
        self.assertEqual(calc.pow(3, 2), 9)


if __name__ == '__main__':
    unittest.main()
