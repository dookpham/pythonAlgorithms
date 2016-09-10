import unittest
from balancedParens import balancedParens

class SomeTests(unittest.TestCase):
  def test_balancedParens(self):
    self.assertTrue(balancedParens('([{}])'))
    self.assertFalse(balancedParens('({[}])'))

  def test_upper(self):
    self.assertEqual('dude'.upper(), 'DUDE')

  def test_isupper(self):
    self.assertTrue('DUDE'.isupper())
    self.assertFalse('DudE'.isupper())

suite = unittest.TestLoader().loadTestsFromTestCase(SomeTests)
unittest.TextTestRunner(verbosity=2).run(suite)