rows = int(input('enter number of rows:'))
star='*'
space=' '
i=1
while i<=rows:
    print(space*i,star*(rows-i+1))
    i=i+1
