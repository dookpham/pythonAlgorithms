import re

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


