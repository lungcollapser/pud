import re
import random
import WarriorCharacterSheet
import ThiefCharacterSheet
import WizardCharacterSheet
wiz = WizardCharacterSheet.Wizard
thief = ThiefCharacterSheet.Thief
war = WarriorCharacterSheet.Warrior

wiz_pattern = re.compile(r".*Wizard$")
thief_pattern = re.compile(r".*Thief$")
war_pattern = re.compile(r".*Warrior$")
yes_pattern = re.compile(r"^.*yes")
no_pattern = re.compile(r"^.*no")

class_list = ["Wizard", "Warrior", "Thief"]


print("welcome to PUD")
player = input("what is your name?")
print("hmmmm", player, "huh?...very interesting.")
print(class_list)


def choose_class():
    class_choice = input("what is your class?")
    if re.search(wiz_pattern, class_choice):
        print(wiz.wizard_sheet)
        yes_no = input("are you sure? yes or no?")
        if re.search(yes_pattern, yes_no):
            print("spell-casters don't last long here.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()
    elif re.search(war_pattern, class_choice):
        print(war.warrior_sheet)
        yes_no = input("are you sure? yes or no?")
        if re.search(yes_pattern, yes_no):
            print("brute strength suits you.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()
    elif re.search(thief_pattern, class_choice):
        print(thief.thief_sheet)
        yes_no = input("are you sure? yes or no?")
        if re.search(yes_pattern, yes_no):
            print("don't go looking into my pockets.")
        elif re.search(no_pattern, yes_no):
            choose_class()
        else:
            choose_class()


choose_class()


def beginning():
    print("yoyoyo bitch")


def are_you_ready():
    yes_no = input("are you ready to begin? yes or no?.")
    if re.search(yes_pattern, yes_no):
        beginning()
    elif re.search(no_pattern, yes_no):
        yes_no = input("Would you like to change your class?")
        if re.search(yes_pattern, yes_no):
            choose_class()
        if re.search(no_pattern, yes_no):
            are_you_ready()


are_you_ready()
