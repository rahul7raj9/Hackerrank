#1-enque
#2- deque
#3 - print
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[0]
        
        
    def pop(self):
        self.second = self.first[1:]
        self.first=self.second
        return
        
    def put(self, value):
        self.first.append(value)
        return

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
