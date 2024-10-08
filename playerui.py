import fontstyle


def player_user_interface():
    player_ui = {"name": 1, "path": 2, "stats/equipment": 3, "continue": 4, "quit": 5}
    print(player_ui)
    # This displays the characters name.
    action = input("Choose your option.")
    if action == "1":
        read_name = open("Player Name", "r")
        print(fontstyle.apply(read_name.read(), "italic"))
# This displays the characters path and gold.
    if action == "2":
        read_path = open("Player Path", "r")
        print(fontstyle.apply(read_path.read(), "italic"))
# This displays the characters class, inventory, and equipment.
    if action == "3":
        read_stats = open("Player Class Equipment", "r")
        print(fontstyle.apply(read_stats.read(), "italic"))
# This allows the player to quit the game and terminate the program.
    if action == "4":
        return
    if action == "5":
        quit()



