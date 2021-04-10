# input 1->2->3->4->5->None , k=3
# output - 3->2->1->5->4->None

# first 3 reverse,


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(f"->{temp.data}",end="")
            temp = temp.next
        print()
    def reverse_list(self):
        prev = None
        temp = self.head
        if temp == None:
            print("ERROR: can't reverse empty list.")
            return
        while temp:
            temp_next = temp.next
            temp.next = prev
            prev = temp
            temp = temp_next
        self.head = prev

    def recursive_reverse_list(self,node):
        if node == None or node.next == None:
            return node
        res = self.recursive_reverse_list(node.next)
        node.next.next = node
        node.next = None
        return res

# Time Complexity: O(n). - Traversal of list is done only once and it has ‘n’ elements.
# Auxiliary Space: O(n/k). - For each Linked List of size n, n/k or (n/k)+1 calls will be made during the recursion.
    def reverse_in_group(self,head,count):
        if head == None:
            return None
        cur_node = head
        prev_node = next_node = None
        k = 0
        while cur_node != None and k < count:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            k += 1
        if next_node != None:
            head.next = self.reverse_in_group(next_node,count)
        return prev_node

    def group_reverse(self,count):
        if self.head == None:
            print("ERROR: Can't reverse empty list.")
            return
        self.head = self.reverse_in_group(self.head,count)

llist = linked_list()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)
llist.print_list()
llist.group_reverse(2)
llist.print_list()
