#1.given a string,slice it to extract the first 3 characters
input="Vcube"
output=input[0:3]
print(output)

#2.reversing a list using slicing
st=[1,2,3,4]
output=st[::-1]
print(output)

#3.slicing a tuple
x=[10,11,12,13,14]
res=x[0:3]
print(res)

#4.modify a list using slicing
st=[100,200,300,400]
st[1]=500
print(st)

#4.modify a list using slicing
st=[100,200,300,400]
st.remove(200)
st.insert(1,500)
print(st)

#5.extract even-indexed characters from a string
input="Vcube Solutions"
res=input[::2]
print(res)

#6.slicing a list of list
x=[1,[2,3,4],5,6]
res=x[1][1:]
print(res)

#7.slicing a string in reverse
input="Vcube"
output=input[::-1]
print(output)

#8.slicing with a step of 3
input="python"
output=input[::3]
print(output)

#9.reversing a list of strings
input=["vcube","python","java"]
output=[s[::-1] for s in input]
print(output)

#10.slicing a string with a step value
input="Vcube Solution"
output=input[::3]
print(output)

#11.concatenating lists by using slicing
L1=[1,2,3,4]
L2=[5,6,7]
L1[len(L1):]=L2
print(L1)

#12.remove duplicates from a list using slicing
input=[1,2,3,1,4,5,2]
output=[]
for i in input:
    if i not in output:
        output.append(i)
print(output)

#13.write a python program to reverse the order of words in a given string by slicing and joing
input="Python"
output=input[::-1]
print(output)

#14.flattening nested lists by using slicing
nested_list=[[1,2],[3,4],[5,6],[7,8]]
flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)

#15.finding the maximum value in a given list by slicing
input=[10,11,12,13,14,15]
max=0
for i in input:
    if i>max:
        max=i
print(max)

#16.write a python program that count the number of occurences of substring in string by slicing
input="Raja"
substring="aja"
count=0
for i in range(len(input)-len(substring)+1):
    if input[i:i+len(substring)]==substring:
        count=count+1
print(count)

#17.given a string 's',determine if it is a palindrome by slicing and checking
st="mom"
if st==st[::-1]:
    print('palindrome')
else:
    print('not palindrome')

#18.given two dictionaries 'dict1' and 'dict2',merge them together by slicing and combining selected keys
dict1={'a':1,'b':2,'c':3}
dict2={'x':10,'y':20,'z':30}
keys1=['a','b']
keys2=['y','z']
merged={k:dict1[k] for k in keys1 if k in dict1}
merged.update({k:dict2[k] for k in keys2 if k in dict2})
print(merged)
