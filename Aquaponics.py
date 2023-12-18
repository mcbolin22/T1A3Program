from functions import add_numbers, view_numbers, remove_numbers, analysis

file_name = "data.csv"
# try:
print("Welcome to the Aquaponics data tracker")

def menu():
    print("1. Enter 1 to add today's data")
    print("2. Enter 2 to view previous data")
    print("3. Enter 3 to remove previous entries")
    print("4. Enter 4 to see analysis of stored data")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = menu()
    if (user_choice == "1"):
        add_numbers()
    elif (user_choice == "2"):
        view_numbers()
    elif (user_choice == "3"):
        remove_numbers()
    elif (user_choice == "4"):
        analysis()
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid Input")

print("Have a nice day!")

# except: