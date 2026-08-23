num1 = int(input('enter num1 value:'))
num2 = int(input('enter num2 value:'))
num3 = int(input('enter num3 value:'))
num4 = int(input('enter num4 value:'))
if num1>num2 or num1>num3 or num1>num4:
    print('largest number is num1')
elif num2>num1 or num2>num3 or num2>num4:
    print('largest number is num2')
elif num3>num1 or num3>num2 or num3>num4:
    print('largest number is num3')
elif num4>num1 or num4>num2 or num4>num3:
    print('largest number is num4')
else:
    print('invalid')
    
