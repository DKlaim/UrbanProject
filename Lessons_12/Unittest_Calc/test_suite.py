""" Систематизация тестов + Пропуск тестов """

import unittest
import test_calc, test_new_calc

calcTS = unittest.TestSuite()
# calcTS.addTest(unittest.makeSuite(test_calc.CalcTest))  # устаревший метод
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

# runner = unittest.TextTestRunner()
runner = unittest.TextTestRunner(verbosity=2)  # verbosity меняет детализацию теста (выводит какие тесты пройдены)
runner.run(calcTS)
