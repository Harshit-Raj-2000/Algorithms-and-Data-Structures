# num1 - 5->6->3-> null. represents 365
# num2 - 8->4->2-> null represents 248
# output - 3->1->6-> output -> 613

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def push(self,data):
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

# Time Complexity - O(m+n)
# Auxillary space - O(m+n)
def add_list(head1, head2):
    if not head1 or not head2:
        print("list empty: assuming empty list to be 0.")
        return head1 or head2 or 0
    carry = 0
    sum_list = linked_list()
    while head1 != None and head2 != None:
        node_sum = head1.data + head2.data + carry
        carry = 1 if node_sum > 9 else 0
        sum_list.push(node_sum%10)
        head1 = head1.next
        head2 = head2.next
    temp = head1 or head2
    while temp != None:
        node_sum = temp.data + carry
        carry = 1 if node_sum > 9 else 0
        sum_list.push(node_sum%10)
        temp = temp.next
    if carry == 1:
        sum_list.push(1)
    return sum_list

num1 = linked_list()
num2 = linked_list()
num1.push(7)
num1.push(5)
num1.push(9)
num1.push(4)
num1.push(6)

num2.push(8)
num2.push(4)

sum_list = add_list(num1.head,num2.head)
print("num1:",end=" ")
num1.print_list()
print("num2:",end=" ")
num2.print_list()
sum_list = add_list(num1.head,num2.head)
sum_list.print_list()
