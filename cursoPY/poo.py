class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

person1 = Person('David', 30)
person2 = Person('Carla', 25)

person1.say_hello()
person2.say_hello()
