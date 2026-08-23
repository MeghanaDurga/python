#18.create a copy of a list
x=[10,20,30]
res=x.copy()
print(res)

#19.reverse a list in place(modify the original list)
x=[10,20,30,40]
x.reverse()
print(x)

#20.find the index of the first occurence of an element from a specific position
x=[10,20,30]
res=x.index(10)
print(res)

#21.remove and return the last elements from a list
x=[1,2,3,4]
y=x.pop(1)
print(x)
print(y)

#22.find the index of the last occurence of an element in a list
x=[1,2,3,4]
res=x.index(4)
print(res)
#23.check if two lists are equal
x=[1,2,3]
y=[3,2,1]
print(set(x)==set(y))

#24.sort a list in-place(modify the original list)
x=[20,10,40,30]
x.sort()
print(x)

#25.find the second largest element in a list
x=[10,20,5,15]
first=second=float('-inf')
for num in x:
    if num>first:
        second=first
        first=num
    elif first>num>second:
        second=num
if second==float('-inf'):
    print('no second largest element found')
else:
    print('second largest element is:',second)

#26.remove elements at even indices from a list
list=[10,20,30,40,50,60,70,80]
result=[]
for i in range(len(list)):
    if i%2!=0:
        result.append(list[i])
print(result)

#27.find the intersection of two lists(common elements)
x=[10,20,30,40,50]
y=[20,40,60,70,80]
output=[i for i in x if i in y]
print(output)

#28.find the union of two lists(commom elements)

#29.remove all occurrences of a specific element from a list
x=[10,20,30,40]
x.remove(10)
print(x)

#30.check if a list is a palindrome(reads the same forwards and backwards)
x=input("enter a string:")
if x==x[::-1]:
    print("palindrome")
else:
    print("not palindrome")
