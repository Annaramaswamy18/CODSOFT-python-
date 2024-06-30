print("Welcome to To-do task App")
print("Menu: \n Enter 1 for Adding tasks \n Enter 2 for Modify tasks \n Enter 3 for Delete tasks \n Enter 4 for Complete the tasks \n Press Any other NUmber to exit the operation")
l=[]
comp=[]
while 1:
    n=int(input("Enter your Choice:"))
    if(n==1):
        s=input("Enter the tasks to be added: ")
        l.append(s)
    elif(n==2):
        print("id","tasks")
        for i in range(0,len(l)):
            print(i,l[i])
        x=int(input("Enter the id of the tasks to be modified"))
        if(x>=0 and x<len(l)):
            s=input("Enter the modified tasks: ")
            l[x]=s
            print("Sucessfully completed")
        else:
            print("Invalid operation")
    elif(n==3):
        print("id","tasks")
        for i in range(0,len(l)):
            print(i,l[i])
        x=int(input("Enter the Id of the tasks to be deleted: "))
        if(x>=0 and x<len(l)):
            l.pop(x)
            print("Sucessfully completed")
        else:
            print("Invalid operation")
    elif(n==4):
        print("id","tasks")
        for i in range(0,len(l)):
            print(i,l[i])
        x=int(input("Enter the id of tasks to be completed: "))
        if(x>=0 and x<len(l)):
            h=l.pop(x)
            comp.append(h)
            print("Sucessfully completed")
        else:
            print("Invalid operation")
    else:
        print("Invalid Operation")
        break
            
