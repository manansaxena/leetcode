from Stack import MyStack
open_brackets = ["{","[","("]
def is_balanced(exp):
    stack = MyStack()
    for i in exp:
        if stack.is_empty() or i in open_brackets:
            stack.push(i)
            continue
        else:
            if stack.peek() == "[" and i == "]":
                stack.pop()
            elif stack.peek() == "{" and i == "}":
                stack.pop()
            elif stack.peek() == "(" and i == ")":
                stack.pop()
            else:
                return False
    return True