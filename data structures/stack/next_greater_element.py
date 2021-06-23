# [13,7,6,12]
# >> -1, 12, 12, -1


# O(n^2) -- obvious solution
# using stack will make it easier --- how??

class nge:
    def __init__(self):
        self.array = []
        self.top = -1
    
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
    
    def next_greater(self, list_el):
        for each in list_el:
            if self.is_empty():
                self.push(each)
            else: 
                while (not self.is_empty()) and each > self.peek():
                    print(f"next greater element for {self.pop()} is {each}")
                self.push(each)
        while not self.is_empty():
            print(f"next greater element for {self.pop()} is -1")

# the above method works great, but can't give output in the order of input
# in order to give output in the order of output, instead of printing
# we can store the results in a dict, and then print it in the required order

nge = nge()
lis = [4, 5, 2, 25]
nge.next_greater(lis)

        
            

