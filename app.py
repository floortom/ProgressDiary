menu = """
Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection:
"""
welcome = "Welcome to the progress diary!"

while (userInput := input(menu)) != "3":
    if userInput == "1":
        print("Adding...")
    elif userInput == "2":
        print("View...")
    else:
        print("Invalid options selected.")
