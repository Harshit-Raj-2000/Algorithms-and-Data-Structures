# given two sorted linked lists
#  merge them into one sorted list

# input - 1->5->7->8; 2->3->6
# output - 1->2->3->5->6->7->8

# dummynode
#

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
    def print_list(self):
        temp = self.head
        while temp:
            print(f"->{temp.data}",end="")
            temp = temp.next
        print()


def merge_linked_lists(list1,list2):
    dummy = header = node(1)
    cur_node1 = list1.head
    cur_node2 = list2.head
    if not(cur_node1 and cur_node2):
        print("ERROR: can't merge with empty list!")
    while (cur_node1 and cur_node2):
        if cur_node1.data > cur_node2.data:
            dummy.next = node(cur_node2.data)
            cur_node2 = cur_node2.next
        else:
            dummy.next = node(cur_node1.data)
            cur_node1 = cur_node1.next
        dummy = dummy.next
    if cur_node1 == None:
        dummy.next = cur_node2
    else:
        dummy.next = cur_node1
    temp = header.next
    while temp:
        print(f"->{temp.data}",end="")
        temp = temp.next



list1 = linked_list()
list2 = linked_list()
list1.push(11)
list1.push(8)
list1.push(4)
list1.push(2)
list2.push(12)
list2.push(9)
list2.push(7)
list2.push(3)
print("List1 - ",end="")
list1.print_list()
print("List2 - ",end="")
list2.print_list()
merge_linked_lists(list1,list2)
