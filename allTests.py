import unittest
import runTests
# from balancedParens import balancedParens


# class SomeTests(unittest.TestCase):
#   def test_balancedParens(self):
#     self.assertTrue(balancedParens('([{}])'), 'error message here')
#     self.assertFalse(balancedParens('({[}])'))

#   def test_upper(self):
#     self.assertEqual('dude'.upper(), 'DUDE')

#   def test_isupper(self):
#     self.assertTrue('DUDE'.isupper())
#     self.assertFalse('DudE'.isupper())

# class MoreTests(unittest.TestCase):
#   def test_more(self):
#     self.assertTrue(True)    



# suite = unittest.TestLoader().loadTestsFromTestCase(SomeTests, MoreTests)
# unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == 'main':
  allsuites = unittest.TestSuite([runTests.suite])