rows=int(input('enter number of rows:'))
for i in range(0,rows):
    for j in range(0,rows):
        if i==j or j==rows-i-1 :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
                
