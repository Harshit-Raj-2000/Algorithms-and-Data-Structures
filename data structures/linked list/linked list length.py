# find the num of nodes in linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def iterative_length(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length
    def print_list(self):
        temp = self.head
        if temp == None:
            print("List is empty.")
            return
        while temp:
            print(f"->{temp.data}",end="")
            temp = temp.next
    def recursive_length(self,node):
        if node == None:
            return 0
        else:
            return 1 + self.recursive_length(node.next)

llist = linked_list()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
print(llist.recursive_length(llist.head))
