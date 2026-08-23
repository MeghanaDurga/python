#1.given a list of numbers,sort them in ascending order
x=[5,2,7,1,3]
x.sort()
print(1,x)

#2.given a list of strings,sort them alphabetically
x=['apple','banana','orange','grape','pear']
x.sort()
print(2,x)

#3.given a list of strings,sorted them by their lenght
x=['apple','banana','orange','grape','pear']
res=sorted(x,key=len)
print(3,res)

#4.given a list of numbers,sort them in descending order
x=[5,2,7,1,3]
x.sort()
x.reverse()
print(4,x)

#5.given a list of tuples where each tuple contains two elements,sort the list based on the second element of each tuple
x=[(1,5),(2,3),(3,8),(4,1),(5,6)]
output=sorted(x,key=lambda a:a[1])
print(5,output)

#6.given a list of words,sort them based on their last character
x=['apple','banana','orange','grape','pear']
output=sorted(x,key=lambda a:a[-1])
print(6,output)

#7.given a list of integers and strings,sort them such that all strings are on the left and all integers are on the right
x=["apple",3,"banana",1,"orange",5]
strings=[item for item in x if isinstance(item, str)]
integers=[item for item in x if isinstance(item, int)]
output=strings + integers
print(7,output)

#8.given a list of words,sort them based on the count of vowels in each word.if two words have the same vowel count,maintain their relative order.
x=["apple","banana","orange","grape","pear"]
output=sorted(x,key=lambda a:a[-2])
print(8,output)

#9.given a list of numbers,sort the list such that all even numbers are on the left and all odd numbers are on the right,with both sections sorted in ascending order
y=[5,2,8,1,7,4,3,6]
evens=sorted([num for num in y if num % 2 == 0])
odds=sorted([num for num in y if num % 2 != 0])
output=evens+odds
print(9,output)
