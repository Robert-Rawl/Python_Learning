class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        #Create a Bank Account class with the attributes interest rate abnd balance
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
        #BankAccount.accounts.append(self)


    def deposit(self, amount):
        #Add a deposit method to the BankAccount class
        self.balance += amount
        return(self)



    def withdraw(self, amount):
        # Add a withdraw method to BankAccount class
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insuffiecient Funds: Charging $5')
            self.balance -= 5
        return(self)



    def display_account_info(self):
        # add a display_account_info method to Bank account class
        print(f'Your account balance is: {self.balance}')
        return(self)


    def yield_interest(self):
        #Adding a yield_interest method to BankAccounts class as long as the account is positive
        if self.balance > 0:
            self.balance =  self.balance + (self.balance * self.int_rate)
        return(self)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        


