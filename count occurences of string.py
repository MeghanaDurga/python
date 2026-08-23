s1='python is fun fun '
s2='fun'
cnt=0
for i in range(0,len(s1)):
    if s1[i:i+len(s2)]==s2:
        cnt=cnt+1
print(cnt)        
               
