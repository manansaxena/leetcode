from Stack import MyStack

def next_greater_element(lst):
    res = [-1] * len(lst)
    stack = MyStack()
    for i in range(0,len(lst)):
        if stack.is_empty():
            stack.push(i)
            continue
        if lst[stack.peek()] >= lst[i]:
            stack.push(i)
        else:
            while lst[i] > lst[stack.peek()]:
                res[stack.pop()]  = lst[i]
                if stack.is_empty():
                    break
            stack.push(i)
        print(stack.stack_list)
    
    return res