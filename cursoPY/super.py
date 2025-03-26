class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'Name: {self.name} - Age: {self.age}')

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')


class Student(Person):
    def __init__(self, name, age, school, student_id):
        super().__init__(name, age)
        self.school = school  
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f'I am a student at {self.school} with ID {self.student_id}')

student = Student('John', 25, 'MIT', '1234')
student.greet()                      