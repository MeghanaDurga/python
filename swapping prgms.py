
#1.given two numbers,swap their values without using a third variable
x=10
y=20
x=x+y
y=x-y
x=x-y
print('x=',x,'y=',y)

#2.given two strings,swap their values
str1="hello"
str2="world"
str1,str2=str2,str1
print(str1,str2)

#3.given a list,swap its first and last elements
list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)

#4.given a string,swap the characters at positions i and j
s="hello"
i=1
j=3
output=''
for c in range(len(s)):
    if c==i:
        output=output+s[j]
    elif c==j:
        output=output+s[i]
    else:
        output=output+s[c]
print(output)
        
    
#5.given a list,swap elements at even indices with elements at odd indices
list1=[1,2,3,4,5,6]
#Output: [2, 1, 4, 3, 6, 5]

for i in range(0,len(list1),2):
    list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)

#6.given a list,swap every pair of elements and then reverse the entire list
list=[1,2,3,4,5,6]
i=0
while i>len(list)-1:
    list[i],list[i+1]=list[i+1],list[i]
list=list[::-1]
print(list)

#7.given two lists,swap their middle elements.if a list has an even number of elements,consider the latter middle
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
mid_index1=len(list1)//2
mid_index2=len(list2)//2
list1[mid_index1],list2[mid_index2]=list2[mid_index2],list1[mid_index1]
print('list1:',list1)
print('list2:',list2)

#8.given a list,swap every element with its mirrored position.for instance,the first element is swapped with the last,the second with the second last,and so on.
my_list=[1,2,3,4,5]
n=len(my_list)
for i in range(n//2):
    temp=my_list[i]
    my_list[i]=my_list[n-i-1]
    my_list[n-i-1]=temp
print(my_list)
