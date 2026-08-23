#write a python program to find second highest value key in a dictionary
#output=rama
d={'rama':67,'sita':76,'hanuma':6,'ram':7}
first_value=float('-inf')
second_value=float('-inf')
first_key=None
second_key=None
for key,value in d.items():
    if first_value<value:
        second_value=first_value
        first_value=value
        second_key=first_key
        first_key=key
print(second_key)
