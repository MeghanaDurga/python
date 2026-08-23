#write a python program to check given number is prime or not using decorators
#input=13
#output=True
def decfun(f):
    def innerfun(x,y):
        f(x,y)
        return innerfun
 
def isprime(n):
    for d in range(2,(n//2)+1):
        if n%d==0:
            return False
    else:
        return True
@decfun
def primenumber(start,end):
    for i in range(start,end+1):
        if isprime==True:
            return i



res=isprime(13)
print(res)
