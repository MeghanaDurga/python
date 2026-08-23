x=[4,2,5,12,14,20]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print("sorted list:",x)
print("minimum:",min(x))
print("maximim:",max(x))
    
    
