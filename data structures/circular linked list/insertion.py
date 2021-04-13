class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class circular_linked_list:
    def __init__(self):
        self.last = None
    def append(self,data):
        new_node = node(data)
        if self.last == None:
            self.last = new_node
            new_node.next = new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
    def print_list(self):
        cur = self.last.next
        if cur == None:
            print("ERROR: Can't print empty list!")
        while cur!=self.last:
            print(f"->{cur.data}",end="")
            cur = cur.next
        print(f"->{cur.data}")

llist = circular_linked_list()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.print_list()
