# Code 1

# Fibonacci Numbers
n=int(input("Enter the number of trems to be printed"))    #getting the number of fibonacci terms to be printed from the user

f1=0
f2=1    #speifying the base conditions
l=[f1,f2]    #creating the list with the first two trems(the base conditions)
  
if n<1:
    print("The number of terms should be greater than 0")
elif n==1:    #if n=0, then this loop is excecuted
    print("The Fibonacci Sequence unto",n,"terms is",l[0])
elif n==2:    #if n=1, then this loop is excecuted
    print("The Fibonacci Sequence unto",n,"terms is",l)
else:    #if n>1, then this loop is excecuted
    for i in range(1,n+1):   #specifying the range required 
        f=f1+f2
        l.append(f)     #after every iteration in this block, the 'f' value is added to the list
        f1=f2
        f2=f
    print(l)

#Code 2

#Printing positive numbers from a list
n=int(input("Enter the number of elements in the list"))    #getting the number of elements from the user

l=[]    #creating an empty list

for i in range(n):
    x=int(input("Enter the list element:"))
    l.append(x)    #creating the list

positive=[]
for i in range(n):
    if l[i]>0:
        positive.append(l[i])
print(positive)
