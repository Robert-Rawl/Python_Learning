class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        #Create a Bank Account class with the attributes interest rate abnd balance
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
        BankAccount.accounts.append(self)


    def deposit(self, amount):
        #Add a deposit method to the BankAccount class
        self.balance += amount
        return self



    def withdraw(self, amount):
        # Add a withdraw method to BankAccount class
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insuffiecient Funds: Charging $5')
            self.balance -= 5
        return self



    def display_account_info(self):
        # add a display_account_info method to Bank account class
        return f'{self.balance}'
        


    def yield_interest(self):
        #Adding a yield_interest method to BankAccounts class as long as the account is positive
        if self.balance > 0:
            self.balance =  self.balance + (self.balance * self.int_rate)
        return(self)

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

#Update the User class __init__ method
class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            'checking' : BankAccount(.02,500),
            'savings' : BankAccount(.035, 2000)
        }

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account.display_account_info()}')
        return self

    def transfer_money(self,amount,user):

        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

rob = User('Rob')
#rob.account.deposit(100)
rob.display_user_balance()


