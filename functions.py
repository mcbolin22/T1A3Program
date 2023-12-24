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
    if not csvfile.tell():
      writer.writerow(["Date", "pH", "Ammonia", "Nitrite", "Nitrate", "Temperature", "DO", "EC"])
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    writer.writerow([current_date] + data)

def add_numbers(file_name):
    print("Add today's numbers")

    ph = get_user_input("Enter pH level: ", float, 0, 14)
    if ph < 6.6:
        print("Warning: Take Action: add lime to boost pH level")
    elif ph > 7:
        print("Warning: Nutrient lockout occurring")
        if ph > 8:
            print("Danger! Add acid to lower pH level")

    ammonia = get_user_input("Enter ammonia (ppm): ", float, 0, 5) 
    if ammonia > 0.75:
        print("High ammonia reading! Check for dead fish.")
        if ammonia > 1:
            print("Stop feeding fish until ammonia is below 0.75ppm.")
        if ammonia > 2:
            print("Warning! Toxic ammonia level. Change 1/3 of water immediately.")

    nitrite = get_user_input("Enter nitrite (ppm): ", float, 0, 5)  
    if nitrite > 0.75:
        print("High nitrite reading! You may have damaged bacteria.")
        if nitrite > 1:
            print("Warning! Toxic nitrite level. Change 1/3 of water immediately.")

    nitrate = get_user_input("Enter nitrate (ppm): ", float, 0, 160)
    if nitrate > 70:
       print("Consistently introduce more plants")
    if nitrate > 100:
        print("Consider adding another grow bed to reduce nitrate levels.")
    if nitrate > 150:
        print("Warning! Nitrate level toxic for fish. Take immediate action.")

    temperature = get_user_input("Enter water temperature (°C): ", float, 0, 100)
    if temperature < 0 or temperature > 49:
      print("Warning! Nitrifying bacteria and edible plants will die at temperatures below 0°C or above 49°C.")
    else:
      if temperature < 4:
        print("Warning! No bacterial activity will occur below 4°C.")
      else:
        if temperature < 10:
          print("The water is cold. Bacterial growth rate is decreased 75%.")
        elif temperature < 18:
          print("The water is cool. Bacterial growth rate is decreased 50%.")
        elif temperature < 30:
          print("The water is within the optimal temperature range for nitrifying bacteria.")
        else:
          print("The water is too hot and may harm bacteria.")

      if 18 <= temperature <= 25:
        print("The water temperature is optimal for plant growth.")
      else:
        print("The water temperature is not ideal for plant growth.")

    do = get_user_input("Enter dissolved oxygen (mg/L): ", float, 0, 20)
    if do < 5:
        print("Oxygen level low! Fish may die. Lower water temp or check aeration systems.")

    ec = get_user_input("Enter electrical conductivity (µS/cm): ", float, 0, 500)
    if ec == 0:
       print("Nutrient levels low!")

    create_csv(file_name, [ph, ammonia, nitrite, nitrate, temperature, do, ec])

    print("Data saved successfully!")
    
def show_numbers(file_name):
    print("Previous entries")

    print("Date\t\tpH\tAmmonia\tNitrite\tNitrate\tTemperature\tDO\tEC")

    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)[1:]

        for row in data:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t\t{row[6]}\t{row[7]}")
    
    return data

def print_entry(entry):
    date, ph, ammonia, nitrite, nitrate, temperature, do, ec = entry
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
  with open(file_name, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

def remove_numbers(file_name, line_number):
    while True:
        try:
            line_number = int(input("\nConfirm line number to remove (1-based): "))

            with open(file_name, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)[1:]

            if 1 <= line_number <= len(rows):
                entry = rows[line_number - 1]
                print("Entry retrieved:", entry)

                confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
                if confirm.lower() == "y":
                    rows.pop(line_number - 1)

                    with open(file_name, "w", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["Date", "pH", "ammonia", "nitrite", "nitrate", "Temperature", "DO", "EC"])
                        writer.writerows(rows[1:])

                    print(f"\nEntry on line {line_number} successfully removed!")
                    break
                else:
                    print("\nEntry remains unchanged.")
                    break
            else:
                print(f"Invalid line number. Please enter a valid value between 1 and {len(rows)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        exit_choice = input("\nDo you want to try removing another entry? (Y/N): ")
        if exit_choice.lower() != "y":
            print("\nExiting remove previous entries.")
            break

# def remove_numbers(file_name, line_number):
#     while True:
#         try:
#             line_number = int(input("\nEnter line number to remove (1-based): "))

#             if 0 < line_number <= len(show_numbers(file_name)):
#                 entry = show_numbers(file_name)[line_number - 1]
#                 print("Entry retrieved:", entry)

#                 confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
#                 if confirm.lower() == "y":
#                     with open(file_name, "r", newline="") as csvfile:  # Open in read mode
#                         reader = csv.reader(csvfile)
#                         rows = list(reader)  # Read all rows into a list

#                     rows.pop(line_number - 1)  # Remove the specified row from the list

#                     with open(file_name, "w", newline="") as csvfile:  # Open in write mode
#                         writer = csv.writer(csvfile)
#                         writer.writerows(rows)  # Write all remaining rows back to the file

#                     print(f"\nEntry on line {line_number} successfully removed!")
#                     break
#                 else:
#                     print("\nEntry remains unchanged.")
#                     break
#             else:
#                 print(f"Invalid line number. Please enter a valid value between 1 and {len(show_numbers(file_name))}")
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")

#         exit_choice = input("\nDo you want to try removing another entry? (Y/N): ")
#         if exit_choice.lower() != "y":
#             print("\nExiting remove previous entries.")
#             break


# def remove_numbers(file_name, line_number):
#    while True:
#        try:
#            line_number = int(input("\nEnter line number to remove (1-based): "))

#            if 0 < line_number <= len(show_numbers(file_name)):
#                entry = show_numbers(file_name)[line_number - 1]
#                print("Entry retrieved:", entry)

#                confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
#                if confirm.lower() == "y":
#                    with open(file_name, "w", newline="") as csvfile:
#                        writer = csv.writer(csvfile)

#                        writer.writerow(["Date", "pH", "ammonia", "nitrite", "nitrate", "Temperature", "DO", "EC"])

#                        for row in show_numbers(file_name):
#                            if row != entry: 
#                                writer.writerow(row)

#                    print(f"\nEntry on line {line_number} successfully removed!")
#                    break
#                else:
#                    print("\nEntry remains unchanged.")
#                    break
#            else:
#                print(f"Invalid line number. Please enter a valid value between 1 and {len(show_numbers(file_name))}")
#        except ValueError:
#            print("Invalid input. Please enter a valid integer.")

#        exit_choice = input("\nDo you want to try removing another entry? (Y/N): ")
#        if exit_choice.lower() != "y":
#            print("\nExiting remove previous entries.")
#            break

def analysis(file_name):
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = list(reader)

        data = [[float(value) for value in row[1:]] for row in data]

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
