import unittest
from src.arrays import *

class TestArrays(unittest.TestCase):
  
  #every
  def test_1(self):
    def equals5(val):
      return val == 5
    self.assertTrue(every([5,5,5,5], equals5), 'error message here')

  def test_2(self):
    def equals7(val):
      return val == 7
    self.assertFalse(every([5,5,6,7], equals7), 'error message here')

  #some
  def test_some1(self):
    def equals5(val):
      return val == 5
    self.assertTrue(some([4,5,6,7], equals5), 'error message here')

  def test_some2(self):
    def equals7(val):
      return val == 7
    self.assertFalse(some([5,5,6,8], equals7), 'error message here')


suite = unittest.TestLoader().loadTestsFromTestCase(TestArrays)
unittest.TextTestRunner(verbosity=2).run(suite)
