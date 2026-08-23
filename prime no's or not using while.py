n =int(input('enter n value:'))
cnt=0
d=1
while d<=n:
    if n%d==0:
        cnt=cnt+1
    d=d+1
if cnt==2:
    print('prime')
else:
     print(' not prime')
    
