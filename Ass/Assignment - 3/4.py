class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  
        self.__balance = initial_balance       
    
 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. Current balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
 
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew Rs.{amount}. Current balance: Rs.{self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
  
    def get_balance(self):
        return self.__balance


account = BankAccount(account_number="123456789", initial_balance=500)

account.deposit(200)  
account.withdraw(100) 
account.withdraw(700)  


print(f"Final balance: Rs.{account.get_balance()}")


