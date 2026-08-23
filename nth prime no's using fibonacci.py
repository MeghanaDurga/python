n = int(input('enter n value:'))
p_cnt=0
a = 0
b = 1
while True:
    c=a+b
    cnt=0
    d=1
    while d<=c:
        if c%d==0:
            cnt=cnt+1
        d=d+1
    if cnt==2:
        p_cnt=p_cnt+1
    if p_cnt==n:
        print(c)
        break
    a=b
    b=c
            
