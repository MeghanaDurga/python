rows = int(input('enter number of rows:'))
space=' '
star='*'
i=1
while i<=rows:
    print(space*(rows-i),star*i)
    i=i+1
