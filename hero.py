import random

class Hero:
    def __init__(self, name, starting_health=100):
        """Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer 
        """
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        winner = random.choice([self, opponent])
        print(f"The winner is {winner.name}!")

if __name__ == "__main__":
   hero1 = Hero("Wonder Woman", 300)
   hero2 = Hero("Dumbledore", 250)

   hero1.fight(hero2)