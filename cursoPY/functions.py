# def greet(name, last_name="No tiene apellido"):
#     print("Hello!", name, last_name)

# greet("Mauro","Yepes")
# greet("Santiago")    


x = 100 

def local_function():
    x = 10 
    print(f"El valor de la variable es {x}")

def show_global():
    print(f"El valor de la variable global es {x}")


#local_function()    
print(x)