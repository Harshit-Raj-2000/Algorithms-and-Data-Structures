# given a key, we need to delete the first node
#  having the key

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

    # iterative method
    def delete_node_iterative(self,key):
        temp = self.head
        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print("Key does not exist")
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        if temp == None:
            print("Linked List is empty")
            return
        while(temp):
            print(f"->{temp.data}",end="")
            temp = temp.next
        print()

llist = linked_list()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.print_list()
llist.delete_node(3)
llist.delete_node(1)
llist.print_list()
