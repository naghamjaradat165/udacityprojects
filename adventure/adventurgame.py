import time
import random

enemies = ["Shade", "Brute", "Crawler", "Mage", "Mech", "Mind"]
weapons = ["Dagger", "Longbow", "Healstaff", "kyeblade"]


def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


def valid_input(prompt, options):
    response = input(prompt).lower()
    while response not in options:
        print_pause("Invalid input. Please try again.")
        response = input(prompt).lower()
    return response


def intro(enemy, weapon):
    print_pause("To get started, enter your name:")
    name = input()
    print_pause(f"Hi, {name}!")
    print_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
    )
    print_pause(
        f"Rumor has it that a {enemy} is somewhere around here, "
        "terrifying the nearby village."
    )
    print_pause(
        f"If you want to be the hero and save the village, "
        f"let's get started, {name}!"
    )
    print_pause("You see two paths ahead of you:")
    print_pause("1. A dark cave to your right.")
    print_pause("2. A house in front of you.")
    print_pause("you hold your trusty (but not very effective) Dagger.")


def cave(weapon):
    print_pause("You cautiously enter the dark cave.")
    if weapon == "Dagger":
        print_pause("Your eyes adjust to the dim light,"
                    "revealing a glint of metal.")
        print_pause("It’s a Longbow! You swap it for your dagger.")
        weapon = "Longbow"
    elif weapon == "kyeblade":
        print_pause("It’s a kyeblade! You swap it,"
                    " but it might not be effective.")
        weapon = "kyeblade"
    else:
        print_pause("Is that just a sun reflection, "
                    " or is it your new winning staff?")
        print_pause("It’s a Healstaff! Swap it right now!"
                    " That's a perfect prize.")
        weapon = "Healstaff"

    print_pause("The cave is empty. You step back into the field.")
    return weapon


def house(enemy, weapon):
    print_pause(f"You move towards the house. The {enemy} might be there!")
    print_pause(f"The door creaks open, revealing the {enemy} staring at you!")
    print_pause(f"You freeze as the {enemy} lunges at you!")
    action = valid_input("Do you (1) fight or (2) "
                         "run back to the field? ", ["1", "2"])
    if action == "1":
        fight(enemy, weapon)
    else:
        print_pause("You run back to the safety of the field.")
    play_again()


def fight(enemy, weapon):
    if weapon == "Dagger":
        print_pause(f"You bravely face the {enemy} with your {weapon}.")
        print_pause("But your dagger is no match for such a powerful foe.")
        print_pause("You have been defeated.")
    elif weapon == "Longbow":
        print_pause(f"You take aim with your {weapon} "
                    "as the {enemy} approaches.")
        if random.choice(["hit", "miss"]) == "hit":
            print_pause(f"Your arrow strikes true,"
                        "and the {enemy} falls! You win!")
        else:
            print_pause("Your arrow misses, and the monster overpowers you.")
            print_pause("You have been defeated.")
    elif weapon == "Healstaff":
        print_pause(f"You wield the mystical {weapon} as the {enemy} attacks.")
        print_pause("The staff heals your wounds,"
                    " and the confused enemy retreats.")
        print_pause("You survive!")
    else:
        print_pause(f"You attempt to fight with your"
                    " {weapon}, but it’s ineffective.")
        print_pause(f"The {enemy} overpowers you. You have been defeated.")
    play_again()


def field(enemy, weapon):
    print_pause("You are in the field, make your choice.")
    path = valid_input("1 or 2?: ", ["1", "2"])
    if path == "2":
        house(enemy, weapon)
    elif path == "1":
        weapon = cave(weapon)
        field(enemy, weapon)


def play_again():
    replay = valid_input("Would you like to play again? (y/n): ", ["y", "n"])
    if replay == "y":
        print_pause("Restarting the game...")
        game()
    else:
        print_pause("Thanks for playing! Goodbye!")
        exit()


def game():
    weapon = random.choice(weapons)
    enemy = enemies[random.randint(0, 5)]
    intro(enemy, weapon)
    field(enemy, weapon)


game()
