# python codsoft internship task-1 (calculator)


print("Welcome to the calculator")
p=0
while(p==0):
    n=int(input("Enter the number 1: "))
    n1=int(input("Enter the number 2: "))
    
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division(quotient)")
    print("Enter 5 for Division(remainder)")
    print("Enter 6 for Absolute difference Subtraction")
    print("Any other Number to exit")
    
    x=int(input("Enter the Choice:"))
    if(x==1):
        print("Addition is ",n+n1)
    elif(x==2):
        print("Subtraction is ",n-n1)
    elif(x==3):
        print("Multiplication is ",n*n1)
    elif(x==4):
        print("Diviiosion is (quotient)",n/n1)
    elif(x==5):
        print("Division is (remainder)",n%n1)
    elif(x==6):
        print("Absolute Difference (subtraction) is",abs(n-n1))
    else:
        break
