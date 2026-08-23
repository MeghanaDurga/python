n1 = int(input('enter n1 value:'))
n2 = int(input('enter n2 value:'))
n3 = int(input('enter n3 value:'))
if n1>n2 or n1>n3:
    print('largest number is n1')
elif n2>n1 or n2>n3:
    print('largest number is n2')
elif n3>n1 or n3>n2:
    print('largest number is n3')
else:
    print('not valid')
