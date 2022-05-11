class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 200

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f'Gold Card Points: {self.gold_card_points}')
        return self


    def enroll_user(self):
        self.is_rewards_member = True
        if self.is_rewards_member != False:
            print("ALREADY A MEMBER!!!!")
            return self

    def spend_points(self,amount):
        self.gold_card_points = (self.gold_card_points - amount)
        if self.gold_card_points <= 1:
            print( "You are almost out of money!!")
            return self







user_1 = User('Robert', 'Rawl', 'rawl.rob@gmail.com', 40)
user_2 = User('Brandon','Rawl', 'brawl@hotmai.com', 39)
user_3 = User('Chloe', 'Yang', 'cyang@yahoo.com', 31)
user_4 = User('Natalie', 'Rawl', 'nrd@hotmail.com', 33)


user_1.display_info().enroll_user().spend_points(50).display_info()
user_2.enroll_user().spend_points(80).display_info()




