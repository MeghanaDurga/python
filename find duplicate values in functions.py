#a=[10,20,30,40,10,20]
#output=[10,20]

def find_duplicate(list):
    duplicate=[]
    for item in list:
        if list.count(item)>1 and item not in duplicate:
            duplicate.append(item)
    return duplicate

a=[10,20,30,40,10,20]
output=find_duplicate(a)
print(output)
                
