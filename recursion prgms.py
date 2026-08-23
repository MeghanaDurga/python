#1.write a python function to calculate the factorial of a given number using recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
res=factorial(5)
print(1,'factorial:',res)

#2.write a python to generate the nth fibonacci numberusing recursion
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
res=fib(7)
print(2,'fib:',res)

#3.write a python function to calculate the sum of digits of a given number using recursive functions
def sum(n):
    if n==0:
        return 0
    else:
        return n%10+sum(n//10)
res=sum(1234)
print(3,'sum:',res)


#5.find the sum of the elements in the given list by using recursive function
def sum(L):
    if len(L)==0:
        return 0
    else:
        return L[0]+sum(L[1: :])
res=sum([1,2,3,4,5,6])
print(5,'sum:',res)


#6.convert the nested list into single list by using recursive function
def nested(fun):
    flatten=[]
    for item in fun:
        if isinstance(item,list):
            flatten.extend(nested(item))
        else:
            flatten.append(item)
    return flatten

res=nested([1,[2,3],4,[5],[6,7,8,9,],10])
print(6,'nested:',res)



#7.check the given number is prime or not by using recursive function
def isprime(num,d=2):
    if num%d==0:
        return False
    elif d<num//2:
        return isprime(num,d+1)
    else:
        return True
res=isprime(5)
print(7,'prime:',res)


#8.print n even numbers by using recursive function
def iseven(n):
    if n==0:
        return 0
    else:
        return n%2==0
res=iseven(4)
print(8,'even:',res)


#9.print n odd numbers by using recursive function
def sum(n):
    if n==0:
        return 0
    else:
        return n%10+sum(n//10)
res=sum(12345)
print(9,'odd:',res)

#4.print the pattern by using recursive function
def pattern(n):
    print(n,end=' ')
    if n==0:
        return
    pattern(n-1)
    print(n,end=' ')
res=pattern(5)

