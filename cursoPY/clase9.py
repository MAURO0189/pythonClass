to_do = ['comer', 'dormir', 'estudiar', 'trabajar']
print(to_do)

numbers = [1, 2, 3, 4, 5, "seis"]
print(numbers)

mix = ["uno", 2, 3, 4, True, [1, 2, 3, 4, 5]]
print(mix)

# Acceder a un elemento de la lista
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento", mix[-1])
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1, ["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1, 2, 100, 90.45, 3, 4, 5]
print("Mayor", max(numbers))
print("Menor", min(numbers))

# eliminar elementos
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)