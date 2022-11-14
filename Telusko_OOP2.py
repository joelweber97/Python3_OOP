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


'''
######
# Class and Objects
######


#the class is basically the blueprint of the objects an dthe objects are the instances
class Computer:
    #two things can go into a class....
    #attributes (variables) and behaviors (methods)
    

    def config(self):
        print('i5, 16gb, 1tb')


comp1 = Computer() #constructor
print(type(comp1)) # returns <class '__main__.Computer'> which shows that it's part of the computer class

#either line below is a way to call the config method on the comp1 instance of class Computer
Computer.config(comp1)
comp1.config()

comp2 = Computer()
Computer.config(comp2)
comp2.config()
'''


'''
######
__init__ method in Python
######


class Computer:

    #we use __init__ to initialize the variables
    #__init__ gets called automatically so we don't need to call the method
    #like we would other methods
    def __init__(self, cpu, ram): 
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

#setting the cpu variable for comp1 to i5
#and the ram variable for comp1 to 16
comp1 = Computer('i5', 16) 
#setting the cpu and ram variable for comp2 to r3 and 8
comp2 = Computer("r3", 8)

comp1.config() #returns i5, 16
comp2.config() #returns r3, 8
'''

'''
######
#Constructor, self, and comparing objects in pythong
######

class Computer:
    
    def __init__(self):
        self.name = 'Joel'
        self.age = 34
        #when creating the constructor each of the objects will have the
        #same valuefor name and age. 
        #we can, however, change the values


    def update(self):
        self.age=30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer() #this is a constructor
print(id(c1)) #print the address of c1
print(c1.age)

c2 = Computer() #this is a constructor
print(id(c2)) #the memory space is different than c1
print(c2.age)
#the size of an object depends on the number of variables
#the constructor is what allocates the size to the object.
#as mentioned each of the objects has the same value for name and age

#here we can change the value while constructing the data
c3 = Computer()
c3.age = 35
print(c3.age)

c1.age = 88
print(c1.age)

#now we can call the update method on a particular object
c1.update()
print(c1.age)



#now we create another function to compare the age of self (aka c1) 
#with a other object
if c1.compare(c2):
    print('they are same')

c1.age = 20
c2.age = 20

if c1.compare(c2):
    print('they are same')
'''


'''
########
#Types of variables in Python
#######

#instance variable:
    #as the object changes the value of the variable also changes
    #defined inside innit

#class variable:
    #variables that are common for all the objects
    #for instance, the number of wheels for all cars is 4
    #defined outside of innit


class Car:

    wheels = 4

    def __init__(self):
        self.mileage = 10 #instance variable
        self.make = 'BMW' #isntance variable


c1 = Car()
c2 = Car()

print(c1.mileage, c1.make)
print(c2.mileage, c2.make)

c1.mileage = 8
print(c1.mileage, c1.make)
print(c2.mileage, c2.make)


print(c1.mileage, c1.make, c1.wheels) #printing the class varialbe for each instance
print(c2.mileage, c2.make, c2.wheels)


#we can also print the wheels variable for the class, rather than a specific object
print(Car.wheels)


#we can change the class variable by using the class name
Car.wheels = 5
#now the wheels variable for all instances have changed as well.
print(c1.mileage, c1.make, c1.wheels)
print(c2.mileage, c2.make, c2.wheels)

'''

'''
########
# Types of methods in Python
########

# 3 types of methods: instance, class, and static

#instance methods are run directly on objects
#Within instance methods there are accessor methods and mutator methods
#accessor methods access the data
#mutator methods modify the data

#instance variables use the self keyword while 
#class methods use the cls keyword  and the @classmethod decorator
 
class Student:

    school = 'Telusko' #setting a class variable that applies to all objects

    def __init__(self, m1, m2, m3):
        self.m1 = m1 # 3 instance variables that get defined when creating the object
        self.m2 = m2
        self.m3 = m3


    def avg(self): #instance method because we pass in self which applies to the object itself
        return self.m1 + self.m2 + self.m3 / 3

    #accessor instance method that prints the value of m1
    def get_m1(self):
        return self.m1


    #mutator instance method that will change the value of m1
    def set_m1(self, m1_changed):
        self.m1 = m1_changed

    @classmethod  #must use decorator for class methods as well
    def get_school_name(cls): #the cls keyword is indicitive of a class method
        return cls.school


    #now we're going to create a static variable
    # use these when not concerned about instance or class variables
    #we have to use a special decorator for static variables, as well
    @staticmethod
    def info():
        print('This is a student class')

s1 = Student(74,22,47) #setting the instance variables during instantiation
s2 = Student(99,10,55)   

print(s1.school, s1.m1, s1.m2, s1.m3)
print(s2.school, s2.m1, s2.m2, s2.m3)

print(s1.avg()) #calling the instance method on an a specific object.
print(s2.avg()) #the avg method will work on every single object created

#calling the accessor instance method get_m1
print(s1.get_m1())
print(s2.get_m1())

#using the mutator instance method to change the value of m1 for each
s1.set_m1(55)
s2.set_m1(1000)
#then we will print the values of m1 for each s1 and s2
print(s1.get_m1())
print(s2.get_m1()) #the values for m1 in each of the instances have been changed

#now that we have the clas method school info we can print the school in 2 different
#ways, either using the school class variable or using the school_info class method
print(Student.school)
print(Student.get_school_name())


Student.info()
'''

'''
#########
# Inner Class in Python
#########
#creating a class within a class?
#lets say we have a student clas with all the variables and methods that students have
#but the we want info about the laptop
#in this case the laptop is it's own class because the latptop can have its own methods and variables
#only create an inner class when you know that class will only be used inside of another class
#for instance, if we know that Laptop will only be used by Student class
#we can add the laptop show method into the student show method which will
#print the student info and the laptop info

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.number)
        self.lap.show()

    class Laptop: # here we created the inner class of laptop
        #the laptop class is initialized in the __init__ method of the Student class
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 16
        def show(self): #we creted another show method but this only applies to the laptop class
            print(self.brand, self.cpu, self.ram)

s1 = Student("Joel", 2)
s2 = Student("Jenny", 3)

print(s1.name, s1.number)
#the above result is the same as creating a show() instance variable 
#that prints out the name and number (can be seen above and below)
s1.show()


#now we will call the brand of the inner Laptop class of the student class
print(s1.lap.brand)
lap1 = s1.lap
print(lap1.brand)


lap2 = s2.lap
print(lap2.ram)

# we can see each lap is different by printing the ids of each
print(id(lap1), id(lap2))



lap3 = Student.Laptop()
print(lap3.brand)


s1.show() #this prints the the output from the show method of the student class
    
    #def show(self):
    #    print(self.name, self.number)
    #    self.lap.show()

'''

'''
#######
# Inheritance in Python
#######

#whatever belongs to your parent also belongs to you
#the childs belongings don't belong to the parents though.

#there are 3 types of inheritance
#single inheritance
#multi-level inheritance
#and multiple inheritance

class A:
    def feature1(self):
        print('feature 1 working')
    
    def feature2(self):
        print('feature 2 is working')



class B(A):   #class B is inheriting all the features of class A
    def feature3(self):
        print('feature 3 working')
    
    def feature4(self):
        print('feature 4 is working')

class D:
    def feature6(self):
        print('feature 6')

class C(B):
    def feature5(self):
        print('feature 5 works')

class E(A, D):  #here E is inheriting from A and D
    def feature7(self):
        print('feature 7')

class F(B, D): #here F is inheriting from D and B (which also inherits from A)
    def feature8(self):
        print('feautre 8')

a1 = A()
print('A')
a1.feature1()
a1.feature2()
print("B")
b1 = B()
b1.feature3()
b1.feature4()

#what if we want to get the methods of class A to work with class B?
#we can make B a child class of A using the class B(A): syntax

b1.feature1()

c1 = C()
print('C')
c1.feature1()
c1.feature2() 
c1.feature3() 
c1.feature4() 
c1.feature5()

#as you can see the child class can inherits all the things
#from parent, grandparent, great grandparent, etc.

# we can also inheritsfrom multiple classes that arent' related
#we can see that class D isn't related 

e1 = E()
e1.feature1()
e1.feature2()
e1.feature6()
e1.feature7()


f1 = F()
#f1.feature 1,2,3,4,6,8 are available
#since F inherits from D and B which inherits from A

'''


'''

########
#Constructor in inheritance
#Method Resolution Order
########

class A:

    def __init__(self):
        print('in A innit')

    def feature1(self):
        print('feature1 working')
    def feature2(self):
        print('feature2 working')

class B(A): #in total class B has 4 methods (aka 4 features)
    def feature3(self):
        print('feature3 working')
    def feature4(self):
        print('feature4 working')


a1 = A() #you can only access features of class A here
a2 = B() #you can access features of class A and class B here
#if class B doesnt have it's own constructor the __Init__ constructor
#will be called when class B is instantiated, as you can see above

class C:

    def __init__(self):
        
        print('in C innit')

    def feature1(self):
        print('feature1 working')
    def feature2(self):
        print('feature2 working')

class D(C): #in total class D has 4 methods (aka 4 features)

    def __init__(self):
        
        print('in innit D') 
    def feature3(self):
        print('feature3 working')
    def feature4(self):
        print('feature4 working')

a3 = C()
a4 = D() #when clas D has an innit it will overwrite the innit from its parent clas
#this is different from clas B which had no innit so it used class A's innit

#when there's no innit in the subclass the subclass will use the innit from the super clas


class E(C):
    def __init__(self):
        super().__init__()
        print('in E innit')

#what if you want to call the innit from C and D?
#we use the super().__init__() call to get the innit from the superclass, as well
#now you can see below that 


a7 = E() # we can see that C innit and E innit is both printed


#now we'll look at multiple inheritance example

class F:
    def __init__(self):
    
        print('in innit F') 

    def feature1(self):
        print('feature 1F working')
    def feature2(self):
        print('feature2 working')

class G:
    def __init__(self):
        
        print('in innit G') 
    def feature1(self):
        print('feature 1G working')
    def feature4(self):
        print('feature4 working')

class H(F,G):

    def __init__(self):
        super().__init__()
        print('in innit H') 

    def feat(self):
        super().feature2() #using the super method to call feature 2 from class F

a8 = H() # at first it's only calling H's innit
#when when we add super.__init__(self) it calls innit from F and H and ignores G
#this relates to the method resolution order (MRO)
#1) tries to find the init of itself
#2)when callling super it always moves from left to right (top to bottom?)
#which is why the super() of H called the innit from F but not G


#the same can be done with methods
#since F and G both have a method with the same name when we call
#feature1 from H it will always call the top method... in this case from class F
a8.feature1() 

#can also use super method to call methods from a different class

a8.feat()

'''



########
# Intro to Polymorphism
########

#many forms
#behaving differently under different scenarios.

#important when it comes to loose coupling, dependency injection, and interfacing
#which we will talk about later.

#4 ways of implementing polymorphism
#1. Duck Typing
#2. Operator Overloading
#3. Method Overloading
#4. Method Overriding



"""

##########
# Duck Typing
##########

#duck test - if it looks like a duck, quacks like a duck, and swims like a duck
#its a duck

x = 5

x = "joel"

#each of the two variables have their own memory space and the x
#is the name attached to that space. so the x doesn't have a type....
#we're actually returning the type of 5 or the type of 'joel' instead

#the variable name is just a name to specific memory space

class PyCharm:
    def execute(self):
        print('compiling')
        print('running')


class MyEditor:
    def execute(self):
        print('spellcheck')
        print('convention check')
        print('compiling')
        print('running')

class Laptop:

    def code(self, ide):
        ide.execute()


ide = PyCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)

#as long as PyCharm() and MyEditor() classes both have the execute
#method they can both be called in the Laptop().code method

"""

"""

#########
#Operator Overloading
#########

#in python we can add integers, an integer and float, 2 strings
#but not an int and string or float and string

a = 5
b = "world"
c = 6
#print(a+b) #throws error
print(a + c)

#behind the scenese the code is calling __add__(a,c) onto the int class
print(int.__add__(a,c))

#if we add 2 strings together it calls the __add__(a,b) method on the str clas
print(str.__add__('test', 'test'))

#The + operator calls the __add__() method
#the - operator calls the __sub__() method
#the * operator calls the __mul__() method
#the / operator calls the __div__() method




class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(60,65)

#s3 = s1 + s2    
# this throws an error because we cannot add 2 class objects
# because the student class doesn't have an add method
# now we added a __add__ method which calls Student.__add(s1,s2)
s3 = s1+s2
print(s3.m1)

#so if we want to use an operator between 2 classes we need to overload
#the operator becausethe student class doesn't know what that + means


# now lets see if 1 object is greater in size than another object
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

#this trhwos an error unless we overload and define a greater than method above




a = 9
print(a)

#when we print a varaible it's actually printing the value
#instead of the memory location that gets printed when we print an object
#that's because its actually running print(a.__str__())
#if we wanna actually print out the values of the object
#we need to override the __str__() method
print(s1.__str__()) #now it prints the values rather than the address.
print(s2)


"""

##########
#Method overloading and Method overriding
###########


#method overloading -> in a class if you have 2 methods with the same name
#but different parameters 

'''
class Student"
    def average(a,b)

    def average(a,b,c)
    
'''
# in python we don't have method overloading so we cannot create
# 2 methods with the same name


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # if we set each param to None we don't have to use all 3 when calling
    #the method. You can see below that we're only passing 2 values into 
    #the sum method
    def sum(self, a= None, b = None, c = None): 

        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s1 = Student(58,69)

print(s1.sum(5,9))
print(s1.sum(23,1,45))
print(s1.sum(23))





#method overriding -> 2 classes have a method with the same name which get inherited
























