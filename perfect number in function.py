def isperfect(num):
    s=0
    d=1
    for d in range(d,(num//2)+1):
        if num%d==0:
            s=s+d
        d=d+1
    if s==num:
        flag=True
    else:
        flag=False
    return flag

res=isperfect(10)
print(res)

res=isperfect(6)
print(res)
