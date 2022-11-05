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

######
#Constructor, self, and comparing objects in pythong
######

























