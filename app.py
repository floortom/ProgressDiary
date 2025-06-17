from database import add_entry, get_entries

menu = """
Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection:
"""
welcome = "Welcome to the progress diary!"

def prompt_new():
    entryContent = input("What have you learned today?")
    entryDate = input("Enter the date: ")
    add_entry(entryContent, entryDate)

def view_entries(entries):
    for entry in get_entries():
        print(f"{entry["date"]}\n{entry["content"]}\n\n")

print(welcome)

while (userInput := input(menu)) != "3":
    if userInput == "1":
        prompt_new()
    elif userInput == "2":
        view_entries(get_entries())
    else:
        print("Invalid options selected.")
