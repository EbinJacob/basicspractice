class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items == []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()

s = stack()
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Quit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        val = int(input("Enter value to be pushed: "))
        s.push(val)
    elif ch==2:
        if s.isempty():
            print("Stack is empty")
        else:
            print("Popped value is: ", s.pop())
    elif ch==3:
        break
    else:
        print("Enter a valid choice!")
