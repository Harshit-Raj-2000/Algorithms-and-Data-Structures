class sort_stack:
    def __init__(self, arr):
        self.array = arr
        self.top = len(arr) - 1
    
    def push(self, value):
        self.array.append(value)
        self.top += 1
    
    def pop(self):
        popped = self.array.pop()
        self.top -= 1
        return popped
    
    def is_empty(self):
        return self.top == -1
    
    def peek(self):
        return self.array[-1]
    
    def insert_sorted(self, item):
        if self.is_empty():
            self.push(item)
        else:
            if item >= self.peek():
                self.push(item)
                return
            temp = self.pop()
            self.insert_sorted(item)
            self.push(temp)

    def sort(self):
        if not self.is_empty():
            temp = self.pop()
            self.sort()
            self.insert_sorted(temp)

a = sort_stack([-3, 14, 18, -5, 30])
a.sort()
print(a.array)

# def push(stack, value):
#         stack.append(value)
        
# def pop(stack):
#     popped = stack.pop()
#     return popped

# def is_empty(stack):
#     return len(stack) == 0

# def peek(stack):
#     return stack[-1]

# def insert_sorted(stack, item):
#     if is_empty(stack):
#         push(stack, item)
#     else:
#         if item >= peek(stack):
#             push(stack, item)
#             return
#         temp = pop(stack)
#         insert_sorted(stack, item)
#         push(stack, temp)

# def sort(stack):
#     if not is_empty(stack):
#         temp = pop(stack)
#         sort(stack)
#         insert_sorted(stack, temp)



# a = [-3, 14, 18, -5, 30]
# sort(a)
# print(a)

