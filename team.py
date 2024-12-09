import random

class Team:
    def __init__(self, name):
        '''Initialize your team with its team name and an empty list of heroes.'''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add a Hero object to the team's list of heroes.'''
        self.heroes.append(hero)

    def view_all_heroes(self):
        '''Print out the names of all heroes in the team.'''
        if not self.heroes:
            print(f"Team {self.name} has no heroes.")
        else:
            print(f"Heroes in team {self.name}:")
            for hero in self.heroes:
                print(f"- {hero.name}")

    def remove_hero(self, name):
        '''Remove a hero from the team by name.
        
        Args:
            name (str): The name of the hero to remove.
        
        Returns:
            int: 0 if the hero is not found, 1 if the hero is successfully removed.
        '''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 1
        return 0
    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths if hero.deaths else hero.kills
        print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''Battle each team against each other.'''
        while self.heroes and other_team.heroes:
            print(f"Heroes in {self.name}: {[hero.name for hero in self.heroes]}")
            print(f"Heroes in {other_team.name}: {[hero.name for hero in other_team.heroes]}")

            if not self.heroes or not other_team.heroes:
                break

            # Randomly select an attacker and a defender
            attacker = random.choice(self.heroes)
            defender = random.choice(other_team.heroes)

            print(f"{attacker.name} is battling {defender.name}!")

            # Let the heroes fight
            attacker.fight(defender)

            # Remove defeated heroes
            if not defender.is_alive():
                print(f"{defender.name} has been defeated!")
                other_team.heroes.remove(defender)

            if not attacker.is_alive():
                print(f"{attacker.name} has been defeated!")
                self.heroes.remove(attacker)

        # Announce the winning team
        if self.heroes:
            print(f"Team {self.name} wins the battle!")
        elif other_team.heroes:
            print(f"Team {other_team.name} wins the battle!")
        else:
            print("Both teams are defeated!")


if __name__ == '__main__':
    from hero import Hero
    from ability import Ability
    from armor import Armor
    from team import Team

    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)

    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)

    print(f"Team Two Initial Health: {team_two.heroes[0].current_health}")
    team_one.attack(team_two)
    print(f"Team Two Final Health: {team_two.heroes[0].current_health if team_two.heroes else 'Defeated'}")

    # #create team
    # team_justice = Team("Justice League")
    # team_wizards = Team("The Order of The Phenoix")

    # team_justice.add_hero(Hero("Superman", 500))
    # team_justice.add_hero(Hero("Wonder Woman", 400))
    # team_wizards.add_hero(Hero("Dumbledore", 400))
    # team_wizards.add_hero(Hero("Harry Potter", 500))

    # # Let the battle begin
    # print("\nLet the battle begin!")
    # team_justice.attack(team_wizards)

    # # Display final teams
    # print("\nFinal Justice League:")
    # team_justice.view_all_heroes()

    # print("\nFinal Order of the Phoenix:")
    # team_wizards.view_all_heroes()
