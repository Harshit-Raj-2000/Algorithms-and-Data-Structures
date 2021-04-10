class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
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
# another way to detect a loop is to change the node class to have
#  a variable flag, we traverse the nodes, change the flags from 0 to 1
# , if flag is 1, loop is found

# for below method - time complexity - O(n)
#  space complexity - O(n)
    def detect_loop(self):
        visited_nodes = set()
        count = 0
        temp = self.head
        while temp:
            if temp in visited_nodes:
                print(f"Loop found at node {count-1}")
                return True
            visited_nodes.add(temp)
            temp = temp.next
            count += 1
        print("Loop not found!")
        return False

    # the best way to find a loop is floyd's cycle finding
    # algorithm - time complexity - O(n) - space complexity - O(1)
    # Traverse linked list using two pointers.
    # Move one pointer(slow_p) by one and another pointer(fast_p) by two.
    # If these pointers meet at the same node then there is a loop.
    # If pointers do not meet then linked list doesn’t have a loop.

    def find_floyd_cycle(self):
        if self.head == None:
            print("ERROR: can't find loops in empty lists.")
        slow = fast = self.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop Found")
                return True
        print("Loop not found")
        return False





a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
f = node(6)
g = node(7)
h = node(8)
i = node(9)

a.next = b
b.next = a
c.next = d
d.next = a
llist = linked_list()
llist.head = a
llist.find_floyd_cycle()
