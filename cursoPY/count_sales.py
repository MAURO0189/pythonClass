from collections import Counter


def count_sales(products: list[str]) -> Counter:
    return Counter (products)

sales = ['laptop','smarthphone','smarthphone','laptop','tablet']
result = count_sales(sales)
print(result)