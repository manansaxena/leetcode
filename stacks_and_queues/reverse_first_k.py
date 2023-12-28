from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    # Write your code here

    if queue.size() == 0 or k <0 or k > queue.size() :
        return None

    s = MyStack()
    
    for i in range(0,k):
        s.push(queue.front())
        queue.dequeue()
    
    for i in range(0,k):
        queue.enqueue(s.pop())
    
    for i in range(0,queue.size()-k):
        queue.enqueue(queue.dequeue())
    return queue

if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue_list)
    res = reverseK(q,3)
    print(res.queue_list)