rows = int(input('enter numbers of rows:'))
space =' '
star ='*'
i=1
while i<=rows:
    if i==1 or i==rows:
        print(star*i,sep='')
    else:
        print(star,space*(1*(i-2)),star,sep='')
    i=i+1
