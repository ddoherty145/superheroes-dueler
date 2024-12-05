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


if __name__ == '__main__':
    from hero import Hero

    #create team
    team_justice = Team("Justice League")
    team_wizards = Team("The Order of The Phenoix")

    hero1 = Hero("Superman", 500)
    hero2 = Hero("Batman", 300)
    hero3 = Hero("Wonder Woman", 400)

    wiz1 = Hero("Dumbledore", 400)
    wiz2 = Hero("Harry Potter", 500)
    wiz3 = Hero("Ginny Weasley", 300)

    team_justice.add_hero(hero1)
    team_justice.add_hero(hero2)
    team_justice.add_hero(hero3)

    team_wizards.add_hero(wiz1)
    team_wizards.add_hero(wiz2)
    team_wizards.add_hero(wiz3)

    print("\nJustice League:")
    team_justice.view_all_heroes()

    print("\nThe Order of the Phenoix")
    team_wizards.view_all_heroes()
    
    result_jl = team_justice.remove_hero("Batman")
    result_wz = team_wizards.remove_hero("Ginny Weasley")

    print("\nAfter removing heroes:")
    if result_jl == 1:
        print("Batman was removed from the Justice League.")
    else:
        print("Batman not found in the Justice League")

    if result_wz == 1:
        print("Ginny Weasley was removed from The Order of the Phenoix")
    else:
        print("Ginny Weasley not found in The Order of the Phenoix")

    print("\nUpdated Justice League:")
    team_justice.view_all_heroes()

    print("\nUpdated Order of the Phenoix")
    team_wizards.view_all_heroes()