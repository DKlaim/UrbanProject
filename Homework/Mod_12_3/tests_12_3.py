import unittest
import runner, runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name = runner.Runner('Имя')
        for _ in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name = runner.Runner('Имя')
        for _ in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name_1 = runner.Runner('Имя_1')
        name_2 = runner.Runner('Имя_2')
        for _ in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def run_tournament(self, tournament_name, *runners):
        tournament = runner_and_tournament.Tournament(90, *runners)
        result = {}
        for place, participant in tournament.start().items():
            result[place] = str(participant)
        self.all_results[tournament_name] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def check_last_runner(self, tournament_name, expected_last_runner):
        last_runner = list(self.all_results[tournament_name].values())[-1]
        self.assertEqual(last_runner, expected_last_runner)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        self.run_tournament('tournament_1', self.runner_1, self.runner_3)
        self.check_last_runner('tournament_1', 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        self.run_tournament('tournament_2', self.runner_2, self.runner_3)
        self.check_last_runner('tournament_2', 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        self.run_tournament('tournament_3', self.runner_1, self.runner_2, self.runner_3)
        self.check_last_runner('tournament_3', 'Ник')

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты:")
        for participants in cls.all_results.values():
            print(participants)


if __name__ == '__main__':
    unittest.main()
