import unittest
import tests_12_3

superTS = unittest.TestSuite()

# Список тестов
superTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
superTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Запуск тестов
runner = unittest.TextTestRunner(verbosity=2)  # verbosity меняет детализацию теста (выводит какие тесты пройдены)
runner.run(superTS)
