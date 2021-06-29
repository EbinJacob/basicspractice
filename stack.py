class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items == []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        self
