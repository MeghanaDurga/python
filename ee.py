i = 1

while i <= 50:
    d = 2
    while d <= i // 2:
        if i % d == 0:
            print(i, 'is not prime')
            break
        d = d + 1
    else:
        # This else belongs to the while loop above, not the if
        print(i, 'is prime')
    i = i + 1
