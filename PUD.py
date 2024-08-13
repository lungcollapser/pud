class_list = ["Wizard", "Warrior", "Thief"]
order_of_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
wiz_name = "Wizard"
thief_name = "Thief"
war_name = "Warrior"

player = ""
class_choice = ""
yes = "Y", "n"
no = "N", "n"

wizard_stats = [10, 14, 12, 20, 16, 18]
thief_stats = [10, 20, 14, 12, 16, 18]
war_stats = [20, 16, 18, 10, 12, 14]

print("Welcome to PUD")
player = input("What is your name?")
print("...Very interesting.")
print(class_list)
class_choice = input("What is your class?")

while class_choice:
    if class_choice == wiz_name:
        print("A wizard? Are you sure?")
        if yes = input("Y") or yes = input("y"):
            print("Very good.")
        break
    elif class_choice == war_name:
        print("A warrior? Are you sure?")
        break
    elif class_choice == thief_name:
        print("A thief? Are you sure?")
        break
    else:
        class_choice = input("Please type in one of the class names.")

    print(class_list)

print("Excellent! Enjoy your adventure.")




