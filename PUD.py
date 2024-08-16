import chooseClass

class_list = ["Wizard", "Warrior", "Thief"]
wiz_stats = {"Strength": 10, "Dexterity": 14, "Constitution": 12, "Intelligence": 20, "Wisdom": 16, "Charisma": 18}
thief_stats = {"Strength": 10, "Dexterity": 20, "Constitution": 14, "Intelligence": 12, "Wisdom": 16, "Charisma": 18}
warrior_stats = {"Strength": 20, "Dexterity": 16, "Constitution": 18, "Intelligence": 10, "Wisdom": 12, "Charisma": 14}
wiz_name = "Wizard"
thief_name = "Thief"
war_name = "Warrior"
yes_no = ""


print("Welcome to PUD")
player = input("What is your name?")
print("...Very interesting.")
print(class_list)
class_choice = input("What is your class?")


while class_choice:
    if class_choice == wiz_name:
        print(wiz_stats)
        yes_no = input("A wizard? Are you sure? Type Y or N.")
        if yes_no == "Y":
            print("Spell-casters do not last very long here")
        elif yes_no == "N":
            print(class_list)
            print("Type in your class.")
        break
    elif class_choice == war_name:
        print(warrior_stats)
        yes_no = input("A warrior? Are you sure? Type Y or N.")
        if yes_no == "Y":
            print("Brute strength suits your demeanor")
        elif yes_no == "N":
            print(class_list)
            print("Type in your class.")
        break
    elif class_choice == thief_name:
        print(thief_stats)
        yes_no = input("A thief? Are you sure? Type Y or N.")
        if yes_no == "Y":
            print("Hmmm.. Not all that surprising.")
        elif yes_no == "N":
            print(class_list)
            print("Type in your class.")
        break
    else:
        class_choice = input("Please type in one of the class names.")
        continue

yes_no: str = input("All set? Type Y to start your adventure.")

yes_no: str = input("You awake in a daze. The ceiling fan loudly swirling around your room. 'I am going to be late again."
                    "letting Roman pressure me into excessive drinking?' You get out of your bed and look around your room."
                    "It's not too terribly messy, but you could clean up. Your eyes fixate on the floor. What would you like"
                    "to do?")




