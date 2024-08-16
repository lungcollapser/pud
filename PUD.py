import chooseClass

class_list = ["Wizard", "Warrior", "Thief"]
order_of_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
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
        yes_no = input("A wizard? Are you sure? Type Y or N.")
        if yes_no == "Y":
            print("Excellent")
        elif yes_no == "N":
            print(class_list)
            print("Type in your class.")
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




