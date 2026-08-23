def isprime(n):
    for d in range(2,(n//2)+1):
        if n%d==0:
            flag=False

            break
    else:
        flag=True
    return flag
res=isprime(8)
print(res)

res=isprime(17)
print(res)

res=isprime(13)
print(res)

