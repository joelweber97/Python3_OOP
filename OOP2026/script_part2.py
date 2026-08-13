

#polymorphism - derivded from greek and means having multiple forms
#ability of an object to take many forms

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('vehicle starting')

    def stop(self):
        print('stopping vehicle')


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print('car is starting')
    
    def stop(self):
        print('car is stopping')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print('bike is starting')

    def stop(self):
        print('bike is stopping')

class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors


vehicles: list[Vehicle] = [Car('Ford', 'Focus', 2008, 5),
            Motorcycle('Honda', 'Scoopy', 2018),
            Plane('Gulfstream', 'G6', 2025, 3)]


for v in vehicles:
    print(f'inspecting {v.brand} {v.model} ({type(v).__name__})')
    v.start()
    v.stop()
    #if isinstance(v, Vehicle):
    #    print(f'inspecting {v.brand} {v.model} ({type(v).__name__})')
    #    v.start()
    #    v.stop()






#WITHOUT POLYMORHPISM THE CODE IS UGLY AS HELL WHEN LOOPING THROUGH A VARIETY OF CLASSES
#class Car:
#    def __init__(self, brand, model, year, number_of_wheels):
#        self.brand = brand
#        self.model = model
#        self.year = year
#        self.number_of_wheels = number_of_wheels
#
#    def start(self):
#        print('car is starting')
#
#    def stop(self):
#        print('car is stopping')
#
#
#class Motorcycle:
#    def __init__(self, brand, model, year):
#        self.brand = brand
#        self.model = model
#        self.year = year
#
#    def start_bike(self):
#        print('motorsycle is starting')
#
#    def stop_bike(self):
#        print('motorcycle is stopping')
#
#
##create list of vehicles to inspect
#vehicles = [
#    Car('Ford', 'Focus', 2008, 5),
#    Motorcycle('Honda', 'Scoopy', 2018)
#]
#
#for v in vehicles:
#    #v.start  #because there is no common method for all vehicles we can't call the start() method or start_bike method 
#    if isinstance (v, Car):
#        print(f'inspecting {v.brand} {v.model} ({type(v).__name__})')
#        v.start()
#        v.stop()
#    elif isinstance(v, Motorcycle):
#        print(f'inspecting {v.brand} {v.model} ({type(v).__name__})')
#        v.start_bike()
#        v.stop_bike()
#    else:
#        raise Exception('object is not a valid vehicle')






'''#inheretance - fundamental concept in oop that involves creating new 
# classes (subclasses or derived classes) based on exsiting classes 
# (superclasses or base classes)

#a car is-a vehicle and a bike is-a vehicle  inheretance is kind of a 'is-a' relationship


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('turn on')

    def stop(self):
        print('vehicle is stopping')


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car = Car('Ford', 'Focus', 2008, 4, 4)
bike = Bike('Honda', 'Scoopy', 2018, 2)


print(car.__dict__)
print(bike.__dict__)

car.start()
car.stop()
'''


'''#abstraction - reduce complexity by hiding unnecessary details

class EmailService:

    def _connect(self):
        print('connecting to email server')

    def _authenticate(self):
        print('authenticating')

    def send_email(self):
        self._connect()
        self._authenticate()
        print('sending email')
        self._disconnect()

    def _disconnect(self):
        print('disconnecting from email server')


email = EmailService()
email.send_email()


    '''


'''
#Encapsulation - bundling the data (attributes and methods) into a single unit called a class
#hides internal implementation details of a class by only exposing necessary functionality to outside world

class BadBankAccount: #band bank account has no encapsulation
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)



class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self._balance += amount

    def withraw(self, amount):
        if amount <= 0:
            raise ValueError('Withraw amount must be positive')
        if amount > self._balance:
            raise ValueError('Insifficient Funds')
        self._balance -= amount


account = BankAccount()
print(account.balance)

account.deposit(1.99)
print(account.balance)

account.withraw(0.99)
print(account.balance)

'''