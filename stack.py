class Stack():
    def __init__(self):
        self.stack = []
        self.cur_pos = -1
    
    def push(self,value):
        self.cur_pos+=1
        self.stack.append(value)
        
    def pop(self):
        self.stack.pop()
        self.cur_pos -= 1

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack[self.cur_pos]

    def is_empty(self):
        return self.cur_pos==-1

def __test__():
    a = Stack()
    a.top()
    print(a.is_empty())
    a.push('test')
    print(a.stack)
    a.push(23)
    a.push(True)
    print(a.stack)
    a.pop()
    print(a.top())


if __name__ == '__main__':
    __test__()
    
        
