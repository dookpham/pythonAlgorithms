#Write an algorithm such that if 

def zeroMatrix(arr):
  colZeros = {}
  rowZeros = {}
  m = len(arr)
  n = len(arr[0])
  for x in range (m):
    print(arr[x])
    for y in range (n):
      if (arr[x][y] == 0):
        rowZeros[x] = True
        colZeros[y] = True
  for key in rowZeros:
    arr[key] = [0 for x in range(n)]
  for key in colZeros:
    for x in range (m):
      arr[x][key] = 0
  print('-------------------')
  for x in range (m):
    print(arr[x])


zeroMatrix([
[ 1, 2, 3, 4, 5],
[45, 8, 2, 0, 4], 
[ 1, 2, 3, 4, 0]
])
