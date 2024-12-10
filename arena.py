from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):
        name = input("What is the ability name?")
        max_damage = int(input("what is the max damage of the ability?"))
        return Ability(name, max_damage)
    
    def create_weapon(self):
        name = input("What is the weapon name?")
        max_damage = int(input("what is the max damage of the weapon?"))
        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input("What is the armor name?")
        max_block = int(input("what is the max block of the armor?"))
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done addin items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero
    
    def build_team_one(self):
        self.team_one = Team("Team One")
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for _ in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        self.team_two = Team("Team Two")
        num_of_team_members = int(input("How many members would you like on Team Two?\n"))
        for _ in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\nTeam One statistics:")
        self.team_one.stats()
        print("\nTeam Two statistics:")
        self.team_two.stats()

        team_one_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_one_deaths = sum(hero.deaths for hero in self.team_one.heroes)
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(f"Team One average K/D: {team_one_kills / team_one_deaths:.2f}")

        team_two_kills = sum(hero.kills for hero in self.team_two.heroes)
        team_two_deaths = sum(hero.deaths for hero in self.team_two.heroes)
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(f"Team Two average K/D: {team_two_kills / team_two_deaths:.2f}")

        survivors_one = [hero.name for hero in self.team_one.heroes if hero.is_alive()]
        survivors_two = [hero.name for hero in self.team_two.heroes if hero.is_alive()]

        print(f"Surviving heroes from Team One: {', '.join(survivors_one) if survivors_one else 'None'}")
        print(f"Surviving heroes from Team Two: {', '.join(survivors_two) if survivors_two else 'None'}")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()