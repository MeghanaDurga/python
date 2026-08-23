#1.create a base class Animal that has a method sound.extend this class with subclassed dog and cat where both provide their specific implementations for the sound they make
class Animal:
    def __init__(self,n):
        self.name=n
    def sound(self):
        print('sound:',self.name)
class Dog(Animal):
    def __init__(self,n):
        super().__init__(n)
    def sound(self):
        print(f'{self.name} says:Bow!')
class Cat(Animal):
    def __init__(self,n):
        super().__init__(n)
    def sound(self):
        print(f'{self.name} says:Meow!')
dog=Dog('Fluto')
cat=Cat('kitty')
dog.sound()
cat.sound()

#2.Develop a base class vehicle with a method type_of _vehicle.extend this class with subclasses Bike and Car,and provide specific types for each vehicle.
class Vehicle:
    def __init__(self,n):
        self.name=n
    def type_of_vehicle(self):
        print('type:',self.name)
class Bike(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def type_of_vehicle(self):
        print(f'{self.name} is a Two wheelers')
class Car(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def type_of_vehicle(self):
        print(f'{self.name} is a Four wheelers')
b=Bike('KTM')
b.type_of_vehicle()
c=Car('TATA NEXON')
c.type_of_vehicle()

#3.Design a base class Fruit with an attribute taste.extend this class with subclasses apple and orange,setting their specific taste in their constructors
class Fruit:
    def __init__(self,n):
        self.name=n
    def taste(self):
        print('taste:',self.name)
class Apple(Fruit):
    def __init__(self,n):
        super().__init__(n)
    def taste(self):
        print(f'{self.name} is a sweet')
class Orange(Fruit):
    def __init__(self,n):
        super().__init__(n)
    def taste(self):
        print(f'{self.name} is a citrusy')
a=Apple('Apple')
a.taste()
o=Orange('Orange')
o.taste()

#4.create a base class Bird that has a method fly.extend this class with subclasses sparrow and ostrich.while the sparrow can fly,the ostrich cannot.
class Bird:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print('name:',self.name)
class Sparrow(Bird):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        print(f'{self.name} can fly in the sky')
class Ostrich(Bird):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        print(f'{self.name} cannot fly in the sky')
s=Sparrow('Sparrow')
s.fly()
o=Ostrich('Ostrich')
o.fly()
        
#5.develop a base class shape with a method area.extend this class with subclasses square and circle.the subclasses should calculate their specific areas based on their attributes.
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        print('area:',self.name)
class Square(Shape):
    def __init__(self,name,side_lenght):
        super().__init__(name)
        self.side_length=side_lenght
    def area(self):
        return self.side_length**2
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
s=Square('Square',4)
res=s.area()
print('area of square:',res)
c=Circle('Circle',3)
res=c.area()
print('area of circle:',res)

#6.design a base class person with attributes name and age.extend this class with subclasses student and teacher.the student class should have an additional attribute grade,and the teacher class should have an attribute subject.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
student=Student('Meghana',21,'A')
teacher=Teacher('Durga',45,'English')
print('student name:',student.name,'student age:',student.age,'student grade:',student.grade)
print('teacher name:',teacher.name,'teacher age:',teacher.age,'teacher subject:',teacher.subject)


#7.design a class hierarchy for a university system.begin with base class universitymember with attributes name and id_number.extend this class with subclasses student and professor.the student class should have additional attributes like major and year,while the professor class should have department and checkingaccount.



#8.create a banking system.start with a base class account with methods deposit,withdraw,and balance.extend this class with subclasses savingsaccount and checkingaccount.savingaccount should have an added interest rate,while checkingaccount mayhave an oversraft limit.



#9.develop a system to manage products in a store.design a base class product with attributes name and price.extend this class with discountedproduct,which should apply a discount percentage to the product's price


#10.desin a class hierarchy for a transp














