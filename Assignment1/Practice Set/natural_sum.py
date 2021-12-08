#Practice Set
#Write a python program to find the sum of natural number

n=int(input("Starting number::"))
n1=int(input("Ending number::"))
s=0
for i in range(n,n1+1):
    s=s+i
print("Sum of natural numbers::",s)
