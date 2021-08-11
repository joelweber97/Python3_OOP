# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:18:27 2021

@author: joelw
"""

''' think about an object,
think about a group of objects
and think about how you can connect them'''

'''objects have somewhere to store data and some behavior'''

'''
the class is the design
the object is the instance
'''
'''
2 things we can put into a class
attributes (variables) and behaviors (methods)
'''


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print('in init')
    
    
    def config(self):
        print('config is ', self.cpu, self.ram)


    def update(self):
        #the whole purpose of update method is to change the cpu of whatever it is called on to 'none'
        self.cpu = 'none'

    def compare(self, other):
        if self.cpu == other.cpu:
            return True
        else:
            return False
        

comp1 = Computer('i5', 16) #when you instantiate the object it will call init automatically.
print(type(comp1))  #<class '__main__.Computer'>
print(comp1)
print(comp1.cpu)
print(comp1.ram)
comp2 = Computer('Ryzen 3', 8)
print(comp2)
print(comp2.cpu)
print(comp2.ram)

#each time you create an object it takes up different space in memory.
#what is the size of an object? depends on the number of variables(attributes) of the object.
#who allocates the size to an object? the constructor.
#in this case the constructor is Computer() which calls __init__ automatically.
print(id(comp1))
print(id(comp2))



#in order to change the variables(attributes) of an object we simply do this
comp1.cpu = 'Ryzen 9'
print(comp1.cpu)

comp1.config()
comp2.config()


#now we will use the update method to update the cpu for comp1
comp1.update()
print(comp1.cpu)
print(comp2.cpu)


#use the compare method to compare comp1 and comp2
if comp1.compare(comp2):
    print('they are the same')
else:
    print('they are different')
    
    
    
#2 different types of variables. instance variable and class variable
class Car:
    
    #if we define a variable outside init it becomes a class variable
    wheels = 4
    #wheels variable is not specific to individual instances of an object.
    #wheels is common among all instances (i.e. the entire class)
    
    def __init__(self):
        self.mileage = 10
        self.company = 'BMW'
        #mileage and company are both instance variables
        #as the car (object) changes these values also change.
        #instance variables are defined inside init
        

car1 = Car()
car2 = Car()

print(car1.company, car1.mileage)
print(car2.company, car2.mileage)

#here we are changing this instance variable for car1
car1.mileage = 8
print(car1.company, car1.mileage, car1.wheels)
print(car2.company, car2.mileage, car2.wheels)

#instance variables are different for different objects.
#if we change the variable for one object it won't affect the variable for a different object.



#we can actually change the class variable as well, but it needs to be called on the class
Car.wheels = 5
print(car1.company, car1.mileage, car1.wheels)
print(car2.company, car2.mileage, car2.wheels)
#now all the car objects have changed to have 5 wheels.



''' 3 types of methods
    instance methods - 
    class methods - 
    static methods - 
    '''

class Student:
    #static (class) variable
    school = 'Telusko'

    #instance variable.
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #create an instance method.
    # we can tell it's an instance method because we pass in self.
    def average(self):
        return (self.m1 + self.m2 + self.m3)/3


    #2 types of instance methods - accessor methods and mutator methods.
    #accessors just fetch the value of the instance variable
    #mutators modify the instance variable
    
    #get methods are accessor instance methods
    def get_m1(self):
        return self.m1
    #set methods are mutator instance methods
    def set_m1(self, value):
        self.m1 = value


    #class methods - in this case school is a class variable. We need class methods to work with these variables
    #to define a class method we need to use the @classmethod decorator
    @classmethod
    def getSchool(cls): #cls notates class
        return(cls.school)

    #static methods
    #when you're not interested in class variables or instance variables we can use a static method
    #for instance, if you want to print the info about the class.
    #leave the parens empty if you don't want to it be related with a class or an instance.
    #use the @staticmethod decorator
    @staticmethod
    def info():
        print("this is Student class... in abc module")



s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)
#m1, m2, and m3 are instance variables in this example
#school is a static variable

print(s1.m1, s1.m2, s1.m3, s1.school)

# we will create a method above to find the average of values
# we will then call that method on student 1
print(s1.average())
print(s2.average())


#here we will call the get accessor instance method get_m1
print(s1.get_m1())
print(s2.get_m1())

#we will also call the set mutator instance method
s1.set_m1(33)
s2.set_m1(10)

print(s1.m1)
print(s2.m1)


#now we will call the class method on the student class.
#to do this we don't use the instances, we put the method onto the entire class
#remember to use the @classmethod decorator when defining the class method.
print(Student.getSchool())



#now lets call the static info method
#make sure to inclue the @staticmethod decorator when creating it

Student.info()


#inner class
#when you know a class will only be used with another class.
#the laptop class will only be called on the student class so you
#don't have to create 2 separate outer classes.
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)


    # we will create another class for laptop within the student class
    #since each student will have their own laptop.
    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8




s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)


print(s1.name, s1.rollno)
s1.show()
#need to call it this way because the lap class is within the student class
s1.lap.brand


lap = s1.lap
lap2 = s2.lap

print(lap, lap2)