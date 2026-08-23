i=1
while i<=50:
 d=2
 while d<=i//2:
     if i%d==0:
         print(i,'not prime')
         break
     d=d+1
 else:
     print(i,'prime')
 i=i+1
