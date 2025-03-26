class BankAccount: 
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'{amount} deposited. New balance is {self.balance}')
        else:
            print('Account is not active, cannot deposit') 

    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f'{amount} withdrawn. New balance is {self.balance}')
            else:
                print('Insufficient funds')
        else:
            print('Account is not active, cannot withdraw')

    def close_account(self):
        self.is_active = False
        print('Account closed')

    def activate_account(self):
            self.is_active = True
            print('Account activated')


account1 = BankAccount('David', 1000)
account2 = BankAccount('Carla', 500)

# llamado a los metodos

account1.deposit(500)
account2.deposit(1000)
account1.close_account()
account1.deposit(500)
account1.activate_account()
account1.deposit(500)

        