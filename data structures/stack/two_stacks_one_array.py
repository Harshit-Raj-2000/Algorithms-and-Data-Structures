# inefficient method - define an array, and equally divide the space for two arrays
# efficient method - check for distance between top elements of both stacks

class twostacks():

    def __init__(self, capacity):
        self.array = [None]*capacity
        self.top1 = -1
        self.top2 = capacity
    
    def push1(self, value):
        if (self.top2 - self.top1) == 1:
            print(f"stack1 overflowed for element {value}")
            return
        self.top1 += 1
        self.array[self.top1] = value
    
    def push2(self, value):
        if (self.top2 - self.top1) == 1:
            print(f"stack2 overflowed for element {value}")
            return
        self.top2 -= 1
        self.array[self.top2] = value
    
    def pop1(self):
        if self.top1 == -1:
            print("stack underflow for stack1")
            return
        popped = self.array[self.top1]
        self.top1 -= 1
        return popped
    
    def pop2(self):
        if self.top2 == len(self.array):
            print("stack underflow for stack2")
            return
        popped = self.array[self.top2]
        self.top2 += 1
        return popped

ts = twostacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))