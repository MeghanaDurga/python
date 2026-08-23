#3.create a class calculator that performs basic arithmetic operations:addition,subtraction,multiplication,and division
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
x=calculator(4,2)
res=x.add()
print('addition:',res)

res=x.sub()
print('sub:',res)

res=x.multi()
print('multi:',res)

res=x.division()
print('division:',res)

#5.create a class student that represents a student's information,include name,roll number,and marks in three subjects.calculate the average marks and display the student's detils.
class student:
    def __init__(self,n,r,m1,m2,m3):
        self.name=n
        self.roll_no=r
        self.telugu_marks=m1
        self.english_marks=m2
        self.maths_marks=m3
    def info(self):
        print(self.name,self.roll_no)
    def getaverage(self):
        return(self.telugu_marks+self.english_marks+self.maths_marks)/3
s1=student('chinni',1,45,55,69)
s2=student('navya',2,58,69,70)
s3=student('meghana',3,57,68,69)

print('-'*20)
s1.info()
res=s1.getaverage()
print(res)

s2.info()
res=s2.getaverage()
print(res)

s3.info()
res=s3.getaverage()
print(res)


#8.create a class book that  represents a book with attributes like title,author,and publication year.implement a method to display book details
class Book:
      def __init__(self,t,a,p):
        self.title=t
        self.author=a
        self.publication_year=p
      def info(self):
        print('-'*20)
        print('title:',self.title)
        print('author:',self.author)
        print('publication_year:',self.publication_year)
b=Book('My Journey','APJ Abdual Kalam',2013)
b.info()


#7.create a class car that simulates a car with attribute like make,model,and current speed.implement methods to accelerate and brake the car.
class Car:
    def __init__(self,ma,mo):
        self.make=ma
        self.model=mo
        self.speed=0
    def car_info(self):
        print('car make:',self.make,',','car model:',self.model)
        
    def accelerate(self,value):
        self.speed=self.speed+value
        print('accelerate:',value,'speed is:',self.speed)
        
    def brake(self,value):
        self.speed=self.speed-value
        if self.speed<0:
            self.speed=0
        print('brake:',value,'speed is:',self.speed)
c=Car('mahindra','mahindra XUV700')
print('-'*20)
c.car_info()

c.accelerate(15)
c.accelerate(40)
c.brake(20)
    




#1.create a class rectangle that calculates the area and perimeter of a retangle.
'''area of rectangle=lenght*width
perimeter of rectangle=2*(lenght+width)'''

class rectangle:
    def __init__(self,l,w):
        self.lenght=l
        self.width=w
    def area(self):
        return(self.lenght*self.width)
    def perimeter(self):
        return(2*(self.lenght+self.width))
x=rectangle(2,4)
y=rectangle(4,2)
print('-'*20)
res=x.area()
print('area:',res)

res=y.perimeter()
print('perimeter:',res)


#2.create a class person that stores and displays information about a person's name and age.
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print('name:',self.name,'age:',self.age)
s=Person('chinni','21')
print('-'*20)
s.info()


#1.Create a class Circle that calculates the area and circumference of a circle    
'''area of circle =pie*r**2
circumference of circle=2*pi*r'''

class Circle:
    def __init__(self,r):
        self.radius = r
        self.pi = 3.14159 
    def area(self):
        return self.pi*self.radius**2

    def circumference(self):
        return 2*self.pi*self.radius

ci = Circle(5)
print('-'*20)
print('Area:',ci.area())
print('Circumference:',ci.circumference())

#6.create a class bank account that represents a simple bank account.implement methods for deposit,withdrawal,and checking the account balance
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance is:", self.balance)
acc = BankAccount()
print('-'*20)
acc.deposit(1000)
acc.withdraw(300)
acc.check_balance()


#9.create a class employee to represent employee information,including name,employee ID,and salary.implement a method to give a salary raise and display employee details
class Employee:
    def __init__(self,n,i,s):
        self.name= n
        self.employee_id=i
        self.salary=s
    def salary_raise(self,amount):
        self.salary=self.salary+amount
        print(self.salary)

    def display_employee(self):
        print('name:',self.name)
        print('employee_id:',self.employee_id)
        print('salary:',self.salary)
        
e=Employee('chinni',24,2400)
print('-'*20)
e.salary_raise(400)
e.display_employee()


#10.create a class Bank that represents a bank with attributes like name and location.implement methods to add and display account holder's names.
class Bank:
    def __init__(self,n,l):
        self.name=n
        self.location=l
        self.holder=[]
    def name(self):
        self.holder=self.holder.append()

b=Bank('Chinni','Hyderabad')
e.name('chinni')






#11.create a class shop that represnts an online shop.implement methods for adding products to the shop and displaying the list of available products.
class Shop:
    def __init__(self,p):
        self.product=p
    
        


'''class A:
    x=100
    def __init__(self,x):
        self.x=x
obj=A(10)
print(obj.x)'''
