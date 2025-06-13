# class Animal:
#     def __init__(self):
#         print("This is the animal class calling .....")
    
#     def eat(self):
#         print("Animal is eating ......")

# class Cat(Animal):
#     def sound(self):
#         print("Meowwww.......")

# class Dog(Animal):
#     def sound(self):
#         print("Bowww.......")

# cat = Cat()
# cat.eat()
# cat.sound()

# dog = Dog()
# dog.eat()
# dog.sound()



################# Method Overriding ###################

# class Animal:
#     def __init__(self):
#         print("Animal Parent class default constructor....")
#     def sound(self):
#         print("Animal sound !!!")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# cat = Cat()
# cat.sound()

################# Single Inheritance ################

# from datetime import datetime

# class BankAccount:
#     def __init__(self,account_number,holder_name,balance=0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
#         self.transactions = []
    
#     def get_balance(self):
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount <=self.balance:
#             self.balance -= amount
#             self._log_transaction("Withdrawal", amount)
#         else:
#             print("Insufficient funds")

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             self._log_transaction("Deposit", amount)
#         else:
#             print("Invalid deposit amount")

#     def _log_transaction(self,txn_type,amount):
#         time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.transactions.append(f"{time} - {txn_type} of Rs.{amount}")
    
#     def show_transactions(self):
#         print(f"Transaction History for {self.holder_name}:")
#         for txn in self.transactions:
#             print(txn)

# class SavingAccount(BankAccount):
#     def __init__(self,account_number, holder_name, balance=0, interest_rate=4.0):
#         super().__init__(account_number,holder_name,balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.balance * self.interest_rate /100
#         self.balance += interest
#         self._log_transaction("Interest",interest)
#         print(f"Interest Rs.{interest:.2f} added to your balance.")


# acc = SavingAccount("SB1245","Shantanu",1000)
# acc.deposit(500)
# acc.withdraw(500)
# acc.add_interest()
# acc.show_transactions()
# print(f"Current Balance : Rs:{acc.get_balance()}")
# acc.add_interest()
# print(f"Current Balance : Rs:{acc.get_balance()}")
    
