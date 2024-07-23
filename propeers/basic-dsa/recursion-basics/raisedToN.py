## My Solution: Recursion
def helper(x, n):
    if n == 0:
        return 1
    return x * helper(x,n-1)

def myPow(x: float, n: int) -> float:
    if n < 0:
        n = n * -1
        x = 1/x
    return helper(x, n)    

## Their Solution: Not recursion
"""
Time Complexity: O(log n)
Space Complexity: O(1)

Where n is the integer.
"""

def myPow(x: float, n: int) -> float:
    # Declare variable 'ans'.
    ans = 1.0

    # Declaring boolean variable, that will be used
    # to check whether 'n' is neg or positive.
    flag = False
    if n < 0:
        flag = True
        n = -n

    # Binary Exponentiation.
    while n > 0:
        # If 'n' is divisible by '2'.
        if n % 2 == 0:
            n //= 2
        else:
            # 'n' is not divisible by 2.
            ans *= x
            # Dividing 'n' by 2.
            n //= 2

        # Multiplying 'x' by itself.
        x *= x

    # If 'flag' is true, that means 'n' was negative.
    if flag:
        ans = 1.0 / ans

    # Format 'ans' to have exactly 6 decimal places.
    ans = "{:.6f}".format(ans)

    return float(ans)
