class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class circular_list:
    def __init__(self):
        self.last = None
    def push(self,data):
        new_node = node(data)
        if self.last == None:
            self.last = new_node
            new_node.next = new_node
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
    def print_list(self):
        cur = self.last.next
        while True:
            print(f"->{cur.data}",end="")
            cur = cur.next
            if cur == self.last.next:
                break

llist = circular_list()
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(3)
llist.push(4)
llist.print_list()
