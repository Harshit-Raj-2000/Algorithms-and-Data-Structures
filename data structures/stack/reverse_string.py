class reverse:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, value):
        self.stack.append(value)
        self.top += 1
    
    def pop(self):
        popped = self.stack.pop()
        self.top -= 1
        return popped
    
    def is_empty(self):
        return self.top == -1
    
    def reverse_string(self,exp):
        output = ""
        for i in exp:
            self.push(i)
        while not self.is_empty():
            output += self.pop()
        return output

exp = "GeeksQuiz"
sol = reverse()
print(sol.reverse_string(exp))
