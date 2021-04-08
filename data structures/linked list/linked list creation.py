class linked_list:
    def __init__(self):
        self.head = None
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    llist = linked_list()
    first = node(1)
    second = node(2)
    third = node(3)
    llist.head = first
    first.next = second
    second.next = third
