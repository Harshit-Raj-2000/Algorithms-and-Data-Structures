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

    def get_middle(self,head):
        fast = slow = head

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

# space complexity - O(nlog(n)),, time complexity - O(n(log(n)))
    def merge_sort(self,node):
        if node == None or node.next == None:
            return node
        middle = self.get_middle(node)
        middle_next = middle.next
        middle.next = None
        left_sorted = self.merge_sort(node)
        right_sorted = self.merge_sort(middle_next)
        result = merge(left_sorted,right_sorted)
        return result
    def sort(self):
        if self.head == None:
            print("ERROR: Can't sort empty list!")
            return
        else:
            self.head =  self.merge_sort(self.head)
            return

def merge(list1_node,list2_node):
    dummy = tail = node(0)
    while 1:
        if list1_node == None:
            tail.next = list2_node
            break
        if list2_node == None:
            tail.next = list1_node
            break
        if list1_node.data < list2_node.data:
            tail.next = list1_node
            list1_node = list1_node.next
        else:
            tail.next = list2_node
            list2_node = list2_node.next
        tail = tail.next
    return dummy.next

llist = linked_list()
llist.append(3)
llist.append(2)
llist.append(1)
llist.append(7)
llist.append(6)
llist.append(9)
llist.append(11)
llist.print_list()
llist.sort()
llist.print_list()
