# given a position, delete the node at that position
# from the linked list

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
    def delete_node(self,position):
        temp = self.head
        current_position = 0
        if temp != None and position == 0:
            self.head = temp.next
            temp = None
            return
        while temp != None:
            if current_position == position:
                break
            prev = temp
            temp = temp.next
            current_position += 1
        if temp == None:
            print("Element not found")
            return
        prev.next = temp.next
        temp = None
    def print_list(self):
        temp = self.head
        if temp == None:
            print("List is empty!")
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
