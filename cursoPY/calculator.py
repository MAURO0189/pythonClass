def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


def calculate():
    while True:
        print('Welcome to the calculator')
        print('select an option')
        print('1. Add')
        print('2. Substract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')

        option = input('Select an option: (1,2,3,4,5):')
        
        if option == '5':
            print('Exiting...')
            break

        if option in ['1','2','3','4']:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))

            if option == '1':
                print('Result:', add(num1, num2))
            elif option == '2':
                print('Result:', substract(num1, num2))
            elif option == '3':
                print('Result:', multiply(num1, num2))
            elif option == '4':
                print('Result:', divide(num1, num2))
        else:
            print('Invalid option, try again')

calculate()                