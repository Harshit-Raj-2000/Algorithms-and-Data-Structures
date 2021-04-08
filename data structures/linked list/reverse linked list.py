# 1->2->3->4
# output - 4->3->2->1
# timecomplexity - O(n)
# space complexity - O(1)

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
    def reverse_list(self):
        temp = self.head
        prev_node = None
        while temp:
            temp_next = temp.next
            temp.next = prev_node
            prev_node = temp
            temp = temp_next
        self.head = prev_node
    def recursive_reverse(self,node,prev_node):
        if node == None:
            self.head = prev_node
            return
        else:
            node_next = node.next
            node.next = prev_node
            self.recursive_reverse(node_next,node)
    def recursive_reverse_list(self):
        if self.head == None:
            print("ERROR: Can't reverse empty list!")
            return
        self.recursive_reverse(self.head,None)
        return

    def print_list(self):
        temp = self.head
        while temp:
            print(f"->{temp.data}",end="")
            temp = temp.next
        print()


llist = linked_list()
llist.push(1)


llist.print_list()
llist.recursive_reverse_list()
llist.print_list()
