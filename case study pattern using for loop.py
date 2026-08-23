rows = int(input("Enter number of rows: "))
start = 1  # This keeps track of the starting number for each row

for i in range(1, rows + 1):  # i is the current row number
    j = start  # j starts from 'start' for each row
    for k in range(i):  # Each row has 'i' numbers
        print(j, end=' ')
        j += 2  # Increase by 2 each time
    print()
    start += 1  # Move to the next starting number for the next row

        
    
    
