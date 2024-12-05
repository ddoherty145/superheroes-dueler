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
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

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
        total_block = 0
        for armor in self.armors:
            total_block == armor.block()
        return total_block

    def take_damage(self, damage):
        ''' Updates self.current_health to reflect the daage minus the defense.
        '''
        defense = self.defend()
        effective_damage = max(0, damage - defense)
        self.current_health -= effective_damage
        if self.current_health < 0:
            self.current_health = 0

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print("draw")
            return
        while self.is_alive() and opponent.is_alive():
            damage_to_opponent = self.attack()
            opponent.take_damage(damage_to_opponent)

            if not opponent.is_alive():
                print(f"{self.name} won!")
                return
            
            damage_to_hero = opponent.attack()
            self.take_damage(damage_to_hero)

            if not self.is_alive():
                print(f"{opponent.name} won!")
                return

if __name__ == "__main__":
   ability = Ability("Great Debugging", 50)
   another_ability = Ability("Lasso of Truth", 90)
   armor = Armor("Shield of Athena", 40)

   hero1 = Hero("Wonder Woman", 300)
   hero1.add_ability(ability)
   hero1.add_ability(another_ability)
   hero1.add_armor(armor)

   hero2 = Hero("Dumbledore", 250)
   wizard_powers = Ability("Exspelliomus", 50)
   wizard_powers2 = Ability("Priteago", 110)
   wiz_armor = Armor("Protecto", 50)


   hero2.add_ability(wizard_powers)
   hero2.add_ability(wizard_powers2)
   hero2.add_armor(wiz_armor)

   print(f"Heor attack damage: {hero1.attack()}")
   print(f"Hero defence: {hero1.defend()}")

   print(f"Hero 2 attack damage: {hero2.attack()}")

   hero1.fight(hero2)
