class linked_list:
    def __init__(self):
        self.head = None
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# function to print the list
def print_linked_list(list):
    initial_node = list.head
    if(initial_node == None):
        print("Linked List is empty")
        return
    while initial_node != None:
        print(f"->{initial_node.data}",end="")
        initial_node = initial_node.next

# Creating the linked list

llist = linked_list()
llist.head = node(1)
second = node(2)
third = node(3)
llist.head.next = second
second.next = third
print_linked_list(llist)
