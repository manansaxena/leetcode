# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
            elif op == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)