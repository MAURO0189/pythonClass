import json 

file_path = 'products.json'

new_product = {
    "ID": 31,
    "Nombre": "Iphone 12",
    "Marca": "Apple",
    "Categoría": "Teléfono",
    "Precio": 999.99,
    "Stock": 60,
    "Total_value": 46999.5
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)    

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)