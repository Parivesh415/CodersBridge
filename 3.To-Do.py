
print("Creating an To-Do List")

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk, item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def TopmostItem(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top], "<-top")
        for a in range(top-1, -1, -1):
            print(stk[a])
#MAIN PROGRAM
stack=[]
top=None
while True:
    print("-"*15)
    print("To-do Operations")
    print("1.Add a new task ")
    print("2.Remove a task ")
    print("3.View your 1st Task")
    print("4.DisplayStack")
    print("5.Exit")
    print("-"*15)
    ch=int(input("Enter Your Choice[1-5]: "))
    if ch==1:
        item=input("Enter Task :")
        Push(stack, item)
    elif ch==2:
        item=Pop(stack)
        if item=="underflow":
            print("underflow:Stack is empty:")
        else:
            print("Removed Task is: ", item)
    elif ch==3:
        item=TopmostItem(stack)
        if item=="underflow":
            print("underflow:Stack is empty:")
        else:
            print("Top most Task  is", item)
    elif ch==4:
        Display(stack)
    elif ch==5:
        break
    else:
        print("Invalid Choice:")
