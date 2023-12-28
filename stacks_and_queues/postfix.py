from Stack import MyStack

def evaluate_post_fix(exp):
    operators = ["+","-","*","/"]
    if len(exp) == 0 or exp[0] in operators or exp[1] in operators:
        return None
    stack = MyStack()
    
    for i in exp:
        if i in operators:
            second = stack.pop()
            first = stack.pop()
            stack.push(eval(str(first) + i + str(second)))
        else:
            stack.push(i)
        print(stack.peek())
    return stack.pop()
