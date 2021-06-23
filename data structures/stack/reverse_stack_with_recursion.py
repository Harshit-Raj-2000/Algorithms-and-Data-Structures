# Write a program to reverse a stack using recursion. 
# You are not allowed to use loop constructs like while, for..etc, and 
# you can only use the following ADT functions on Stack S: 
# isEmpty(S) 
# push(S) 
# pop(S)

# 1 2 3 4 5 6
# 2 1 4 3 6 5
# 1 2 3 5 4
# 1 2 5 3 

# 5 4 3 2 1

# class reverse_stack:
#     def __init__(self, given_array):
#         self.array = given_array
#         self.top = len(given_array) - 1
    
#     def push(self, value):
#         self.array.insert(0, value)
#         self.top += 1
    
#     def pop(self):
#         popped = self.array.pop()
#         self.top -= 1
#         return popped
    
#     def is_empty(self):
#         return self.top == -1
    
#     def reverse(self):

#         if self.is_empty():
#             return

#         temp = self.pop()
#         self.reverse()
#         self.push(temp)

# the above method works, another method given in gfg


    
def push(stack, value):
    stack.append(value)
        
    
def pop(stack):
    popped = stack.pop()
    return popped
    
def is_empty(stack):
    return len(stack) == 0
    
def insert_at_bottom(stack, item):
    if is_empty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insert_at_bottom(stack, item)
        push(stack, temp)

    
def reverse(stack):
    if not is_empty(stack):
        temp = pop(stack)
        reverse(stack)
        insert_at_bottom(stack, temp)


stack = [1,2,3,4,5,6]
reverse(stack)
print(stack)

    
    