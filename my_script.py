"""
Class: CSO 1035-01
Author: Tommy Xiong
Date: 12-24-24
Assignment: Python Project Assignment
"""
class PlayerStats:
    def __init__(self):
        self.reputation = 0
        self.health = 100
        self.stamina = 100
        self.morale = 100

    def change_reputation(self, value):
        self.reputation += value
        print(f"Reputation: {self.reputation}")

    def change_health(self, value):
        self.health += value
        print(f"Health: {self.health}")

    def change_stamina(self, value):
        self.stamina += value
        print(f"Stamina: {self.stamina}")

    def change_morale(self, value):
        self.morale += value
        print(f"Morale: {self.morale}")


class NPC:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.trust = 50  # Initial trust level

    def change_trust(self, value):
        self.trust += value
        print(f"{self.name}'s trust: {self.trust}")


class Game:
    def __init__(self):
        self.player_stats = PlayerStats()
        self.npcs = {
            "Chris": NPC("Chris", "Military Comrade"),
            "Sarah": NPC("Sarah", "Medic"),
            "Hobo": NPC("Hobo", "Survivor"),
            "Student": NPC("Student", "Survivor"),
            "Scientist": NPC("Scientist", "Researcher")
        }

    def start_game(self):
        print("Welcome to my simulation called 'FrostBite Minnesota Zombies'.")
        print("Your objective is to survive in a zombie apocalypse and make choices that affect your reputation and ending.")
        print("Thomas, a National Guard reserve soldier, was deployed to help quell a local riot happening in Minneapolis in the midst of winter.")
        print("As he sits in the shotgun seat of the armored car, he glances at his clock, wondering if he will make it home to his family.")
        print("His teammate Chris slaps him on the shoulder and says, 'You're good. We're five minutes away from the location.'")
        print("Sarah, the team's medic, grumbles, 'It's freezing out here. Why do people have to riot at this time? Aren't they cold—or afraid of frostbite?'")
        print("Your team was deployed to stop some rioting and looting in Minneapolis. When they arrive near a Best Buy, you see the rioters running.")
        print("You feel something is off, and your captain orders them to stop moving or face non-lethal weapons.")
        print("But then you notice the rioters are not just ignoring the orders—they're running straight toward your team.")
        print("Upon closer inspection, you spot a man in a bloodstained blue jacket who pounces on a woman, tearing her to shreds.")
        print("It becomes clear: these are zombies. You report the situation to your captain, who pulls out his binoculars and says, 'Oh my God!'")
        print("He orders you and your team to help those civilians and the situation spirals from there...")

        self.moral_choices()
        self.exploration_choices()
        self.combat_choices()
        self.npc_interaction()
        self.critical_decision()
        self.scavenging_choices()
        self.check_ending()

    def moral_choices(self):
        print("\nYou come across a group of survivors, some are injured, others seem fine.")
        print("Do you:")
        print("1. Help the injured and share your supplies.")
        print("2. Take supplies and leave them behind.")
        print("3. Ignore them and keep moving.")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You helped the survivors and shared your supplies. Your reputation improves.")
            self.player_stats.change_reputation(10)
            self.player_stats.change_morale(10)
        elif choice == "2":
            print("You took the supplies and left the survivors behind. Your reputation worsens.")
            self.player_stats.change_reputation(-20)
            self.player_stats.change_morale(-10)
        elif choice == "3":
            print("You ignored the survivors and kept moving. No change in reputation.")
        else:
            print("Invalid choice. You did nothing.")

    def exploration_choices(self):
        print("\nYou're at a crossroads: One road leads to an abandoned hospital, the other to a dense forest.")
        print("Do you:")
        print("1. Go to the abandoned hospital.")
        print("2. Head towards the dense forest.")
        print("3. Stay where you are and fortify your current position.")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You head to the abandoned hospital. There may be supplies, but it's dangerous.")
            self.visit_location("Hospital")
        elif choice == "2":
            print("You head into the forest. You may find useful resources, but you could encounter danger.")
            self.visit_location("Forest")
        elif choice == "3":
            print("You decide to stay where you are and fortify your position, waiting for the next move.")
        else:
            print("Invalid choice. You remain still.")

    def visit_location(self, location):
        print(f"You are visiting the {location}.")
        if location == "Hospital":
            self.scavenging_choices()
        elif location == "Forest":
            self.combat_choices()

    def combat_choices(self):
        print("\nYou're surrounded by zombies. What do you do?")
        print("1. Fight them head-on.")
        print("2. Use a flare to distract them and escape.")
        print("3. Try to hide and wait for them to pass.")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You fight the zombies head-on. It's risky, but you manage to kill a few.")
            self.player_stats.change_health(-10)
        elif choice == "2":
            print("You use a flare to distract the zombies. It works, and you manage to escape.")
            self.player_stats.change_stamina(-10)
        elif choice == "3":
            print("You try to hide. It's tense, but the zombies pass by.")
            self.player_stats.change_stamina(-5)
        else:
            print("Invalid choice. The zombies close in!")

    def npc_interaction(self):
        print("\nYou approach Chris, your military comrade, who looks worried.")
        print("Do you:")
        print("1. Reassure him and offer support.")
        print("2. Tell him to stop worrying and focus on the mission.")
        print("3. Ignore him and keep moving.")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You reassure Chris, and he seems more confident. Your relationship improves.")
            self.npcs["Chris"].trust += 10
        elif choice == "2":
            print("You tell Chris to stop worrying. He doesn't seem happy with you.")
            self.npcs["Chris"].trust -= 5
        elif choice == "3":
            print("You ignore Chris, leaving him worried and uneasy.")
            self.npcs["Chris"].trust -= 10
        else:
            print("Invalid choice. Chris remains uncertain.")

    def critical_decision(self):
        print("\nA survivor is trapped under rubble. You're with your group, and time is running out.")
        print("Do you:")
        print("1. Attempt to save the survivor, risking your own safety.")
        print("2. Leave the survivor behind and keep moving for your own safety.")
        print("3. Try to negotiate with the survivor and persuade them to escape on their own.")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You risk your safety to save the survivor. You succeed, but you're injured.")
            self.player_stats.change_health(-10)
            self.player_stats.change_morale(10)
        elif choice == "2":
            print("You leave the survivor behind. The group is upset, and your morale drops.")
            self.player_stats.change_morale(-20)
        elif choice == "3":
            print("You try to convince the survivor to escape alone. They make it, but you're left behind.")
            self.player_stats.change_health(-5)
        else:
            print("Invalid choice. The survivor is lost.")

    def scavenging_choices(self):
        print("\nYou come across a locked storage container. It could hold important supplies.")
        print("Do you:")
        print("1. Break the lock and take whatever is inside.")
        print("2. Leave the container alone. It might attract unwanted attention.")
        print("3. Try to pick the lock quietly.")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You break the lock, and the supplies are useful, but the noise attracts zombies.")
            self.combat_choices()
        elif choice == "2":
            print("You leave the container alone. No zombies are attracted, but you miss out on supplies.")
        elif choice == "3":
            print("You quietly pick the lock and manage to access the supplies without alerting zombies.")
        else:
            print("Invalid choice. You waste time.")

    def check_ending(self):
        if self.player_stats.reputation > 50:
            print("\nYou've earned the good ending: United We Stand.")
        elif self.player_stats.reputation < -50:
            print("\nYou've earned the bad ending: Alone and Betrayed.")
        else:
            print("\nYou've earned the neutral ending: Survival is a Struggle.")


if __name__ == "__main__":
    game = Game()
    game.start_game()


