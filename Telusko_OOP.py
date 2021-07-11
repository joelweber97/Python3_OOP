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





comp1 = Computer('i5', 16) #when you instantiate the object it will call init automatically.
print(type(comp1))  #<class '__main__.Computer'>
print(comp1)
print(comp1.cpu)
print(comp1.ram)
comp2 = Computer('Ryzen 3', 8)
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

comp1.config()
comp2.config()


