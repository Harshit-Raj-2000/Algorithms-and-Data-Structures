# we will need to use 2 queues to make it work

class queue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.insert(0, value)
    
    def dequeue(self):
        return self.array.pop()
    
    def is_empty(self):
        return len(self.array) == 0

class stack:
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()
    
    def push(self, value):
        self.q2.enqueue(value)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.dequeue()
        

st = stack()

st.push(5)
st.push(7)
st.push(9)
st.push(11)

print(st.q1.array)
print(st.pop())
print(st.pop())
print(st.pop())



        


        