#find the key of maxvalue in the dict
#output='c'
#find the key of minvalue in the dict
#output='d'
d={'a':27,'b':35,'c':69,'d':7}
max_char=max(d,key=d.get)
min_char=min(d,key=d.get)
print(max_char)
print(min_char)
