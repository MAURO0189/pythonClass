# Leer un archivo linea por linea
# with open('caperucita.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# Leer un archivo completo
# with open('caperucita.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)

# Agregar texto a un archivo
# with open('caperucita.txt', 'a') as file:
#     file.write('\n\nBy:ChatGPT')

# Sobreescribir un archivo
with open('caperucita.txt', 'w') as file:
    file.write('Había una vez una niña llamada Caperucita Roja.\n')
    file.write('Vivía en un pueblo en medio del bosque.\n')
    file.write('Un día su madre le pidió que llevara una cesta con comida a su abuela.\n')
    file.write('En el camino, Caperucita se encontró con un lobo feroz.\n')
    file.write('El lobo llegó primero a la casa de la abuela y se la comió.\n')
    file.write('Caperucita llegó y descubrió al lobo.\n')
    file.write('Un cazador pasaba por ahí y mató al lobo.\n')
    file.write('Caperucita y su abuela vivieron felices para siempre.\n')