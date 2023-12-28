from Stack import MyStack

def sort_it(main_stack, value):
    holding_stack = MyStack()

    while main_stack.peek() <= value:
        holding_stack.push(main_stack.pop())
        if main_stack.is_empty():
            break
    main_stack.push(value)
    while holding_stack.is_empty() == False:
        main_stack.push(holding_stack.pop())
    
def sort_stack(stack):
    # Write your code here
    if stack.is_empty():
        return None

    main_stack = MyStack()

    for i in range(0,stack.size()):
        if main_stack.is_empty():
            main_stack.push(stack.pop())
            continue
        sort_it(main_stack, stack.pop())
    
    return main_stack

if __name__ == "__main__":
    s = MyStack()
    s.push(2)
    s.push(10)
    s.push(13)
    s.push(3)
    s.push(2)
    print (s.stack_list)
    
    res = sort_stack(s)
    print(res.stack_list)



'''
Recursive : 

def sort_stack(stack):
    if (not stack.is_empty()):
        # Pop the top element off the stack
        value = stack.pop()
        # Sort the remaining stack recursively
        sort_stack(stack)
        # Push the top element back into the sorted stack 
        insert(stack, value) 
 
def insert(stack, value):
    if (stack.is_empty() or value < stack.peek()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

'''