# numbers = [1,2,3,4,5,6]
# for i in numbers:
#     print("Aquí i es igual a:",i + 1)
    
# for i in range(10):
#     print("Aquí i es igual a:",i)


fruits = ["apple","banana","cherry","orange","kiwi","melon","mango"]
for fruit in fruits:
    print(fruit)
    if fruit =="orange":
        print("Naranja encontrada")    

x = 0 
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1     


numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print("Aquí i es igual a:",i)