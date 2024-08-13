

class_list = ["Wizard", "Warrior", "Thief"]
order_of_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
wiz_name = "Wizard"
thief_name = "Thief"
war_name = "Warrior"

player = ""
class_choice = ""

wizard_stats = [10, 14, 12, 20, 16, 18]
thief_stats = [10, 20, 14, 12, 16, 18]
war_stats = [20, 16, 18, 10, 12, 14]

print("Welcome to PUD")
print("What is your name?")
input(player)
print("...Very interesting. What is your class?")
print(class_list)
while input(class_choice):
    if class_choice == wiz_name:
        print("A wizard? Are you sure?")
    elif class_choice == war_name:
        print("A warrior? Are you sure?")
    elif class_choice == thief_name:
        print("A thief? Are you sure?")
    else:
        print("Please type in one of the class names.")
    print(class_list)





