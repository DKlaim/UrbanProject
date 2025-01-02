import calc
import unittest


class CalcTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
