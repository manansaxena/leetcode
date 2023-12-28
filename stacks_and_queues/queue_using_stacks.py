from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here
        self.temp_stack = MyStack()


    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)
        return True


    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        while self.main_stack.is_empty() == False:
            self.temp_stack.push(self.main_stack.pop())
        data = self.temp_stack.peek()
        self.temp_stack.pop()
        while self.temp_stack.is_empty() == False:
            self.main_stack.push(self.temp_stack.pop())

        return data
    