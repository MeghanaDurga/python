num1 = int(input('enter num1 value:'))
num2 = int(input('enter num2 value:'))
num3 = int(input('enter num3 value:'))
if num1>num2 or num1>num3:
    print('smallest number is num1')
elif num2>num3 or num2>num1:
    print('smallest number is num2')
elif num3>num1 or num3>num1:
    print('smallest number is num3')
else:
    print('invalid')
