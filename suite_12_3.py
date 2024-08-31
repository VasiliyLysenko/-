import runner as r1
import runner2 as r2
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = r1.Runner('Test Runner1')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = r1.Runner('Test Runner2')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = r1.Runner('Test Runner2')
        for _ in range(10):
            runner3.walk()
            runner3.run()
        self.assertNotEqual(runner3.walk, runner3.run)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Инициализация атрибута класса для хранения результатов всех тестов

    def setUp(self):
        self.runner1 = r2.Runner("Усэйн", speed=10)  # скорость 10
        self.runner2 = r2.Runner("Андрей", speed=9)  # скорость 9
        self.runner3 = r2.Runner("Ник", speed=3)  # скорость 3


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Инициализация атрибута класса для хранения результатов всех тестов

    def setUp(self):
        self.runner1 = r2.Runner("Усэйн", speed=10)  # скорость 10
        self.runner2 = r2.Runner("Андрей", speed=9)  # скорость 9
        self.runner3 = r2.Runner("Ник", speed=3)  # скорость 3

    @classmethod
    def tearDownClass(cls):
        for name, time in cls.all_results.items():
            print(f"{name}: {time}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usein_nik(self):
        tournament = r2.Tournament(90, self.runner1, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_nik(self):
        tournament = r2.Tournament(90, self.runner2, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_usein_nik(self):
        tournament = r2.Tournament(90, self.runner2, self.runner1, self.runner3)
        all_results = tournament.start()
        last_runner = max(all_results.keys())
        self.assertTrue(all_results[last_runner].name == "Ник")
