import re

def balancedParens(string):
  parensOpen = 0;
  curlyOpen = 0;
  brackOpen = 0;
  strippedString = re.sub(r"([^(){}[\]])", "", string)
  # return True

  # counter = {
  #   '(': 0,
  #   '{': 0,
  #   '[': 0,
  #   ')': '(',
  #   '}': '{',
  #   ']': '['
  # }

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

  # for x in range (len(strippedString)):
  #   char = strippedString[x]
  #   if (char == '(' or char == '{' or char == '['):
  #     counter[char] += 1
  #   elif (char == ')' or char == '}' or char == ']'):
  #     openChar = counter[char]
  #     if (counter[openChar] <= 0):
  #       return False
  #     counter[openChar] -= 1
  
  # if (counter['('] != 0 or counter['{'] != 0 or counter['['] != 0):
  #   return False
  # return True

print(balancedParens('([{}])'));
