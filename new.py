i=9
s=0
while i<=999:
  d=2
  while d<=i//2:
    if i%d==0:
        break
    d=d+1
    else:
      s=s+i
  i=i+1
print(s)
