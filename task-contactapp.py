from collections import defaultdict
print("welcome to contact-app")
print("Menu:\n Enter 1 for add new contact \n Enter 2 for Search contacts by Name \n Enter 3 for search Contacts by phone number\n Enter 4 for modify the contacts \n Enter 5 for delete contacts \n Enter 6 for display all the contacts \n Enter Any other choice to exit")
d1=defaultdict(int)
while 1:
    n=int(input("Enter the choice: "))
    if(n==1):
        s=input("Enter the name: ")
        s1=int(input("Enter the phone number: "))
        s2=input("Enter the email addess: ")
        s3=input("Enter the Address: ")
        d1[s]=[s1,s2,s3]
        print("Sucessfully completed")
    elif(n==2):
        s=input("Enter the name: ")
        fl=0
        for i in d1:
            if(i.count(s)!=0):
                fl=1
                print("name: ",i,"ph-no: ",d1[i][0],"email: ",d1[i][1],"address: ",d1[i][2])
        if(fl==0):
            print("No records found")
    elif(n==3):
        s=input("Enter the ph-no: ")
        fl=0
        for i in d1:
            if(str(d1[i][1]).count(s)!=0):
                fl=1
                print("name: ",i,"ph-no: ",d1[i][0],"email: ",d1[i][1],"address: ",d1[i][2])
        if(fl==0):
            print("No records found")
    elif(n==4):
        s=input("Enter the name: ")
        fl=0
        for i in d1:
            if(i.count(s)!=0):
                fl=1
                print("Menu: \n Enter 1 to change Name \n Enter 2 to Change Ph-no \n Enter 3 to change Email \n Enter 4 to change Address \n Any other choice for seeing any other matchings of this contacts is there")
                n1=int(input("Enter the choice: "))
                if(n1==1):
                    t1=input("Enter the new name: ")
                    h=d1[i]
                    del d1[i]
                    d1[t1]=h
                    break
                elif(n1==2):
                    t2=input("Enter the new ph-no: ")
                    t2=int(t2)
                    d1[i][0]=t2
                    break
                elif(n2==3):
                    t3=input("Enter the new ph-no: ")
                    d1[i][1]=t3
                    break
                elif(n==4):
                    t4=input("Enter the new Address: ")
                    d1[i][2]=t4
                    break
        if(fl==0):
            print("No records found")
    elif(n==5):
        s=input("Enter the name: ")
        fl=0
        for i in d1:
            if(i.count(s)!=0):
                fl=1
                print("Menu \n  Enter 1 to delete \n Enter Any other number to see Any other match of this contact is there ")
                n1=int(input("Enter the choice: "))
                if(n1==1):
                    del d1[i]
                    break
        if(fl==0):
            print("No records found")
    elif(n==6):
        for i in d1:
            print("name: ",i,"ph-no: ",d1[i][0],"email: ",d1[i][1],"address: ",d1[i][2])
        
    else:
        print("Thank You")
