import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    def run_tournament(self, tournament_name, *runners):
        tournament = runner_and_tournament.Tournament(90, *runners)
        result = {}
        for place, participant in tournament.start().items():
            result[place] = str(participant)
        self.all_results[tournament_name] = result

    def test_tournament_1(self):
        self.run_tournament('tournament_1', self.runner_1, self.runner_3)
        last_runner = list(self.all_results['tournament_1'].values())[-1]
        expected_last_runner = 'Ник'
        self.assertTrue(last_runner == expected_last_runner)

    def test_tournament_2(self):
        self.run_tournament('tournament_2', self.runner_2, self.runner_3)
        last_runner = list(self.all_results['tournament_2'].values())[-1]
        expected_last_runner = 'Ник'
        self.assertTrue(last_runner == expected_last_runner)

    def test_tournament_3(self):
        self.run_tournament('tournament_3', self.runner_1, self.runner_2, self.runner_3)
        last_runner = list(self.all_results['tournament_3'].values())[-1]
        expected_last_runner = 'Ник'
        self.assertTrue(last_runner == expected_last_runner)

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты:")
        for participants in cls.all_results.values():
            print(participants)


if __name__ == '__main__':
    unittest.main()
