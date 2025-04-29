import json 

with open('products.json', mode='r') as file:
    products = json.load(file)

    
for product in products:
    #print(product)
    print("Product: ", {product['Nombre']},"Price: ", {product['Precio']},"Stock: ", {product['Stock']})