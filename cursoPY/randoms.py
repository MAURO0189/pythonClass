import random

# Generar un número entero aleatorio 
random_number = random.randint(1, 10)
print(f"El número aleatorio es: {random_number}")

# Elegir colores aleatorios de una lista
colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
random_color = random.choice(colores)
print(f"El color aleatorio es: {random_color}")


# Barajar una lista de cartas
cartas = ["As", "Rey", "Reina", "Joker", "10"]
random.shuffle(cartas)
print(f"Las cartas barajadas son: {cartas}")