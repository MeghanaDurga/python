n = int(input('enter n value:'))
cnt=0
for d in range(1,n+1):
    if n%d==0:
       cnt=cnt+1
if cnt==2:
    print('prime')
else:
    print('not prime')
