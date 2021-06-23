# we need double linked list implementation of stack
# in order to make this work

class stack_node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.count = 0
        self.mid = None
    
    def push(self, value):
        new_node = stack_node(value)

        new_node.next = self.head

        self.count += 1

        if self.count == 1:
            self.mid = new_node
        else:
            self.head.prev = new_node

            if self.count%2 != 0:
                self.mid = self.mid.prev
        self.head = new_node
    
    def pop(self):
        d = self.head.data
        self.head = self.head.next()
        self.count -= 1

        # if self.count -- even, mid = mid.next

        if self.count%2 == 0:
            self.mid = self.mid.next
        
        return d
    
    def find_mid(self):
        return self.mid.data
    
    def delete_mid(self):

        temp = self.mid
        self.count -= 1

        if self.count%2 == 0:
            self.mid = self.mid.next
        else:
            self.mid = self.mid.prev
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
    
    def print(self):

        temp = self.head

        while temp != None:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print()
  
s = stack()
s.push(5)
s.push(6)
s.push(7)
s.delete_mid()
s.print()
s.push(9)

print(s.find_mid())


