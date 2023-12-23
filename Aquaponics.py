from functions import add_numbers, show_numbers, remove_numbers, analysis

file_name = "data.csv"

try:
    data_file = open(file_name, "r")
    data_file.close()
    print("data.csv found")
except FileNotFoundError:
    data_file = open(file_name, "w")
    data_file.write("Date,pH,Ammonia,Nitrite,Nitrate,Temperature,DO,EC")
    data_file.close()
    print("data.csv created")

print("\nWelcome to the Aquaponics data tracker")

def menu():
    print("\n1. Enter 1 to add today's data")
    print("2. Enter 2 to view previous data")
    print("3. Enter 3 to remove previous entries")
    print("4. Enter 4 to see analysis of stored data")
    print("5. Enter 5 to exit")
    choice = input("\nEnter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = menu()
    if (user_choice == "1"):
        add_numbers(file_name)
    elif (user_choice == "2"):
        show_numbers(file_name)
    elif (user_choice == "3"):
        show_numbers(file_name)
        line_number = int(input("Enter line number to remove (1-based): "))
        remove_numbers(file_name, line_number)
    elif (user_choice == "4"):
        if len(show_numbers(file_name)) > 1:
            analysis(file_name)
        else:
            print("No data available for analysis. Please add some entries first.")
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid Input")

print("\nHave a nice day!")