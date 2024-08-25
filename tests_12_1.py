import runner
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = runner.Runner('Test Runner1')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = runner.Runner('Test Runner2')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = runner.Runner('Test Runner3')
        for _ in range(10):
            runner3.walk()
        for _ in range(10):
            runner3.run()
        self.assertNotEqual(runner3.walk, runner3.run)

if __name__ == '__main__':
    unittest.main()
