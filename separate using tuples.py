#separate the elements in tuples in the given list
l=[1,[2,3,4],(1,2,3),4,5,6,{7,1},(1,5,6)]
separate=[]
for i in l:
    if type(i)==tuple:
        for j in i:
            separate.append(j)
output=tuple(separate)
print(output)
