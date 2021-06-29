import array as arr
a = arr.array('i',[1,2,3,4,5])
while True:
    print("1. Print array")
    print("2. Add Elements to array")
    print("3. Delete Elements")
    print("4. Exit")
    ch = int(input("Enter Your Choice: "))
    if ch==1:
        for n in a:
            print(n)
    elif ch==2:
        val= int(input("Enter value to be added: "))
        if isinstance(val, int):
            a.append(val)
        else:
            print("Invalid input")
    elif ch==3:
        value = a.pop()
        print("Removed Value: ",value)
    elif ch==4:
        break
    else:
        print("Enter valid choice!")
        