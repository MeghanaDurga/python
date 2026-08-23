num=[10,3,5,8,13,20,17,22]
s=[]
for i in num:#10
   for d in range(2,(i//2)+1):#10//2
      if i%d==0:#
        break
   else:
       s.append(i)
print(s)
       
