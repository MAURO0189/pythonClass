import os 

# os: Módulo para interactuar con el sistema operativo
cwd = os.getcwd() 
print(f"Directorio de trabajo actual: {cwd}")

# Listar archivos y carpetas en el directorio actual
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"Archivos .txt en el directorio actual: {txt_files}")

# Renombrar un archivo
os.rename('caperucita.txt', 'cuento.txt')
print("Archivo renombrado de 'caperucita.txt' a 'cuento.txt'")

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"Archivos .txt en el directorio actual: {txt_files}")