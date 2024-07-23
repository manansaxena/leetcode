## My Solution
from typing import *

def factorial(i):
    if i == 0 or i == 1:
        return 1
    return factorial(i-1) * i;

def helper(i, n, result):
    if factorial(i) > n:
        return
    if factorial(i) <= n:
        result.append(factorial(i))
    helper(i+1,n,result)
    return

def factorialNumbers(n: int) -> List[int]:
    result = []
    helper(1, n, result)
    return result  

## Solution
from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    result = 1
    cnt = 1
    ans = []
    
    while result <= n // cnt:
        # Multiplying 'result' with 'cnt'.
        result *= cnt
        
        # Incrementing 'cnt' by '1'.
        cnt += 1
        
        # Inserting 'result' in the list 'ans'.
        ans.append(result)
    
    return ans