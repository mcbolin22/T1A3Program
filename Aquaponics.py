
from statistics import mean, median, stdev
from functions import add_numbers, view_numbers, remove_numbers, analysis


file_name = "data.csv"

try:
    data_file = open(file_name, "r")
    data_file.close()
    print("In try block")
except FileNotFoundError:
    data_file = open(file_name, "w")
    data_file.write("date,pH,temp,DO,EC")
    data_file.close()
    print("In except block")
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
        add_numbers(file_name)
    elif (user_choice == "2"):
        view_numbers(file_name)
    elif (user_choice == "3"):
        try:
            line_number = int(input("Enter line number to remove (1-based): "))
            if 0 < line_number <= len(get_data(file_name)):
                remove_numbers(file_name, line_number)
            else:
                print(f"Invalid line number. Please enter a valid value between 1 and {len(get_data(file_name))}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif (user_choice == "4"):
        if len(get_data(file_name)) > 1:
            analysis(file_name)
        else:
            print("No data available for analysis. Please add some entries first.")
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid Input")

print("Have a nice day!")

# except: