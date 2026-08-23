i = 1
while i<=100:
    cnt=0
    d=1
    while d<=i:
        if i%d==0:
            cnt=cnt+1
        d=d+1
#a prime number has exactly 2 divisors:1 and itself
    if cnt==2:
        print(i)
    i=i+1

 
