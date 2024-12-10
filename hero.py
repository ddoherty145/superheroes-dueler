import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.defeated = False

    def add_ability(self, ability):
        ''' Add ability to abilities list'''
        # we need the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: armor object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block ammount from all armor blocks.
            return: total_block:Int
        '''
        if not self.is_alive():
            return 0
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        ''' Updates self.current_health to reflect the daage minus the defense.
        '''
        defense = self.defend()
        effective_damage = max(0, damage - defense)
        self.current_health -= effective_damage
        if self.current_health <= 0 and not self.defeated:
            self.defeated = True
            self.current_health = 0
            self.deaths += 1

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths
        

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0 and not self.defeated


    def fight(self, opponent):
        ''' Hero fights an opponent. '''
        if not self.abilities and not opponent.abilities:
            print(f"Draw! Neither {self.name} nor {opponent.name} has abilities.")
            return

        while self.is_alive() and opponent.is_alive():
            print(f"{self.name} attacks {opponent.name}")
            opponent.take_damage(self.attack())
            print(f"{opponent.name} health: {opponent.current_health}")

            if not opponent.is_alive():
                print(f"{self.name} defeated {opponent.name}!")
                self.add_kill(1)
                opponent.add_death(1)
                return

            print(f"{opponent.name} attacks {self.name}")
            self.take_damage(opponent.attack())
            print(f"{self.name} health: {self.current_health}")

            if not self.is_alive():
                print(f"{opponent.name} defeated {self.name}!")
                opponent.add_kill(1)
                self.add_death(1)
                return


if __name__ == "__main__":
   ability = Ability("Great Debugging", 50)
   lasso = Weapon("Lasso of Truth", 90)
   armor = Armor("Shield of Athena", 40)

   hero1 = Hero("Wonder Woman", 300)
   hero1.add_ability(ability)
   hero1.add_weapon(lasso)
   hero1.add_armor(armor)

   hero2 = Hero("Dumbledore", 300)
   wand = Weapon("Wand", 50)
   wizard_powers2 = Ability("Priteago", 110)
   wiz_armor = Armor("Protecto", 50)

   hero2.add_weapon(wand)
   hero2.add_ability(wizard_powers2)
   hero2.add_armor(wiz_armor)

   print(f"Hero 1 attack damage: {hero1.attack()}")
   print(f"Hero 1 defence: {hero1.defend()}\n")

   print(f"Hero 2 attack damage: {hero2.attack()}")
   print(f"Hero 2 defense: {hero2.defend()}\n")

   print(f"{hero1.name} - Kills: {hero1.kills}, Deaths: {hero1.deaths}")
   print(f"{hero2.name} - Kills: {hero2.kills}, Deaths: {hero2.deaths}")

   hero1.fight(hero2)
