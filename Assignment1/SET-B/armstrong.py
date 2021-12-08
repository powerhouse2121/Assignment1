#SET.B
#Write a python program to check armstronng number

num=int(input("Enter the number:"))
sum=0
num1=num
while(num1>0):
    d=num1%10
    num1=int(num1/10)
    sum=sum+d*d*d
if(num==sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
