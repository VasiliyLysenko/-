import runner_2
import unittest
class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Инициализация атрибута класса для хранения результатов всех тестов

    def setUp(self):
        self.runner1 = runner_2.Runner("Усэйн", speed=10)  # скорость 10
        self.runner2 = runner_2.Runner("Андрей", speed=9)  # скорость 9
        self.runner3 = runner_2.Runner("Ник", speed=3)  # скорость 3

    @classmethod
    def tearDownClass(cls):
        # Вывод результатов всех тестов
        print("\nРезультаты всех тестов:")
        for name, time in cls.all_results.items():
            print(f"{name}: {time}")
            
    def test_race_usein_nik(self):
        tournament = runner_2.Tournament(90, self.runner1, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")

    def test_race_andrey_nik(self):
        tournament = runner_2.Tournament(90, self.runner2, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")

    def test_race_andrey_usein_nik(self):
        tournament = runner_2.Tournament(90, self.runner2, self.runner1, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")

if __name__ == "__main__":
    unittest.main()


