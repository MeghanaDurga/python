price = int(input('enter price:'))
if price >100:
    discount = price*20//100
else:
    discount=price*10//100
final_price =price-discount
print('final price after discount:$',final_price)
