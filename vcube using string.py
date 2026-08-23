s='vcube'
output=' '
i=0
for char in s:
    if i%2==0:
        output=output+char.upper()
    else:
        output=output+char.lower()
    i=i+1
print(output)
