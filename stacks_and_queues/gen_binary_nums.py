from Queue import MyQueue

def find_bin(number):
    # Write your code here 
    q = MyQueue()  
    res = []
    count = 0

    while count < number:
        if count == 0:
            res.append("1")
            q.enqueue("1")
            count += 1
            continue
        front_elem = q.front()
        res.append(front_elem + "0")
        q.enqueue(front_elem + "0")
        count += 1
        if count < number:
            res.append(front_elem + "1")
            q.enqueue(front_elem + "1")
            count += 1
        q.dequeue()
    
    return res


if __name__ == "__main__":
    res = find_bin(10)
    print(res)