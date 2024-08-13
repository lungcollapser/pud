

class_list = ["Wizard", "Warrior", "Thief"]
order_of_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]


player = ""


wizard_stats = [10, 14, 12, 20, 16, 18]
thief_stats = [10, 20, 14, 12, 16, 18]
war_stats = [20, 16, 18, 10, 12, 14]

print(">Welcome to PUD")
print(">What is your name?")
input(player)
print(">...Very interesting. What is your class?")
print(class_list)
class_choice = input("> ")
while class_choice:
    if class_choice == "Wizard":
        print("A wizard? Are you sure?")
    elif class_choice == "Warrior":
        print("A warrior? Are you sure?")
    elif class_choice == "Thief":
        print("A thief? Are you sure?")
    else:
        print("Please type in one of the class names.")
print(class_list)





