year=int(input('enter an year:'))
if(year%4==0 and year%100!=0) or (year%400==0):
    print('it is an leap year')
else:
    print('it is not an leap year')
