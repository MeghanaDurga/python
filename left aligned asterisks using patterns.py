rows = int(input('enter number of rows:'))
star = '*'
space = ' '
i=1
while i<=rows:
    print(space*(rows-i),star*(1*i-1))
    i=i+1
