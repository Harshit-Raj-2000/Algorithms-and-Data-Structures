class balanced:
    def __init__(self):
        self.array = []
        self.top = -1
        self.bracket_dict = {')':'(', '}':'{', ']':'['}
    
    def push(self, value):
        self.array.append(value)
        self.top += 1
    
    def pop(self):
        popped = self.array.pop()
        self.top -= 1
        return popped
    
    def peek(self):
        return self.array[-1]
    
    def is_empty(self):
        return self.top == -1
    
    def check_balanced(self, exp):

        for i in exp:
            try: 
                if self.is_empty():
                    self.push(i)
                elif self.peek() == self.bracket_dict[i]:
                    self.pop()
            except:
                self.push(i)
        if self.is_empty():
            return True
        else:
            return False

exp = '[(])'
b = balanced()
print(b.check_balanced(exp))
