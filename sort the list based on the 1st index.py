#write a python to sort the list based on the 1st index
#output=[(1,4),(97,7),(9,67),(7,76),(6,104)]
d=[(9,67),(7,76),(1,4),(97,7),(6,104)]
for i in range(0,len(d)):
    for j in range(0,len(d)-1):
        if d[j][1]>d[j+1][1]:
            d[j],d[j+1]=d[j+1],d[j]
print(d)
