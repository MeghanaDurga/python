#[10,30,40,100,90,99]
#output=[99] second largest

def second_largest(list):
    largest=second=float('-inf')
    for num in list:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    return [second] if second!=float('-inf') else[]


a=[10,30,40,100,90,99]
output=second_largest(a)
print(output)
