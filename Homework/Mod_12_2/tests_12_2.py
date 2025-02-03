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

    def test_start_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = {}
        for place, participant in tournament.start().items():
            result[str(place)] = str(participant)
        self.all_results['tournament_1'] = result

    def test_start_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = {}
        for place, participant in tournament.start().items():
            result[str(place)] = str(participant)
        self.all_results['tournament_2'] = result

    def test_start_3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = {}
        for place, participant in tournament.start().items():
            result[str(place)] = str(participant)
        self.all_results['tournament_3'] = result

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты:")
        for participants in cls.all_results.values():
            print(participants)


if __name__ == '__main__':
    unittest.main()
