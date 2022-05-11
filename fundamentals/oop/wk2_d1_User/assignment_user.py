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


    def enroll_user(self):
        self.is_rewards_member = True
        if self.is_rewards_member != False:
            print("ALREADY A MEMBER!!!!")

    def spend_points(self,amount):
        self.gold_card_points = (self.gold_card_points - amount)
        if self.gold_card_points <= 1:
            print( "You are almost out of money!!")







user_1 = User('Robert', 'Rawl', 'rawl.rob@gmail.com', 40)
user_2 = User('Brandon','Rawl', 'brawl@hotmai.com', 39)
user_3 = User('Chloe', 'Yang', 'cyang@yahoo.com', 31)
user_4 = User('Natalie', 'Rawl', 'nrd@hotmail.com', 33)

user_1.display_info()
user_3.display_info()
user_1.enroll_user()
user_2.enroll_user()
user_1.spend_points(50)
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_1.enroll_user()
user_3.spend_points(199)
