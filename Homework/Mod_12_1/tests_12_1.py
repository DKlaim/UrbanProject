import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Test for walk method in runner
        :return:
        """
        name = runner.Runner('Имя')
        for _ in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        """
        Test for run method in runner
        :return:
        """
        name = runner.Runner('Имя')
        for _ in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        """
        Test for run and walk methods in runner
        :return:
        """
        name_1 = runner.Runner('Имя_1')
        name_2 = runner.Runner('Имя_2')
        for _ in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


if __name__ == '__main__':
    unittest.main()
