try:
    divisor = int(input("Ingrese un número: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: División por cero o valor no numérico")
    print("Ha ocurrido un error:", e)
except ValueError as e:
    print("Error: Debes introducir un número válido")
    print("Ha ocurrido un error:", e)