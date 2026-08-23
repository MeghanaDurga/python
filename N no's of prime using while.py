num = int(input('enter a value:'))
cnt=0
i=2
while cnt<num:
 d=2
 while d<i:
      if i%d==0:
          break
      d=d+1
 if d==i:
    print(i)
    cnt=cnt+1
 i=i+1
