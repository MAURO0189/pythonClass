class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f'Hello, my name is {self.name}, have {self.age} years old, and my salary is {self.salary}'


employee1 = Employee(f'Carl', 30, 4500.0)
print(employee1.introduce())        