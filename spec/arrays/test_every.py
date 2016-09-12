import unittest
from src.arrays import every

class TestEvery(unittest.TestCase):
  def test_one(self):
    def equals5(val):
      return val == 5
    self.assertTrue(every([5,5], equals5), 'error message here')


suite = unittest.TestLoader().loadTestsFromTestCase(TestEvery)
unittest.TextTestRunner(verbosity=2).run(suite)