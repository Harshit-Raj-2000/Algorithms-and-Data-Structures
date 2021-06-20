class conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, value):
        self.array.append(value)
        self.top += 1
    
    def pop(self):
        if not self.is_empty():
            popped = self.array.pop()
            self.top -= 1
            return popped
        else:
            return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.array[-1]
        else:
            return "Stack is empty"
    
    def is_operand(self, char):
        return char.isalpha()
    
    def not_greater(self, i):
        try:
            precd_i = self.precedence[i]
            precd_stack = self.precedence[self.peek()]

            return True if precd_stack >= precd_i else False
        except KeyError:
            return False
    
    def infix_to_postfix(self, expression):

        for each in expression:

            if self.is_operand(each):
                self.output.append(each)
            
            elif each == '(':
                self.push(each)
            
            elif each == ')':
                while (not self.is_empty()) and (self.peek() != '('):
                    self.output.append(self.pop())
                if not self.is_empty():
                    self.pop()
                else:
                    return "some error occured"
            else:
                while (not self.is_empty()) and self.not_greater(each):
                    self.output.append(self.pop())
                self.push(each)
        while (not self.is_empty()):
            self.output.append(self.pop())
        
        print( "".join(self.output))
    

exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = conversion(len(exp))
obj.infix_to_postfix(exp)


    
        
