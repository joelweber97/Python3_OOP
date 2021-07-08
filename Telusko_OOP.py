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
comp2 = Computer('Ryzen 3', 8)

print(comp2.cpu)


comp1.config()
comp2.config()


