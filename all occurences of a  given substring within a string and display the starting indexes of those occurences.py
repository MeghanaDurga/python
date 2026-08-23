main_string="bananas are banana-flavored banana snacks"
substring="banana"
position=[]
for i in range(0,len(main_string)):
    if main_string[i:i+len(substring)]==substring:
        if i!=0:
            position.append(i)
print("Substring found at index positions:", position)
