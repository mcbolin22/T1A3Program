import csv
import datetime
from statistics import mean, median, stdev

def get_user_input(prompt, data_type, min_val, max_val):
  while True:
    try:
      value = data_type(input(prompt + ": "))
      if min_val is not None and value < min_val:
        print(f"Value must be at least {min_val}. Please enter again.")
      elif max_val is not None and value > max_val:
        print(f"Value must be less than {max_val}. Please enter again.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid " + data_type.__name__)

def create_csv(file_name, data):
  with open(file_name, "a") as csvfile:
    writer = csv.writer(csvfile)
    if not csvfile.tell():  # Check if file is empty (no header yet)
      writer.writerow(["Date", "pH", "Temperature", "DO", "EC"])
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    writer.writerow([current_date] + data)

def add_numbers(file_name):
    print("Add today's numbers")
    ph = get_user_input("Enter pH level:", float, 0, 14)
    temperature = get_user_input("Enter water temperature (°C):", float, 0, 100)
    do = get_user_input("Enter dissolved oxygen (mg/L):", float, 0, 20)
    ec = get_user_input("Enter electrical conductivity (µS/cm):", float, 0, 500)
    create_csv(file_name, [ph, temperature, do, ec])
    print("Data saved successfully!")


    
def show_numbers(file_name):
    print("Previous entries")
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        if data and data[0][0].lower() == "date":  # Check for header
            data = data[1:]  # Skip header if present
        for row in data:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    return data


def print_entry(entry):
    date, ph, temperature, do, ec = entry  # Handle the list structure
    print(f"Date: {date}")
    print(f"pH: {ph}")
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
            data = show_numbers(file_name)

            # Print the raw input and converted line number
            raw_input = input("Enter line number to remove (1-based): ")
            line_number = int(raw_input)

            if 0 < line_number <= len(data):  # Check if line number is valid
                entry = data[line_number - 1]  # Access the entry
                print("Entry retrieved:", entry)  # Print the entry

                confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
                if confirm.lower() == "y":
                    with open(file_name, "w", newline="") as csvfile:  # Open in write mode
                        writer = csv.writer(csvfile)

                        # Write the header if necessary (corrected logic for header check)
                        # if data and data[0][0].lower() == "date":  # Check if the first row is the header
                        #     writer.writerow(["Date", "pH", "Temperature", "DO", "EC"])  # Write the header
                        
                        writer.writerow(["Date", "pH", "Temperature", "DO", "EC"])

                        # Write all lines except the one to be removed
                        for i in range(len(data)):
                            if i != line_number - 1:
                                writer.writerow(data[i])

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

        # Extract only the numeric values (pH, temperature, DO, EC) from each row
        data = [[float(value) for value in row[1:]] for row in data]  # Skip the first column (date)

        ph_vals, temp_vals, do_vals, ec_vals = zip(*data)

        print("pH:")
        print(f"\tMean: {mean(ph_vals):.2f}")
        print(f"\tMedian: {median(ph_vals):.2f}")
        print(f"\tStandard deviation: {stdev(ph_vals):.2f}")

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

