i=1
while i<=50:
    d=2
    cnt=0
    while d<=i//2:
        if i%2==0:
            cnt=cnt+1
            break
        d=d+1
    if cnt==0:
        print(i)
    i=i+1
    
