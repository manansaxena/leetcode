## MY solution recursion
from os import *
from sys import *
from collections import *
from math import *

def helper(arr1, arr2, result):
	if len(arr1) == 0 and len(arr2) == 0:
		return
	if len(arr2) == 0:
		result.extend(arr1)
		return
	if len(arr1) == 0:
		result.extend(arr2)
		return
	if arr1[0] >= arr2[0]:
		result.append(arr2[0])
		helper(arr1,arr2[1:], result)
	else:
		result.append(arr1[0])
		helper(arr1[1:],arr2, result)
	return


def findKthElement(arr1, arr2, k):
	result = []
	helper(arr1, arr2, result)
	return result[k-1]


## Their solution (no recursion)
'''

    Time Complexity: O((M + N) * log(M + N))
    Space Complexity: O(M + N)

    Where M is the size of the array/list 'ARR1' and N is the size of 'ARR2'.
    
'''

def findKthElement(arr1, arr2, k):
    m = len(arr1)
    n = len(arr2)

    arr3 = [0] * (m + n)

    # Merging 'ARR1' and 'ARR2' in 'ARR3'.
    for i in range(m):
        arr3[i] = arr1[i]

    for i in range(n):
        arr3[i + m] = arr2[i]

    # We need to sort the new array.
    arr3.sort()
    return arr3[k - 1]
