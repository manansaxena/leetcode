class Node:
    def __init__(self,data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

def insert_at_tail(lst, value):
    new_node = Node(value)
    if lst.is_empty():
        lst.head_node = new_node
        return
        
    temp = lst.get_head()
    while temp.next_element != None:
        temp = temp.next_element
    
    temp.next_element = new_node
    return

def search_node(lst,value):
    if lst.is_empty() == True:
        return False
    temp = lst.get_head()
    while temp != None:
        if temp.data == value:
            return True
        temp = temp.next_element
    return False

if __name__ == "__main__":
    lst = LinkedList()
    insert_at_tail(lst,0)
    insert_at_tail(lst,1)
    insert_at_tail(lst,2)
    lst.print_list()
    ans = search_node(lst,2)
    print(ans)