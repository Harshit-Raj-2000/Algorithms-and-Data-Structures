class stack:
    def __init__(self):
        self.array = []
    
    def push(self, num):
        self.array.insert(0, num)
        return True
    
    def pop(self):
        if not self.isEmpty():
            val = self.array[0]
            del self.array[0]
            return val
        else:
            print("ERROR: list is empty")
    
    def peek(self):
        return self.array[0]

    def isEmpty(self):
        return len(self.array) == 0

stack_var = stack()
stack_var.push(5)
stack_var.push(6)
stack_var.push(7)

print(stack_var.peek())
stack_var.pop()
stack_var.pop()
print(stack_var.peek())

