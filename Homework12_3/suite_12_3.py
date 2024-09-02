import unittest
import Test_12_3Runner
import Test_12_3Tournament

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_12_3Runner.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_12_3Tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)