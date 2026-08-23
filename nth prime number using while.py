num = int(input('enter a value:'))
cnt=0
i=2
while True:
 d=2
 while d<=i//2:
      if i%d==0:
          break
      d=d+1
 else:
      cnt=cnt+1
      if cnt==num:
          print(i)
          break
 i=i+1
