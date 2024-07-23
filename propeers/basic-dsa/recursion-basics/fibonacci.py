## Basic Recursion
from typing import List

def helper(n):
    if n == 0 or n == 1:
        return n
    return helper(n-1) + helper(n-2)

def generateFibonacciNumbers(n: int) -> List[int]: 
    result = []
    for i in range(n):
        result.append(helper(i))
    return result
