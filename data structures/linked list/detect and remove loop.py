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

    # use hashing to find loop and thn remove it
    def remove_loop_hashing(self):
        prev_node = None
        if self.head == None:
            print("Error: Empty List Error.")
            return
        temp = self.head
        visited_nodes = set()
        while temp:
            if temp in visited_nodes:
                prev_node.next = None
                print("Loop removed")
                return True
            visited_nodes.add(temp)
            prev_node = temp
            temp = temp.next
        print("Loop not found")
        return False

    def floyd_loop_detection(self):
        slow = fast = self.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop found")
                self.floyd_loop_removal(slow)
                return True
        return False

    # technique one to remove loop after finding a loop_node
    # def floyd_loop_removal_tech1(self,loop_node):
    #     temp = self.head
    #     pointer = loop_node
    #     while 1:
    #         while pointer.next != loop_node and pointer.next != temp:
    #             pointer = pointer.next
    #         if pointer.next == temp:
    #             break
    #         temp = temp.next
    #     pointer.next = None


# technique 2 to remove node after finding loop node through floyd's technique
    def floyd_loop_removal(self,loop_node):
        loop_node_count = 1
        temp = loop_node.next
        while temp != loop_node:
            loop_node_count +=1
            temp = temp.next
        ptr1 = ptr2 = self.head
        for i in range(loop_node_count):
            ptr2 = ptr2.next
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None




    # this a very non-optimal way
    # we could use floyd's cycle finding algorithm or use a set to
    #  put the nodes in to optimise it.
    # def remove_loop(self):
    #     if self.head == None or self.head.next == None:
    #         # no loops in empty list or list with one node
    #         return False
    #     temp = self.head.next
    #     node_num = 1
    #     while temp.next != None:
    #         cur_node = self.head
    #         for i in range(0,node_num):
    #             if cur_node == temp.next:
    #                 temp.next = None
    #                 print(f"Loop found at node {node_num} removed")
    #                 return True
    #             cur_node = cur_node.next
    #         temp = temp.next
    #         node_num += 1
    #     print("No loop found!")
    #     return False

a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
a.next = b
b.next = c
c.next = a


llist = linked_list()
llist.head = a
llist.floyd_loop_detection()
llist.print_list()
