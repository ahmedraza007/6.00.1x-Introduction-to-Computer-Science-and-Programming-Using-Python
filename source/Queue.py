class Queue(object):
    
    def __init__(self):
        self.x = []
        
    def insert(self, e):
        if e not in self.x:
            self.x.append(e)
    
    def remove(self):
        try:
            p = self.x.pop(0)
            return p
        except:
            raise ValueError('not found')
        

q = Queue()
q.insert(7)
q.insert(8)
q.insert(9)
print q.remove()