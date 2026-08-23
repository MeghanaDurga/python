'''#1.find the index of the first occurrence and last occurrence of a specific element in a tuple
t=(10,20,30,40,50)
res=t.index(10)
result=t.index(50)
print(res)
print('index of first occurence is:',result)

#2.concatenate two tuples
t1=(10,20,30,40)
t2=(50,60,70,80)
res=t1+t2
print('concatenate of two tuple:',res)

#3.count the occurrences of an element in a tuple
t="apple"
res=t.count('p')
print('count is:',res)

#4.check if an element exists in a tuple
t=(10,20,30,40,50)
if 30 in t:
    print("30 is exists in t")
else:
    print("30 is not exists in t")

#5.reverse a tuple
t=(10,20,30,40,50)
res=t[::-1]
print('reverse is:',res)

#6.find the maximum and minimum elements in a tuple
t=(10,20,30,40,50,60,70,80)
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if t[i]>t[j]:
            t[i],t[j]==t[j],t[i]
print("sorted list:",t)
print("minimum:",min(t))
print("maximim:",max(t))

#7.check if all elements in a tuple are the same
x=(4,4,4,4)
all_same=len(set(x))==1
print('all same is:',all_same)

#8.sort a tuple of numbers in ascending order
x=(10,40,30,50,20)
res=sorted(x)
print('sorted:',res)

#9.find the sum of all elements in a tuple
x=(10,20,30,40,50)
res=sum(x)
print('sum is:',res)

#10.check if a tuple contains only unique elements
x=(5,4,3,2,1)
if len(x)==len(set(x)):
    print('it contains unique elements')
else:
    print('it not contain unique elements')

#11.multiply a tuple contains only unique elements
x=(10,20,30,40)
res=x*2
print('multiply a tuple is:',res)
#12.unpack a tuple into individual variables
x,y,z=(20,40,60)
print('x:',x)
print('y:',y)
print('z:',z)

#13.convert a tuple of string into a single string
t = ("Hello", "world")
res = " ".join(t)
print('tuple of string:',res)

#14.merge two tuples into one using the + operator
t1=(10,20,30,40)
t2=(50,60,70,80)
res=t1+t2
print('merge two tuples is:',res)

#15.create a tuple of tuples(nested tuple)
t=(
   (1, 2, 3),
   ("a", "b", "c"),
)
print(t)

#16.find the product of all elements in a tuple of numbers
t = (1,2, 3, 4, 5)
product = 1
for num in t:
    product *= num
print("Product of all elements:", product)


#17.check if a tuple contain duplicate elements
x=[10,20,10,30,40,50,60]
if len(x)!=len(set(x)):
    print("duplicate")
else:
    print("no duplicate")

#18.remove an element from a tuple and create a new tuple without that element
original_tuple=(1, 2, 3, 4, 5)
element_to_remove=4
new_tuple=tuple(x for x in original_tuple if x != element_to_remove)
print("Original tuple:", original_tuple)
print("New tuple:", new_tuple)

#19.find the difference between two tuples
t1=(1, 2, 3, 4, 5)
t2=(4, 5, 6, 7)
difference=tuple(set(t1)-set(t2))
print("Difference:", difference)

#20.count the occurrences of each element in a tuple and store the results in adictionary
my_tuple=(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
count_dict={}
for item in my_tuple:
    if item in count_dict:
        count_dict[item]=count_dict[item]+1
    else:
        count_dict[item]=1
print("Element counts:", count_dict)

#21.find the common elements between two tuples
t1=(10,20,30,40)
t2=(50,60,40,20,70)
common=tuple(set(t1)&set(t2))
print('common element:',common)

#22.create a tuple from a string
s='iam learning python'
res=tuple(s)
print('string:',res)

#23.combine multiple tuples into one
t1=(10,20,30)
t2=(40,50,60)
t3=(70,80,90)
res=t1+t2+t3
print('combined value:',res)

#25.find the sum of all elements in a tuple
t=(1,2,3,4,5,6,7,8,9)
res=sum(t)
print('sum of all elements:',res)

#24.find the largest element in a tuple of numbers
t=(1,2,3,45,6)
max_value=0
for i in t:
    if i>max_value:
        max_value=i
print('largest elements is:',max_value)

#26.create a tuple of even numbers from an existing tuple
t=(1,2,3,4,5,6,7,8,9)
even_numbers=tuple(i for i in t if i%2==0)
print('even numbers are:',even_numbers)

#27.check if a tuple is a subset of another tuple
t1=(1,2,3,4)
t2=(1,2,3,4)
subset=set(t1)==set(t2)
print('subset are:',subset)

#28.check if a tuple is empty without using the len() function
tuple=()
if  tuple:
    print('tuple is not empty')
else:
    print('tuple is empty')

#29.create a new tuple with elements reversed in order from an existing tuple
t=(10,20,30,40)
res=t[::-1]
print('reversed elements are:',res)

#30.check if a tuple contains only numberic elements
t=(10,20,30,40,)
for item in t:
    if not isinstance(item,(int)):
        print('all elements are not numberic')
        break
else:
    print('all elements are numberic')

#31.check if a tuple is a palindrome(reads the same forwards and backwards)
t='madam'
if t==t[::-1]:
    print('palindrome')
else:
    print('not palindrome')

#32.find the tuple with the maximum sum in a list of tuples
t=(10,20,30,40,50)
res=sum(t)
print('max sum is:',res)'''

#33.rotate a tuple to right by k steps;
t=(1,2,3,4,5)
k=int(input('enter k value:'))
r_type=input('rotation type(RR/LR):')
if r_type=='RR':
    output=tuple(t[len(t)-k:]+t[:len(t)-k])
    print("Rotated Tuple:", output)
