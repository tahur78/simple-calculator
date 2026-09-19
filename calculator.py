print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.floor division")
print("6.exponential")
c=int(input("choose the operation below "))
a=float(input("enter the first number "))
b=float(input("enter the second number "))
match c :
    case 1:
        print("the addition of ",a,"and",b,"is",a+b )
    case 2 :
        print("the subtraction of ",a,"and",b, "is",a-b)
    case 3:
        print("the multiplication of",a,"and",b,"is",a*b)
    case 4:
        if b==0:
         print("invalid!!!")
        else:
         print("the division of",a,"and",b,"is", a/b)
    case 5:
        print("the floor division of",a,"and",b,"is",a//b)
    case 6:
        print("the exponenential of",a,"to",b,"is",a**b)
    case _ :
        print("please enter valid operation")

        

        
        
        
