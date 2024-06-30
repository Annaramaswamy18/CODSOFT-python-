import string
import random
print("welcome to the password generator app")
n=int(input("Enter the Password Length >=8 and less than<=25: "))
if(n<8 or n>25):
    print("Enter the correct length of the password as mentioned above")
else:
    l=[]
    s=""
    for i in range(0,n):
        h=random.randint(0,4)
        if(h==0):
            num=random.randint(0,10)
            l.append(num)
        elif(h==1):
            str1=random.choice(string.ascii_letters)
            l.append(str1.lower())
        elif(h==2):
            str2=string.punctuation
            l1=len(str2)
            r1=random.randint(0,l1)
            l.append(str2[r1])
        else:
            str3=random.choice(string.ascii_letters)
            l.append(str3.upper())
    for i in l:
        s+=str(i)
    print("Your Random password with Given Length is Given Below: ",end=' ')
    print("\n")
    print(s)
