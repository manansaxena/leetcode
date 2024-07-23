## My Solution
def isPalindrome(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    answer = isPalindrome(string[1:-1])
    if answer == False:
        return False
    else:
        if string[0] == string[-1]:
            return True
        else:
            return False
    return answer

## Solution
'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the length of the string
'''

def isPalindrome(string: str) -> bool:
    size=len(string)
    # Base case: If the length of string is 1, the string is a palindrome.
    if size <= 1:
        return True
    # If the characters at the left and right pointers are not equal, the string is not a palindrome.
    if string[0]!=string[size-1]:
        return False
    # Recurse for the substring by moving the left pointer to the right and the right pointer to the left.
    return isPalindrome(string[1:-1])