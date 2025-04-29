import statistics
import csv

# Leer los datos de ventas desde el archivo CSV
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(f"Monthly Sales Data:", monthly_sales)        

# Calcular la media
mean_sales = statistics.mean(sales)
print(f"La media es:", mean_sales)

# Calcular la mediana
median_sales = statistics.median(sales)
print(f"La mediana es:", median_sales)

# Calcular la moda
mode_sales = statistics.mode(sales)
print(f"La moda es:", mode_sales)


# Calcular la desviación estándar
std_sales = statistics.stdev(sales)
print(f"La desviación estándar es:", std_sales)

# Calcular la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es:", variance_sales)

max_sales = max(sales)
min_sales = min(sales)
print(f"Máxima venta mensual:", max_sales)
print(f"Mínima venta mensual:", min_sales)

# Calcular el rango
range_sales = max_sales - min_sales
print(f"Rango de ventas:", range_sales)