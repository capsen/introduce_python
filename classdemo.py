class Employee:
    company = "Apple"
    def __init__(self, name, project, salary):
        self.name = name
        self._project = project
        self.__salary = salary

    def getmySalary(self):
        return self.__salary
    
    
    @staticmethod
    def sum_numbers(a, b):
        print(a+b)

e1 = Employee("Tom", "AI", 300000)
e2 = Employee("Jerry", "DevOps", 200000)
print(e1.name)
print(e1._project)
print(e1.getmySalary())
print(e2.getmySalary())

print(e1.company)
print(e2.company)

e1.company="Microsoft"
print(e1.company)
print(e2.company)

#test static method
e1.sum_numbers(3,6)
Employee.sum_numbers(4,9)

#normal method require instance as self
print(Employee.getmySalary(e1))


#demo 
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        return "Starting the engine..."

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    
    def open_trunk(self):
        return "Trunk is open"

my_car = Car("Toyota", "Camry", 4)
print(my_car.start())
print(my_car.open_trunk())
print(my_car.make)
print(my_car.doors)

# Polymophism demo
# how to use a common interface
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Elephant(Animal):
    def walk(self):
        return "Duang!"

dog = Dog()
cat = Cat()
elephant = Elephant()

print(dog.make_sound())
print(cat.make_sound())
print(elephant.make_sound())

class Horse(Animal):
    def make_sound(self):
        return "Neigh!"

horse = Horse()
print(horse.make_sound())