def start_adventure():

    living_situation = input("Do you live in a house or an apartment? 
(Enter 'house' or 'apartment'): ").lower()
    
    if living_situation == 'apartment':
        print("Thank you for the input to your demise and to begin you 
awake to screams and a loud car explosion outside you're apartment.")
        print("Choose your path wisely...\n")
        print("1. Stay inside and barricade the doors.")
        print("2. Try to find the local authorities/police station.")
        print("3. Gather any supplies in your apartment and head to the 
countryside.")
        print("4. Try to contact/find your family and friends.")
        print("5. You get a notification on your phone about a military 
facility near St. Paul. Would you want to head towards the military 
base?")
        print("6. Try to find a boat and escape by driving through the 
Mississippi River.")
        print("7. Search for other survivors. Bigger groups increase your 
survival rate to not get your brains eaten lol.")
        print("8. Drive in your car to find a safe haven until things calm 
down.")
        print("9. Head to the roof and signal for help.")
    else:
        print("Got it! To begin you awake to the smell of smoke and hear 
the neighbors screaming and a horfic bark like a dog but to you it sounds 
more human like and immediatly understand its the apocalypse.")
        print("Choose your path wisely...\n")
        print("1. Stay inside and barricade the doors.")
        print("2. Try to find the local authorities/police station.")
        print("3. Gather any supplies in your home and head to the 
countryside.")
        print("4. Try to contact/find your family and friends.")
        print("5. You get a notification on your phone about a military 
facility near St. Paul. Would you want to head towards the military 
base?")
        print("6. Try to find a boat and escape by driving through the 
Mississippi River.")
        print("7. Search for other survivors. Bigger groups increase your 
survival rate to not get your brains eaten lol.")
        print("8. Hide in your basement.")
        print("9. Wait it out and climb to your roof and signal for 
help.")

    choice = get_user_choice(9)

    if choice == 1:
        stay_inside()
    elif choice == 2:
        police_station()
    elif choice == 3:
        countryside()
    elif choice == 4:
        find_family()
    elif choice == 5:
        military_base()
    elif choice == 6:
        escape_by_sea()
    elif choice == 7:
        find_survivors()
    elif choice == 8:
        if living_situation == 'apartment':  # For apartment choice, we 
drive in the car
            drive_to_safety()
        else:  # For house choice, the player hides in the basement
            hide_in_basement()
    elif choice == 9:
        signal_for_help()

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input(f"Enter your choice (1-{max_choice}): "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a valid option (1-{max_choice}):")
        except ValueError:
            print(f"Please enter a valid option (1-{max_choice}):")

def stay_inside():
    print("You decide to stay inside and barricade the doors.")
    print("After a few days, the food runs out and the zombies break 
through. You didn't survive.")
    end_adventure()

def police_station():
    print("You run to the nearest police station.")
    print("The police station is overrun with zombies. You didn't 
survive.")
    end_adventure()

def countryside():
    print("You gather supplies and head to the countryside.")
    print("You find a small group of survivors and manage to stay safe. 
You join their colony and rebuild a new life. You survived!")
    end_adventure()

def find_family():
    print("You try to find your family and friends.")
    print("You find them, but they have turned into zombies. You didn't 
survive.")
    end_adventure()

def military_base():
    print("You head to the nearest military base.")
    print("The military base is overrun, but you manage to find a group of 
survivors. Together, you form a colony and rebuild. You survived!")
    end_adventure()

def escape_by_sea():
    print("You try to find a boat and escape by sea.")
    print("You find a boat, but you're stranded on a deserted island. The 
supplies run out, and you didn't survive.")
    end_adventure()

def find_survivors():
    print("You search for other survivors.")
    print("You find a group of survivors. Together, you escape the 
zombies, but you're forced to make a heroic sacrifice to help them reach 
the government facility.")
    heroic_sacrifice()

def hide_in_basement():
    print("You hide in the basement.")
    print("The basement is dark and you run out of supplies. You didn't 
survive.")
    end_adventure()

def drive_to_safety():
    print("You drive in your car, trying to find a safe haven.")
    print("The roads are chaotic, and after a few days of driving, you 
find a remote town that has set up a safe zone.")
    print("You survive and find a community of survivors. You've managed 
to stay safe for now. You survived!")
    end_adventure()

def signal_for_help():
    print("You head to the roof and signal for help.")
    print("A helicopter sees your signal and rescues you. You survived!")
    end_adventure()

def heroic_sacrifice():
    print("You help the group of survivors reach a government facility, 
but the zombies catch up to you. You make the ultimate sacrifice, ensuring 
the others are saved.")
    print("Your sacrifice is heroic, and the survivors are rescued. You 
didn't survive, but you saved them all.")
    end_adventure()

def end_adventure():
    print("The adventure has ended. Would you like to play again? 
(yes/no)")
    play_again = input().lower()

    if play_again == "yes":
        start_adventure()
    else:
        print("Thanks for playing!")

# Start the adventure
start_adventure()
