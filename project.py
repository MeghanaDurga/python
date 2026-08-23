#PROJECT
veg=['potato','cabbage','carrot','onion']
quantity=[20,40,60,80]
cost_price=[10,20,30,35]
sale=[15,25,35,45]
profit=[]
total_earning=0
total_profit=0
cart=[]
user_cart=[]
user_quant=[]
sold_quantity = [0]*len(veg)
item_profit = [0]*len(veg)
customer_history = []

while True:
    print('*'*10,"INVENTORY MANAGEMENT",'*'*10)
    select_role=input("select role(Owner/User/Exit):")
    if select_role=='1':
        user=input('enter a name:')
        password=input('enter password:')
        if user=='meghana' and password=='123':
            while True:
                print('1.Add')
                print('2.Remove')
                print('3.Update')
                print('4.View')
                print('5.Sales Report')
                print('6.Exit')
                ch=int(input('choose your option:'))
                if ch==1:
                    print('-'*4,"ADD",'-'*4)
                    item=input('which item you want to add:')
                    if item in veg:
                        print(item,'is already available in cart') 
                    else:
                        qty=int(input('how many kgs you want:'))
                        c_price=int(input('enter cost price of veg:'))
                        s_price=int(input('enter selling price of veg:'))
                        veg.append(item)
                        quantity.append(qty)
                        cost_price.append(c_price)
                        sale.append(s_price)
                        profit.append(0)
                        sold_quantity.append(0)     
                        item_profit.append(0)
                        print(item,'is added to cart')
                elif ch==2:
                    print('-'*4,"REMOVE",'-'*4)
                    item=input('which item do you want to remove:')
                    if item in veg:
                        idx=veg.index(item)
                        veg.pop(idx)
                        quantity.pop(idx)
                        cost_price.pop(idx)
                        sale.pop(idx)
                        sold_quantity.pop(idx)      
                        item_profit.pop(idx)
                        print(item,'has been removed from cart')
                    else:
                        print(item,'is not available in cart')
                elif ch==3:
                     print('-'*4,"update",'-'*4)
                     item=input('Enter the name of the veg you want to update:')
                     if item in veg:
                         idx=veg.index(item)
                         update_qty=input('Do you want update the qty of veg(Yes/No):')
                         if update_qty=='yes':
                             new_qty=int(input('which kgs you want to update:'))
                             quantity[idx]=new_qty
                         update_cprice=input('Do you want update the cost price of veg(Yes/No):')
                         if update_cprice=='yes':
                             new_cprice=int(input('which cost price you want to update:'))
                             cost_price[idx]=new_cprice
                         update_sprice=input('Do you want update the selling price of veg(Yes/No):')
                         if update_sprice=='yes':
                             new_sprice=int(input('which selling price you want to update :'))
                             sale[idx]=new_sprice
                         print(item,'has been update in cart')
                     else:
                         print(item,'is not available in cart')
                elif ch==4:
                    print('-'*4,"VIEW",'-'*4)
                    for v,q,c in zip(veg,quantity,cost_price):
                        print(v,"-",q,'kgs',"-",c,'Rs')
                elif ch==5:
                    print('*'*20,"SALES REPORT",'*'*20)
                    print("Customer Purchase History:")
                    for cust in customer_history:
                        name=cust[0]
                        phone=cust[1]
                        purchase=cust[2]
                        total_paid=cust[3]
                        print("Name:",name,"Phone:",phone)
                        print("Purchased Items:")
                        for item_info in purchase:
                            print(" ", item_info[0], "- Qty:", item_info[1], "- Price: Rs.", item_info[2], "- Total: Rs.", item_info[3])
                        print("Total Paid:Rs.",total_paid)
                    print('-'*50)
                    print("Vegetable   In Stock   Sold   Item Profit")
                    print('-'*50)
                    for i in range(len(veg)):
                        print(veg[i],' '*5, quantity[i],' '*5, sold_quantity[i],' '*5,"Rs.",item_profit[i])
                    print("Financial Summary:")
                    total_rev=0
                    for cust in customer_history:
                        total_rev=total_rev+cust[3]
                    print("Total Revenue:Rs.",total_rev)
                    print("Total Profit:Rs.",sum(item_profit))
                    print('*'*50)
                elif ch==6:
                    print('Exiting...')
                    break
                else:
                    print('invalid command')
    elif select_role=='2':
        while True:
            print('1.Add')
            print('2.Remove')
            print('3.Modify')
            print('4.view')
            print('5.Billing')
            print('6.Exit')
            total=0
            
            ch=int(input('choose your option:'))
            if ch==1:
                print('-'*4,"ADD",'-'*4)
                item=input('which item you want  to add:')
                if item in user_cart:
                    print(item,'is already in cart')
                else:
                    qty=int(input('how many kgs you want:'))
                    user_cart.append(item)
                    user_quant.append(qty)
                    print(item,'added to cart')
            elif ch==2:
                print('-'*4,'REMOVE','-'*4)
                item=input('which item do you want to remove:')
                if item in user_cart:
                    idx=user_cart.index(item)
                    user_cart.pop(idx)
                    user_quant.pop(idx)
                    print(item,'removed from cart')
                else:
                    print(item,'is not in the cart')
            elif ch==3:
                print('-'*4,'MODIFY','-'*4)
                item=input('which item do you want to modify:')
                if item in user_cart:
                    modify=user_cart.index(item)
                    qty=int(input('how many kgs do you want to modify:'))
                    user_quant[modify]=user_quant[modify]-qty
                    print(item,'is modify')
                else:
                    print(item,'is not modify')
            elif ch==4:
                print('-'*4,'VIEW','-'*4)
            
                for v,q in zip(user_cart,user_quant):
                    print(v,"-",q,"kgs")
            elif ch==5:
                print('-'*4,'BILL','-'*4)
                customer_name = input("Enter your name: ")
                customer_phone = input("Enter your phone number: ")
                purchase = []
                total = 0
                for item, qty in zip(user_cart, user_quant):
                    if item in veg:
                        idx = veg.index(item)
                        if quantity[idx] >= qty:
                            total_price = qty * sale[idx]
                            profit_amount = (int(sale[idx]) - cost_price[idx])* qty
                            purchase.append([item, qty, sale[idx], total_price])
                            total = total + total_price
                            quantity[idx] = quantity[idx] - qty
                            sold_quantity[idx] = sold_quantity[idx] + qty
                            item_profit[idx] = item_profit[idx] + profit_amount
                        else:
                            print("Insufficient stock for", item, "-", quantity[idx], "kg available.")
                    else:
                       print(item, "is not in stock.")
                print("-"*4," BILL RECEIPT", "-"*4)
                for item_info in purchase:
                    print(item_info[0], "- Qty:", item_info[1], "- Price: Rs.", item_info[2], "- Total: Rs.", item_info[3])
                print("Total Paid: Rs.", total)
                customer_history.append([customer_name, customer_phone, purchase, total])
                user_cart.clear()
                user_quant.clear()
            elif ch==6:
                print('Thank you for visiting!')
                break
            else:
                print('invalid choice')
    elif select_role == '3':
        print('Exiting program....')
        user_cart.clear()
        user_quant.clear()
        break
    else:
        print('invalid input, please choose correct option')



                
    

            
            

        
                   
