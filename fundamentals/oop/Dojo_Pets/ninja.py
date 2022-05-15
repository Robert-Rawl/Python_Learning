


class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

# walk() - walks the ninja's pet invoking the pet play() method
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f'Feeding {self.pet.name} {food}!')
            self.pet.eat()
        else:
            print('You are out of Pet Food!')
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def bathe(self):
        self.pet.noise()
        
# bathe() - cleans the ninja's pet invoking the pet noise() method
class Pet():
    def __init__(self,name,pet_type,tricks,pet_noise):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.pet_noise = pet_noise

    def sleep(self):
        #increase the pets energy by 25
        self.energy += 25
        return self

    def eat(self):
        # increases the pet's energy by 5 and health by 10
        self.energy += 5
        self.health += 10
        return self


    def play(self):
        # increases the pet's helath by 5
        self.health += 5
        return self

    def noise(self):
        #prints out the pet's sound
        print(self.pet_noise)

my_treats = ['bacon', 'cheese', 'carrots', 'peanut butter']
my_pet_food = ['chicken', 'pork', 'turkey', 'beef']

velvet = Pet('Velvet', 'dog', 'dancing', 'Ruff Ruff')

rob = Ninja('Rob', 'Rawl',my_treats,my_pet_food, velvet )

rob.feed()
rob.bathe()
rob.walk()


