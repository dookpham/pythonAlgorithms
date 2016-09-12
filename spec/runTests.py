import unittest
from balancedParens import balancedParens

class AllTests(unittest.TestCase):
  def test_balancedParens(self):
    self.assertTrue(balancedParens('([{}])'), 'error message here')
    self.assertFalse(balancedParens('({[}])'))

  def test_upper(self):
    self.assertEqual('dude'.upper(), 'DUDE')

  def test_isupper(self):
    self.assertTrue('DUDE'.isupper())
    self.assertFalse('DudE'.isupper())

suite = unittest.TestLoader().loadTestsFromTestCase(AllTests)
# def suite():
  # suite = unittest.TestSuite

unittest.TextTestRunner(verbosity=2).run(suite)