('''a=1
b=2
print(a+b)''')


('''a=34
b=5
print("remainder when a is divided by is ", a%b)''')

('''a=int(input("enter the  of) a")
print(type(a)) ''')

('''a=int(int(input("enter number 1:"))
)b=int(int(input("enter number 2:"))
)
print("a is greater than b is",a>b)=''')

('''a=int(int(input("enter a number"))
b)=int(int(input("enter a number"))
p)rint("the average of these two number is",(a+b)/2)''')

('''a=int(int(input("enter the number 1:)"))
print("the square of the number is",a**2)''')

('''here=int(input("enter your here ")
)
print(f"good afternoon {here}")''')

('''here="gopal is a goodboy and  "
print(here.find("goo "))''')

"""marks=[]
f1=int(input("enter marks here:"))
marks.append(f1)
f2=int(input("enter marks here:"))
marks.append(f2)
f3=int(input("enter marks here:"))
marks.append(f3)
f4=int(input("enter marks here:"))
marks.append(f4)"""

"""marks=[]
f1=int(input("enter marks here:"))
marks.append(f1)
f2=int(input("enter marks here:"))
marks.append(f2)
f3=int(input("enter marks here:"))
marks.append(f3)
f4=int(input("enter marks here:"))
marks.append(f4)

marks.sort
print(marks)"""

"""g=[3,2,3,2]
print(sum(g))"""

'''words={
    "chair":"khurshi",
    "gopal":"vihaan",
    "madad":"help"
}

word=input("enter the word u want meaing of:")
print(words[word])'''

"""fruits=[]
f1=input("enter fruit name:")
fruits.append(f1)
f2=input("enter fruit name:")
fruits.append(f2)
f3=input("enter fruit name:")
fruits.append(f3)
f4=input("enter fruit name:")
fruits.append(f4)"""


'''s=set()
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))
n=input("Enter number:")
s.add(int(n))'''

'''a1=int(input("enter number 1:"))
a2=int(input("enter number 2:"))
a3=int(input("enter number 3:"))
a4=int(input("enter number 4:"))
if(a1>a2 and a1>a3 and a1>a4):
   print("greatest number is a1:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
   print("greatest number is a2:",a2)
elif(a3>a1 and a3>a2 and a3>a4):
   print("greatest number is a3:",a3)
elif(a4>a1 and a4>a2 and a4>a3):
   print("greatest number is a4:",a4)'''

"""marks1=int(input("enter marks1:"))
marks2=int(input("enter marks2:"))
marks3=int(input("enter marks3:"))
total_percentage=(marks1+marks2+marks3)/300*100

if(total_percentage>=40):
    print("you are pass")
else:
    print("you filled ,try again next year!")"""

"""n=int(input("enter a number:"))
for i in range (1,11):
    print(f"{n}x{1}={n*i}")"""

"""n=int(input("enter a number:"))
for i in range (2,n):
    if(n%i)==0:
        print("number is  not prime ")
        break
else:
    print("number is prime")"""

"""n=int(input("enter the number:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)"""

"""n=int(input("enter the number:"))
product=1
for i in range(1,n+1):
    product=product*i

print(f"the factorial of {n}is {product}"""

"""n=int(input("enter the number:"))
for i in range(1,n+1):
    print(""*(n-i),end="")
    print("*"* (2*i-1), end="")
    print("")"""

"""n=int(input("enter a number"))
for i in range(1,n+1):
    print("*"* i,end="")
    print("")"""

"""enter a number8
********
*      *
*      *
*      *
*      *
*      *
*      *
********"""
"""n=int(input("enter a number"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n)
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")"""
"""print reverse table 
n=int(input("enter a number"))
for i in range (1,11):
    print(f"{n}x{11-i}={n*(11-i)}")"""

"""def f_to_c(f):
    return 5*(f-32)/9
f=int(input("enter temp in f:"))
print(f_to_c(f))"""

"""def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(4)
outputs=
****
***
**
*"""
"""def inch_to_cms(inch):
    return inch*2.54

n=int(input("enter value in inches:"))
print(f"the corresponding value in cms is {inch_to_cms(n)}")
"""
'''
a="a very long string with emails
'''
"""f=open("file.text")
data = f.read()
print(data)
f.closed()"""

""""
append mode = file k end mai kuch add kerna hoto append mode use kerte hai 
"""
'''import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time:", current_time)
    time.sleep(1)'''






