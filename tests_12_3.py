import suite_12_3 as suite
import unittest

testST = unittest.TestSuite()
# testST.addTest(unittest.makeSuite(suite.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(suite.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(suite.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)




