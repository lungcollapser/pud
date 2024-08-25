import re
import random
import WarriorCharacterSheet
import ThiefCharacterSheet
import WizardCharacterSheet
import royaltyintro
import peasantintro
import commonerintro
wiz = WizardCharacterSheet.Wizard
thief = ThiefCharacterSheet.Thief
war = WarriorCharacterSheet.Warrior

royalty_intro = royaltyintro.royalty_intro()
peasant_intro = peasantintro.peasant_intro()
commoner_intro = commonerintro.commoner_intro()

wiz_pattern = re.compile(r".*wizard$")
thief_pattern = re.compile(r".*thief$")
war_pattern = re.compile(r".*warrior$")
yes_pattern = re.compile(r"^.*yes")
no_pattern = re.compile(r"^.*no")

royalty_pattern = re.compile(r"^.*royalty")
peasant_pattern = re.compile(r"^.*peasant")
commoner_pattern = re.compile(r"^.*commoner")

class_list = ["wizard", "warrior", "thief"]
path_list = ["royalty", "peasant", "commoner"]

print("welcome to PUD")
player = input("what is your name?")
print("hmmmm", player, "huh?...very interesting.")
print(class_list)


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


def which_path():
    print("now decide your path to start on. this will greatly alter your experience, so choose wisely.")
    print(path_list)
    choose_path = input("")
    if re.search(royalty_pattern, choose_path):
        yes_no = input("royalty? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("wealth is a shortcut to an early grave. watch your back.")
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()
    if re.search(peasant_pattern, choose_path):
        yes_no = input("peasant? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("you'll be rolling in shit before you know it.")
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()
    if re.search(commoner_pattern, choose_path):
        yes_no = input("commoner? are you sure? type yes or no.")
        if re.search(yes_pattern, yes_no):
            print("ahhh, a perfectly normal and average life. how underwhelming.")
        elif re.search(no_pattern, yes_no):
            which_path()
        else:
            which_path()


def are_you_ready():
    yes_no = input("are you ready to begin? type yes or no.")
    if re.search(yes_pattern, yes_no):
        royalty_intro()
    elif re.search(no_pattern, yes_no):
        yes_no = input("would you like to change your class?")
        if re.search(yes_pattern, yes_no):
            choose_class()
            are_you_ready()
        if re.search(no_pattern, yes_no):
            yes_no = input("would you like to change your path?")
            if re.search(yes_pattern, yes_no):
                which_path()
            elif re.search(no_pattern, yes_no):
                are_you_ready()


which_path()
are_you_ready()
