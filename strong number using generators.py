#write a python prgm to print the range of strong from 9 to 999 using generator
'''
def isstrong(num):
    bkp=num
    s=0
    while num>0:
        t=num%10
        f=1
        while t>1:
            f=f*t
            t=t-1
        s=s+f
        num=num//10
    if s==bkp:
        flag=True
    else:
        flag=False
    return flag 

      
def strongnumber(start,end):
    for n in range(start,end+1):
        if isstrong(n):
            yield n 


for i in strongnumber(9,999):
    print(i)

'''
n=int(input("enter a number:"))
temp=n
sum1=0
len1=len(str(n))
for i in range(len1):
    digit=temp%10
    f=1
    for d in range(digit,1,-1):
        f=f*d
    sum1=sum1+f
    temp=temp//10
if sum1==n:
    print("strong number")
else:
    print("not strong number")
        
    






















