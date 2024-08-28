print("Hello\n")
print("What operation do you wish to do?")
n1=int(input("Enter the 1st number for operation: "))
n2=int(input("Enter the 2nd number for operation: "))
a=int(input("Enter 1 for addition ,\n 2 for subtraction ,\n 3 for multiplication ,\n 4 for division \n Soo What do you Choose :"))
if(a==1):
    add=n1+n2
    print("Addition of ",n1,"and ", n2 ," is " , add)
elif(a==2):
    if(n2<n1):
        print("Subtrating ",n1," from ", n2 ," = ", n1-n2)
    else:
        print("Subtrating ",n2, "from ", n1,"=",n2-n1)
elif(a==3):
    print("Product of",n1,"and",n2,"is",n1*n2)
elif(a==4):
    if(n1==0):
        if(n2==0):
            print("Enter again not possible ERROR!!!")
        else:
            print("As the 1st number is zero so final answer is also zero")
    elif(n1!=0 and n2!=0):
        print("Dividing ",n1," from ", n2 ," = ", n1/n2)
    else:
        print("Can't divide number by 0 ")
else:
    print("Number entered wrong reenter the number")
