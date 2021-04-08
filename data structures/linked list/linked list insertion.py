class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        initial_node = self.head
        while initial_node != None:
            print(f"->{initial_node.data}",end="")
            initial_node = initial_node.next

# inserting node at the front
#time complexity - O(1)
def insert_at_front(list,data):
    new_node = node(data)
    new_node.next = list.head
    list.head = new_node

#inserting after a given node
#we are given the pointer to a node, insert data after this node
# time complexity - O(1)
def insert_after_node(data,node_pointer):
    new_node = node(data)
    new_node.next = node_pointer.next
    node_pointer.next = new_node

#  insert node at the end
# time complexity - O(n) as we traverse the list
# we can optimise it to be O(1), if we just maintain a pointer
# to the last element in our linked_list class
def insert_at_end(list,data):
    new_node = node(data)
    current_node = list.head
    if current_node == None:
        list.head = Node(data)
        return
    while(current_node.next):
        current_node = current_node.next
    current_node.next = new_node

llist = linked_list()

insert_at_front(llist,1)
insert_at_front(llist,2)
insert_at_front(llist,3)
insert_after_node(4,llist.head)
insert_after_node(5,llist.head)
insert_after_node(6,llist.head)
insert_at_end(llist,9)
insert_at_end(llist,10)
insert_at_end(llist,11)



llist.print_list()
