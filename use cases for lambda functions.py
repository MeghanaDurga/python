#1.how would you filter even numbers from a list in python?can you give an example?
x=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda y:y%2==0,x))
print(1,even)

#2.how can you calculate the square of numbers in a list in python?can you demonstrate this with an example?
square=lambda n:n**2
res=square(5)
print(2,res)

#3.how would you create a simple calculator in python?can you provide an example?


  

#4.how can you use lambda with sorted function for custom sorting in python ?can you show an example?
x=[(1,5),(4,6),(2,5),(9,7)]
sort=sorted(x,key=lambda a:a[0])
print(4,sort) 

#5.how can you combine lists element-wise in python?can you demonstrate this with an example?
x=[1,2,3,4]
y=[5,6,7,8]
res=[a+b for a,b in zip(x,y)]
print(5,res)  


#6.how would you remove duplicates from list in python?can you give an example?
y=[1,1,2,3,4,2,5,6,1,2]
seen=set()
res=list(filter(lambda x: x not in seen and not seen.add(x),y))
print(6,res)
