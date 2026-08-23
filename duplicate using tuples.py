#find duplicate values for the given tuples
t=(1,2,3,1,2,4,6,2,1)
duplicate=[]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i]==t[j] and t[i] not in duplicate:
            duplicate.append(t[i])
print(duplicate)
    
               
               
               
               
             
