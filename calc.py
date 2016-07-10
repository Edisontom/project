print ("Enter number of action: 1- Additional",
       "2-Subtraction, 3-Multiply, 4-Division")
value=int(input())
print("Enter first number and put Enter on keyboard:")
a = int(input())
print("Enter second number and put Enter on keyboard::")
b = int(input())
if value==1:
    c=a+b
    print (c)
elif value==2:
    c=a-b
    print (c)
elif value==3:
    c=a*b
    print (c)
elif value==4:
    c=a/b
    print (c)
elif value <1:
    print ("Enter correct number of action")
elif value >=5:
    print ("Enter correct number of action")





