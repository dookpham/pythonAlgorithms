import math
# /*
#  * Given a sorted array, find the index of an element
#  * using a binary search algorithm.
#  *
#  * Example usage:
#  *
#  * var index = binarySearch([1, 2, 3, 4, 5], 4);
#  * console.log(index); // 3
#  */

def binarySearch (array, target) :
  left = 0
  right = len(array);
  midpt = math.floor((right - left) / 2)
  value = array[midpt]

  # print(left, right, midpt, value)

  while (target != value) :
    if (left == right - 1) :
      return None
    elif (target > value) :
      left = midpt
    else :
      right = midpt
    midpt = left + math.floor((right - left) / 2)
    value = array[midpt] 

  return midpt

result = binarySearch([0,2,3,4,5], 0)
print(result)

