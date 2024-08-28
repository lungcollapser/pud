import re
import random
import WarriorCharacterSheet
import ThiefCharacterSheet
import WizardCharacterSheet
import royaltyintro
import peasantintro
import commonerintro
import playerui
wiz = WizardCharacterSheet.Wizard
thief = ThiefCharacterSheet.Thief
war = WarriorCharacterSheet.Warrior
play_ui = playerui.PlayerUi


wiz_pattern = re.compile(r"(?i).*wizard$")
thief_pattern = re.compile(r"(?i).*thief$")
war_pattern = re.compile(r"(?i).*warrior$")
yes_pattern = re.compile(r"(?i)^.*(yes)|(yup)|(y)")
no_pattern = re.compile(r"(?i)^.*(no)|(nope)|(n)")

royalty_pattern = re.compile(r"(?i)^.*royalty")
peasant_pattern = re.compile(r"(?i)^.*peasant")
commoner_pattern = re.compile(r"(?i)^.*commoner")

class_list = ["wizard", "warrior", "thief"]
path_list = ["royalty", "peasant", "commoner"]

print("welcome to PUD")
player = input("what is your name?")
print("hmmmm", player, "huh?...very interesting.")
print(class_list)

# Function to ask the player what class they would like to choose based on certain stats.
def choose_class():
    class_choice = input("what is your class?")
    if re.search(wiz_pattern, class_choice):
        print(wiz.wizard_sheet)
        yes_no = input("are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("spell-casters don't last long here.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()
    elif re.search(war_pattern, class_choice):
        print(war.warrior_sheet)
        yes_no = input("are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("another hero with a sword and shield in line for his death.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()
    elif re.search(thief_pattern, class_choice):
        print(thief.thief_sheet)
        yes_no = input("are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("don't go looking into my pockets.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()
    else:
        choose_class()


choose_class()

# Function to ask the player which path they would like to go down.


def which_path():
    print("now decide your path to start on. this will greatly alter your experience, so choose wisely.")
    print(path_list)
    choose_path = input("")
    if re.search(royalty_pattern, choose_path):
        yes_no = input("starting gold = 200. royalty? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("wealth is a shortcut to an early grave. watch your back.")
            are_you_ready_royalty()
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()
    if re.search(peasant_pattern, choose_path):
        yes_no = input("starting gold = 5. peasant? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("you'll be rolling in shit before you know it.")
            are_you_ready_peasant()
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()
    if re.search(commoner_pattern, choose_path):
        yes_no = input("starting gold = 25. commoner? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("ahhh, a perfectly normal and average life. how underwhelming.")
            are_you_ready_commoner()
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()

# List of function paths intros. Need to fix and find a way to put on separate file at some point.


def are_you_ready_peasant():
    yes_no = input("are you ready to begin? type yes or no.")
    if re.search(yes_pattern, yes_no):
        peasantintro.peasant_intro()
    elif re.search(no_pattern, yes_no):
        yes_no = input("would you like to change your class?")
        if re.search(yes_pattern, yes_no):
            choose_class()
            are_you_ready_peasant()
        if re.search(no_pattern, yes_no):
            yes_no = input("would you like to change your path?")
            if re.search(yes_pattern, yes_no):
                which_path()
            elif re.search(no_pattern, yes_no):
                are_you_ready_peasant()


def are_you_ready_commoner():
    yes_no = input("are you ready to begin? type yes or no.")
    if re.search(yes_pattern, yes_no):
        commonerintro.commoner_intro()
    elif re.search(no_pattern, yes_no):
        yes_no = input("would you like to change your class?")
        if re.search(yes_pattern, yes_no):
            choose_class()
            are_you_ready_commoner()
        if re.search(no_pattern, yes_no):
            yes_no = input("would you like to change your path?")
            if re.search(yes_pattern, yes_no):
                which_path()
            elif re.search(no_pattern, yes_no):
                are_you_ready_commoner()


def are_you_ready_royalty():
    yes_no = input("are you ready to begin? type yes or no.")
    if re.search(yes_pattern, yes_no):
        royaltyintro.royalty_intro()
    elif re.search(no_pattern, yes_no):
        yes_no = input("would you like to change your class?")
        if re.search(yes_pattern, yes_no):
            choose_class()
            are_you_ready_royalty()
        if re.search(no_pattern, yes_no):
            yes_no = input("would you like to change your path?")
            if re.search(yes_pattern, yes_no):
                which_path()
            elif re.search(no_pattern, yes_no):
                are_you_ready_royalty()


which_path()

print(play_ui.player_ui)
action = input("what would you like to do?")



