s1="listen"
s2="silent"
sorted_s1=sorted(s1)
sorted_s2=sorted(s2)
anagram=sorted_s1==sorted_s2
if anagram:
    print("yes")
else:
    print("no")
