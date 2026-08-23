rows = int(input('enter numbers of rows:'))
star = '*'
space = ' '
i=0
while i<=rows:
    print(space*i + star*(2*(rows-i)-1))
    i=i+1
