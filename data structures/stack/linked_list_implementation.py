class stack_node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.root = None
    
    def push(self,data):
        new_node = stack_node(data)
        new_node.next = self.root
        self.root = new_node
        return True
    
    def pop(self):
        if not self.is_empty():
            popped = self.root.data
            self.root = self.root.next
            return popped
        else:
            print("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.root.data
        else:
            print("stack is empty")

    def is_empty(self):
        return not self.root

stack_var = stack()
stack_var.push(5)
stack_var.push(6)
stack_var.push(7)
stack_var.push(9)


print(stack_var.peek())
stack_var.pop()
stack_var.pop()
print(stack_var.peek())

    

        
        
