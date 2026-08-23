#output={1:'a',2:'b',3:'c'}
d={'a':1,'b':2,'c':3}
output={}
for k in d:
    value=d[k]
    output[value]=k
print(output)
