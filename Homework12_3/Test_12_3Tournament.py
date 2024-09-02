
import Homework12_3
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner1 = Homework12_3.Runner('Усэйн', 10)
        self.runner2 = Homework12_3.Runner('Андрей', 9)
        self.runner3 = Homework12_3.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{value}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament = Homework12_3.Tournament(90, self.runner1, self.runner3)
        self.all_results['test_tournament1'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament1')).get(max(self.all_results.get('test_tournament1')))
                        == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament = Homework12_3.Tournament(90, self.runner2, self.runner3)
        self.all_results['test_tournament2'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament2')).get(max(self.all_results.get('test_tournament2')))
                        == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament = Homework12_3.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['test_tournament3'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament3')).get(max(self.all_results.get('test_tournament3')))
                        == self.runner3.name)


if __name__ == '__main__':
    unittest.main()
