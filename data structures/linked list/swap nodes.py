# swap nodes in a linked list without swapping data
# given 2 keys, swap the nodes having these two keys

# 1->4 3->2 2->5 4->3
# 1->2->3->4->5->6
# 2,4
# first make key1_prev.next = key2_current
# key2_prev.next = key1_current
# now swap both the key1_current.next and key2_current.next

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
    def swap_node(self,key1,key2):
        prev_node = None
        key1_prev = None
        key2_prev = None
        key1_current = None
        key2_current = None

        temp = self.head
        while temp and (key1_current == None or key2_current == None):
            if temp.data == key1:
                key1_current = temp
                key1_prev = prev_node
            elif temp.data == key2:
                key2_current = temp
                key2_prev = prev_node
            prev_node = temp
            temp = temp.next
        #after this while loop, following possibilities are there-
        # if either key1_current or key2_current not present
        # one of the keys is not present, so return
        # if both are present, but key_prev is None, then that key
        # is present in first node, so deal accordingly

        if key1_current == None or key2_current == None:
            print("ERROR: key not present error.")
            return
        if key1_prev == None:
            self.head = key2_current
        else:
            key1_prev.next = key2_current
        if key2_prev == None:
            self.head = key1_current
        else:
            key2_prev.next = key1_current
        (key1_current.next,key2_current.next) = \
        (key2_current.next,key1_current.next)
        return

    def print_list(self):
        temp = self.head
        while temp:
            print(f"->{temp.data}",end="")
            temp = temp.next
        print()

llist = linked_list()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.print_list()
llist.swap_node(2,3)
llist.print_list()
