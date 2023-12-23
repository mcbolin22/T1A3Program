import csv
import datetime
from statistics import mean, median, stdev

def get_user_input(prompt, data_type, min_val, max_val):
  while True:
    try:
      value = data_type(input(prompt))
      if min_val is not None and value < min_val:
        print(f"Value must be at least {min_val}. Please enter again.")
      elif max_val is not None and value > max_val:
        print(f"Value must be less than {max_val}. Please enter again.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid number.")
    except TypeError:
      print("Invalid input. Please enter a valid number.")

def create_csv(file_name, data):
  with open(file_name, "a") as csvfile:
    writer = csv.writer(csvfile)
    if not csvfile.tell():  # Check if file is empty (no header yet)
      writer.writerow(["Date", "pH", "Ammonia", "Nitrite", "Nitrate", "Temperature", "DO", "EC"])
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    writer.writerow([current_date] + data)

def add_numbers(file_name):
    print("Add today's numbers")

    ph = get_user_input("Enter pH level: ", float, 0, 14)

    if ph < 6.6:
        print("**Warning: Take Action: add lime to boost pH level**")
    elif ph > 7:
        print("**Warning: Nutrient lockout occurring**")
        if ph > 8:
            print("**Danger! Add acid to lower pH level**")

    ammonia = get_user_input("Enter ammonia (ppm): ", float, 0, 5) 
    if ammonia > 0.75:
        print("**High ammonia reading! Check for dead fish.**")
        if ammonia > 1:
            print("**Stop feeding fish until ammonia is below 0.75ppm.**")
        if ammonia > 2:
            print("**Warning! Toxic ammonia level. Change 1/3 of water immediately.**")

    nitrite = get_user_input("Enter nitrite (ppm): ", float, 0, 5)  
    if nitrite > 0.75:
        print("**High nitrite reading! You may have damaged bacteria.**")
        if nitrite > 1:
            print("**Warning! Toxic nitrite level. Change 1/3 of water immediately.**")

    nitrate = get_user_input("Enter nitrate (ppm): ", float, 0, 100)  # Adjust max range as needed
    if nitrate > 150:
        print("**Consider adding another grow bed to reduce nitrate levels.**")
    if nitrate > 300:
        print("**Warning! Nitrate level toxic for fish. Take immediate action.**")

    temperature = get_user_input("Enter water temperature (°C): ", float, 0, 100)

    if temperature < 4:
        print("**Warning! No bacterial activity will occur below 4°C.**")
        # ... (rest of temperature warnings as before)

    do = get_user_input("Enter dissolved oxygen (mg/L): ", float, 0, 20)

    if do < 5:
        print("**Oxygen level low! Fish may die. Raise water temp or check aeration systems.**")

    ec = get_user_input("Enter electrical conductivity (µS/cm): ", float, 0, 500)

    create_csv(file_name, [ph, ammonia, nitrite, nitrate, temperature, do, ec])

    print("Data saved successfully!")
    
def show_numbers(file_name):
    print("Previous entries")

    print("Date\t\tpH\tAmmonia\tNitrite\tNitrate\tTemperature\tDO\tEC")  # Tab-separated header

    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)[1:]  # Skip header if present

        for row in data:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t\t{row[6]}\t{row[7]}")
    
    return data

def print_entry(entry):
    date, ph, ammonia, nitrite, nitrate, temperature, do, ec = entry  # Handle the list structure
    print(f"Date: {date}")
    print(f"pH: {ph}")
    print(f"Ammonia: {ammonia}")
    print(f"Nitrite: {nitrite}")
    print(f"Nitrate: {nitrate}")
    print(f"Temperature: {temperature}°C")
    print(f"Dissolved oxygen: {do} mg/L")
    print(f"Electrical conductivity: {ec} µS/cm")

def delete_line(file_name, line_number):
  with open(file_name, "r") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
  del data[line_number - 1]
  with open(file_name, "a", newline="") as csvfile:  # Open in append mode
    writer = csv.writer(csvfile)
    writer.writerows(data)  # Write modified data without header

def remove_numbers(file_name, line_number):
    while True:
        try:
            # Get the data before prompting for line number to avoid errors
            data = show_numbers(file_name)  # Retrieve data before input

            # Prompt for line number and validate
            raw_input = input("Enter line number to remove (1-based): ")
            line_number = int(raw_input)

            if 0 < line_number <= len(data):  # Check if line number is valid
                entry = data[line_number - 1]  # Access the entry
                print("Entry retrieved:", entry)  # Print the entry

                confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
                if confirm.lower() == "y":
                    with open(file_name, "w", newline="") as csvfile:  # Open in write mode
                        writer = csv.writer(csvfile)

                        writer.writerow(["Date", "pH", "ammonia", "nitrite", "nitrate", "Temperature", "DO", "EC"])

                        for row in data:  # Iterate through rows directly
                            if row != entry:  # Skip the entry to be removed
                                writer.writerow(row)

                    print(f"\nEntry on line {line_number} successfully removed!")
                    break
                else:
                    print("\nEntry remains unchanged.")
                    break
            else:
                print(f"Invalid line number. Please enter a valid value between 1 and {len(data)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        # Exit prompt
        exit_choice = input("\nDo you want to try removing another entry? (y/N): ")
        if exit_choice.lower() != "y":
            print("\nExiting remove numbers function.")
            break

def analysis(file_name):
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = list(reader)

        data = [[float(value) for value in row[1:]] for row in data]  # Skip the first column (date)

        ph_vals, ammonia_vals, nitrite_vals, nitrate_vals, temp_vals, do_vals, ec_vals = zip(*data)

        print("Data Analysis:")

        print("pH:")
        print(f"\tMean: {mean(ph_vals):.2f}")
        print(f"\tMedian: {median(ph_vals):.2f}")
        print(f"\tStandard deviation: {stdev(ph_vals):.2f}")

        print("Ammonia:")
        print(f"\tMean: {mean(ammonia_vals):.2f}")
        print(f"\tMedian: {median(ammonia_vals):.2f}")
        print(f"\tStandard deviation: {stdev(ammonia_vals):.2f}")

        print("Nitrite:")
        print(f"\tMean: {mean(nitrite_vals):.2f}")
        print(f"\tMedian: {median(nitrite_vals):.2f}")
        print(f"\tStandard deviation: {stdev(nitrite_vals):.2f}")

        print("Nitrate:")
        print(f"\tMean: {mean(nitrate_vals):.2f}")
        print(f"\tMedian: {median(nitrate_vals):.2f}")
        print(f"\tStandard deviation: {stdev(nitrate_vals):.2f}")

        print("Temperature:")
        print(f"\tMean: {mean(temp_vals):.2f}")
        print(f"\tMedian: {median(temp_vals):.2f}")
        print(f"\tStandard deviation: {stdev(temp_vals):.2f}")

        print("DO:")
        print(f"\tMean: {mean(do_vals):.2f}")
        print(f"\tMedian: {median(do_vals):.2f}")
        print(f"\tStandard deviation: {stdev(do_vals):.2f}")

        print("EC:")
        print(f"\tMean: {mean(ec_vals):.2f}")
        print(f"\tMedian: {median(ec_vals):.2f}")
        print(f"\tStandard deviation: {stdev(ec_vals):.2f}")
