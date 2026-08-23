n =int(input('enter n value:'))
i = 1
cnt=0
while i<=100:
    if i%2==0:
        cnt=cnt+1
    if cnt==n:
        print(i)
        break
    i=i+1
