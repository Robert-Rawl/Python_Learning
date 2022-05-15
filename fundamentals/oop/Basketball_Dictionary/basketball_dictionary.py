#Define player class/ change constructor to accept a dictionary as an argument
class Player:
    def __init__(self, information):
        self.name = information["name"]
        self.age = information['age']
        self.position = information['position']
        self.team = information['team']

#Bonus
    @classmethod
    def add_newPlayer(cls, information):
        newPlayers =[]
        for info in information:
            newPlayers.append(cls(info))
        return newPlayers
#Challenge 2

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        'position': 'small forward',
    	"team": "Brooklyn Nets"
}

#Challenge 3



# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print(player_kevin)
print(player_jason)
print(player_kyrie)
# player_jason = ???
print(player_jason.position)
print (player_kyrie.age)
print (player_kevin.team)