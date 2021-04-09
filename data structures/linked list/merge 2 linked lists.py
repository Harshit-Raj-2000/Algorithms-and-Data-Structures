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
    dummy = tail = node(0)
    list1_node = list1.head
    list2_node = list2.head

    while True:
        if not list1_node:
            tail.next = list2_node
            break
        if not list2_node:
            tail.next = list1_node
            break
        if list1_node.data > list2_node.data:
            tail.next = list2_node
            list2_node = list2_node.next
        else:
            tail.next = list1_node
            list1_node = list1_node.next
        tail = tail.next
    return dummy.next

def recursive_merge_list(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data < head2.data:
        temp = head1
        temp.next = recursive_merge_list(head1.next, head2)
    else:
        temp = head2
        temp.next = recursive_merge_list(head1,head2.next)
    return temp





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
list1.head = recursive_merge_list(list1.head,list2.head)
list1.print_list()
