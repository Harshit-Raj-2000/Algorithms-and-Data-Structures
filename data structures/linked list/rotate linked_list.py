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
    def rotate_list(self,rotate_count):
        if not self.head:
            print("ERROR: Can't rotate empty list")
            return
        temp_head = temp = self.head
        for i in range(rotate_count-1):
            temp = temp.next
        temp_next = temp.next
        self.head = temp_next
        temp.next = None
        temp = temp_next
        while temp.next != None:
            temp = temp.next
        temp.next = temp_head

llist = linked_list()
llist.push(60)
llist.push(50)
llist.push(40)
llist.push(30)
llist.push(20)
llist.push(10)
llist.print_list()
llist.rotate_list(4)
llist.print_list()
