#1.can you provide a lambda function to square a number in python
square=lambda n:n**2
res=square(4)
print(1,'square:',res)

#2.how can you create a lambda function to add two numbers in python?can you give an example?
addition=lambda a,b:a+b
res=addition(20,40)
print(2,'addition:',res)

#3.how would you write a lambda function to find the maximum of two numbers in python?can you show an example?
maximum=lambda a,b:a if a>b else b 
res=maximum(100,40)
print(3,'maximum number is:',res)

#4.how can you create a lambda function to check if a number is even in python?can you provide an example?
even=lambda a:a%2==0
res=even(4)
print(4,'even:',res)

#5.can you demonstrate a lambda function to extract the last chararcter from a string in python?
string=lambda st:st[5]
res=string("chinni")
print(5,'last character:',res)

#6.how would you write a lambda function to sort a list of tuples based on the second element in python?can you provide an example?
n=[(2,10),(3,4),(1,5),(4,8)]
res=sorted(n,key=lambda x:x[1])
print(6,'second elements:',res)

#7.how can you create a lambda function to filter even number s from a list in python ?can you give an example?
n=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,n))
print(7,'even numbers are:',even)
#8.can you provide a lambda function with a conditional expression to categorize ages in python?
categorize_age=lambda age: "Child" if age < 15 else "Teen" if age < 25 else "Adult"
ages=[10,20,35]
categories=[categorize_age(age) for age in ages]
print(8,categories)

#9.how can you write a lambda function to calculate the factorial of a number using recursion in python? can you demonstrate this with an example?
factorial=lambda n:1 if n==0 else n*factorial(n-1)
res=factorial(5)
print(9,res)
    
