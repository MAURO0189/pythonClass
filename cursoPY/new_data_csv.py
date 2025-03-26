import csv 

new_product = {'Nombre': 'Smartphone', 'Precio': 1000.00, 'Categoría': 'Teléfono'}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)