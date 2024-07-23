# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.min_element = 2**31

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_element:
            self.min_element = val
        self.size += 1

    def pop(self) -> None:
        popped_val = self.stack.pop()
        self.size -= 1
        if popped_val == self.min_element:
            self.min_element = 2**31
            for i in range(0,self.size):
                if self.stack[i] <= self.min_element:
                    self.min_element = self.stack[i]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element


'''
Neetcode

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.getMin():
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.getMin())

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

'''