## My Solution
from  typing import *

def helper(n, result):
    if n == 0:
        return 
    result.append("Coding Ninjas")
    helper(n-1,result)
    return

def printNtimes(n: int) -> List[str]:
    result = []
    helper(n, result)
    return result

## Solution
"""
    Time Complexity: O(n)
    Space Complexity: O(n)

    Where 'n' is the given integer.
"""

def printNtimes(n: int) -> None:
    print("Coding Ninjas ", end="")

    # Recursively calling printNtimes as long as 'n' > 1.
    if n > 1:
        printNtimes(n - 1)
