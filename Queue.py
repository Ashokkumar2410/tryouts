class Queue:
    def __init__(self):
        self.queue=[]
    def addQueue(self,x):
        if x not in self.queue:
            self.queue.insert(0,x)
            return True
        else:
            return False
    def removeQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return "NO elements"
