# Creando un iterador para los numeros impares

#Limit 
limit = 10

odd_itter = iter(range(1,limit+1,2))

# Usar el iterador
for num in odd_itter:
    print(num)