#write a python program to find the second highest value key in a given dictionary
d={'a':67,'s':76,'b':24,'e':676}
values=list(d.values())
values.sort(reverse=True)
second_highest=values[1]
for key in d:
    if d[key]==second_highest:
        print("second highest value is:",key)
    
