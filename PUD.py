import re
import random
import WarriorCharacterSheet
import ThiefCharacterSheet
import WizardCharacterSheet
wiz = WizardCharacterSheet.Wizard
thief = ThiefCharacterSheet.Thief
war = WarriorCharacterSheet.Warrior

class_list = ["Wizard", "Warrior", "Thief"]
wiz_name = "Wizard"
thief_name = "Thief"
war_name = "Warrior"


print("welcome to PUD")
player = input("what is your name?")
print("hmmmm", player, "huh?...very interesting.")
print(class_list)


def choose_class():
    class_choice = input("what is your class?")
    if class_choice == wiz_name:
        print(wiz.wizard_sheet)
        yes_no = input("are you sure? type Y or N")
        if yes_no == "Y":
            print("spell-casters don't last long here.")
        if yes_no == "N":
            choose_class()
        else:
            choose_class()
    elif class_choice == war_name:
        print(war.warrior_sheet)
        yes_no2 = input("are you sure? type Y or N")
        if yes_no2 == "Y":
            print("brute strength suits you.")
        elif yes_no2 == "N":
            choose_class()
        else:
            choose_class()
    elif class_choice == thief_name:
        print(thief.thief_sheet)
        yes_no3 = input("are you sure? type Y or N")
        if yes_no3 == "Y":
            print("don't go looking into my pockets.")
        if yes_no3 == "N":
            choose_class()
        else:
            choose_class()

choose_class()
yes_no = input("are you ready to begin?")