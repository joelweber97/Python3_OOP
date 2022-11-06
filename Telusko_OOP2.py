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


































































