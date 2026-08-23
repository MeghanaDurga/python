rows = int(input('enter number of rows:'))
space= ' '
star = '*'
i=1
while i<=rows:
    print(space*(rows-i),star*(2*i-1))
    i=i+1
