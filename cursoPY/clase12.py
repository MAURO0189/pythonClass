numbers = {1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco"}
print(numbers)
print(numbers[2])

imformation = {"name":"Juan", "age":22, "city":"Bogota", "height":1.75}
print(imformation)
del imformation["age"]
print(imformation)
claves = imformation.keys()
print(claves)
#print(type(claves))
values = imformation.values()
print(values)
pairs = imformation.items()
print(pairs)

contacts = {"Mauro": {"Apellido": "Yepes", "Altura": 1.80, "Edad": 35}, "Juan":{"Apellido": "Perez", "Altura": 1.70, "Edad": 38}}

print(contacts)
print(contacts["Juan"])