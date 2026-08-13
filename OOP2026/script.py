
#we can also use protected and private for methods as well as attributes

class BankAccount:
    MIN_BALANCE = 100 #static attribute

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction('deposit', amount)
        else:
            print('Deposit amount must be positive')

    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"logging {transaction_type} of ${amount}. New balance: ${self._balance}")


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount('Joe', 500)
account.deposit(200)


#account._is_valid_amount(200) #can access this outside of the class but we're not supposed to
#account.__log_transaction('withdraw', 300) #errors because we can't access it outside of the class

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))





'''

# a static method in python is a method that belongs to the class iteself rather than any instance of the class.
# to define a static method, we use the @staticmethod decorator

#both static and instance methods are stored in the class itself, not in each individual object

#static methods are ideal for tasks realted to the classes domain but dont' require any specific instance data
#eg utility functions

class BankAccount:
    MIN_BALANCE = 100 #static attribute

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print('Deposit amount must be positive')

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount('Joe', 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))


'''




'''
#statuc attributes (shared among all instances of the class)
# a static (or class) attribute is an attribute that belongs to the class itself, not to any specific instance of the class
#static attributes makes sense for:
    # counters and totals
    # shared constants (applicable accorss all instances) like a default value or configuration
    # class level configs (any setting that should be the same for all instances)


class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display(self):
        print(f'username: {self.username}, email: {self.email}')


user1 = User('joe', 'joe@email.com')
user2 = User('Jim', 'jim@gmail.com')


print(User.user_count) #can access user count as a class attribute
print(user1.user_count) #can also access it through an instance attribute
print(user2.user_count)
'''



'''
#accessing and modifying data:
# 1. traditional way - make the data private the use getters and setters
# 2.  properties


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print('email accessed')
        return self._email
    
    
    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self._email = new_email
    
    
user1 = User('dan', 'test1@email.com', 'pword')
user1.email = 'this is not an email@'
print(user1.email)


'''





'''

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email   #double unders actually make something private so we can't call the attribute at all outside of the class 
        self.password = password

    

    def get_email(self):
        print(f'email accessed at {datetime.now()}')
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email


    


joe = User('joe', 'test@email.com', 'pword')

print(joe.get_email())

joe.set_email('new_em@.com')

print(joe.get_email())



'''








'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hello, my name is {self.name} and i am {self.age} years old')



joe = Person('joe', 12)

joe.greet()


jim = Person('Jim', 23)

jim.greet()
'''


'''
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print('woof woof')

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner('Joel', '122 Springfield Dr', '888-8999')
owner2 = Owner('Tim', 'local address', 'local phone')

dog1 = Dog('Bruce', 'Scotty', owner1)
dog2 = Dog('Freya', 'Greyhound', owner2)

print(dog1.owner.name)

print(dog2.owner.name)'''