i=1
while i<=100:
    s=0
    d=1
    while d<=i//2:
        if i%d==0:
            s=s+d
        d=d+1
    if s==i:
        print(i,'is a perfect number')
    else:
        print(i,'is not a perfect number')
    i=i+1
