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
res=isstrong(145)
print(res)

res=isstrong(124)
print(res)
