def divide(a: int, b: int) -> float:
  #validar ambos parametros 
  if not isinstance(a, int) or not isinstance(b, int):
    #print('Error ambos parametros deben de ser enteros o flotantes')
    raise TypeError('Error ambos parametros deben de ser enteros o flotantes')
    return None
  #verificar el divisor no se igual a cero
  if b == 0:
    #print('Error el divisor no puede ser cero')
    raise ValueError('el divisor no puede ser cero')
    return None 

  return a/b

#Ejemplo de uso 
# try:
#   res = divide(10,'2')
#   print(res)
# except TypeError as e:
#   print(f'Error: {e}')

try: 
  res = divide(10,2)
  print(res)
except (ValueError, TypeError) as e:
  print(f'Error: {e}')  