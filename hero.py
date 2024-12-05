import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

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

    # def add_heroes(self, hero):
    #     ''' Add Hero Object to self.heroes'''
    #     # TODO: Add the Hero object that is passed in to the list of heroes in
    #     # self.heroes
    #     pass

    # def view_all_heroes(self):
    #     ''' Prints out all heroes to the console.'''
    #     # TODO: Loop over the list of heroes and print their names to the terminal one by one.
    #     pass

    # def remove_hero(self, name):
    #     '''Remove hero from heroes list.
    #     If hero isn't found return 0.
    #     '''
    #     foundHero = False

    #     for hero in self.heroes:
    #         if hero.name == name:
    #             self.heroes.remove(hero)
    #             foundHero = True
    #     if not foundHero:
    #         return 0

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
            total_block += armor.block()
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
            print("Draw! Neither Hero has any Abilities.")
            return
        
        while self.is_alive() and opponent.is_alive():
            damage_to_opponent = self.attack()
            print(f"{self.name} attacks {opponent.name} for {damage_to_opponent} damage.")
            opponent.take_damage(damage_to_opponent)
            print(f"{opponent.name} has {opponent.current_health} health remaining.")

            if not opponent.is_alive():
                print(f"{self.name} won!")
                return
            
            damage_to_hero = opponent.attack()
            print(f"{opponent.name} attacks {self.name} for {damage_to_hero} damage.")
            self.take_damage(damage_to_hero)
            print(f"{self.name} has {self.current_health} health remaining.")

            if not self.is_alive():
                print(f"{opponent.name} won!")
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


   hero1.fight(hero2)
