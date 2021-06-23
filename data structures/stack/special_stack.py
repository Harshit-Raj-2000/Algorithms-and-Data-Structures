# esign a Data Structure SpecialStack that supports all the stack operations like
# push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
# which should return minimum element from the SpecialStack. 

class special_stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.min_stack = []
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, value):
        if self.is_empty() or value <= self.get_min():
            self.min_stack.append(value)
        self.stack.append(value)
        self.top += 1
        
    
    def pop(self):
        popped = self.stack.pop()
        self.top -= 1
        if popped == self.get_min():
            self.min_stack.pop()
        return popped
    
    def get_min(self):
        return self.min_stack[-1]

st = special_stack()
st.push(18)
st.push(19)
st.push(29)
st.push(15)
st.push(16)

print(st.get_min())
st.pop()
st.pop()
print(st.get_min())

# we can also use a single variable min, to do the same job, if
# instead of putting the actual values in the stack, we rather
# put (actualvalue*dummyvalue + min till now), using this we can recover the dummy value
#  as well as the min value, at each point of time.
