import re
import unittest

def balancedParens(string):
  parensOpen = 0;
  curlyOpen = 0;
  brackOpen = 0;
  strippedString = re.sub(r"([^(){}[\]])", "", string)

  openChars = {
    '(': True,
    '{': True,
    '[': True
  }

  closedChars = {
    '}': '{',
    ')': '(',
    ']': '['
  }

  openCharStack = []
  for x in range (len(strippedString)):
    char = strippedString[x]
    if (char in openChars):
      openCharStack.append(char)
    else :
      pair = closedChars[char]
      popped = openCharStack.pop()
      if (pair != popped):
        return False
  print(openCharStack)
  if (len(openCharStack) > 0):
    return False
  else: 
    return True

print(balancedParens('([{}])'));

class SomeTests(unittest.TestCase):
  def test_upper(self):
    self.assertEqual('dude'.upper(), 'DUDE')

  def test_isupper(self):
    self.assertTrue('DUDE'.isupper())
    self.assertFalse('DudE'.isupper())

suite = unittest.TestLoader().loadTestsFromTestCase(SomeTests)
unittest.TextTestRunner(verbosity=2).run(suite)
