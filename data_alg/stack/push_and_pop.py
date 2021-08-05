class Stack:
    def __init__(self):
      self.stack = []
    
    def __str__(self) -> str:
        str1 = " "
        return (str1.join(self.stack))
    
    def push(self, dataval):
        self.stack.append(dataval)
         
    
    def pop(self):
        if len(self.stack) <= 0:
            return("No element in stack")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]
        
    
    
        
A_stack = Stack()
A_stack.push("One")
A_stack.push("Two")
A_stack.push("Three")
print(A_stack)
print(A_stack.pop())
print(A_stack.peek())   
print(A_stack)