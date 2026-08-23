rows=int(input('enter number of rows:'))
for i in range(0,rows):
    for j in range(0,rows):
        if i==0 or j==0 :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
                
