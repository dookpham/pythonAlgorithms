def every(arr, fn):
  return reduce(lambda p, c: (p and fn(c)), arr, True)
  
def some(arr, fn):
  return reduce(lambda p, c: (p or fn(c)), arr, False)

def removeDuplicates(arr):
  return list(set(arr))


