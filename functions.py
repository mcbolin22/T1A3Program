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

# def view_numbers(file_name):
#     print("Previous entries")
#     with open(file_name, "r") as csvfile:
#         reader = csv.reader(csvfile)
#         print("Date\t\tpH\tTemp\tDO\tEC")
#         next(reader)
#         for row in reader:
#             print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

# def get_data(file_name):
#     with open(file_name, "r") as csvfile:
#         reader = csv.reader(csvfile)
#         # Skip header if it exists
#         next(reader)
#         data = [row for row in reader]
#     return data

def show_numbers(file_name):
    print("Previous entries")
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        if next(reader)[0].lower() == "date":
            next(reader)
        for row in reader:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

def print_entry(entry):
    line_number, date, ph, temperature, do, ec = entry
    print(f"Line {line_number}:")
    print(f"\tDate: {date}")
    print(f"\tpH: {ph:.2f}")
    print(f"\tTemperature: {temperature:.2f}°C")
    print(f"\tDissolved oxygen: {do:.2f} mg/L")
    print(f"\tElectrical conductivity: {ec:.2f} µS/cm")

def delete_line(file_name, line_number):
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    del data[line_number - 1]  # Adjust index for 1-based line number
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "pH", "Temperature", "DO", "EC"])
        writer.writerows(data)


def remove_numbers(file_name):
  while True:
    try:
      line_number = int(input("Enter line number to remove (1-based): "))
      if 0 < line_number <= len(get_data(file_name)):
        entry = show_numbers(file_name)[line_number - 1]
        print(f"\nPreview of entry to be removed (line {line_number}):")
        print_entry(entry)
        confirm = input("\nAre you sure you want to remove this entry? (y/N) ")
        if confirm.lower() == "y":
          delete_line(file_name, line_number)
          print(f"\nEntry on line {line_number} successfully removed!")
          break
        else:
          print("\nEntry remains unchanged.")
          break
      else:
        print(f"Invalid line number. Please enter a valid value between 1 and {len(get_data(file_name))}")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

def analysis(file_name):
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        data = list(reader)
        ph_vals, temp_vals, do_vals, ec_vals = zip(*data)
        print("pH:")
        print(f"\tMean: {mean(ph_vals):.2f}")
        print(f"\tMedian: {median(ph_vals):.2f}")
        print(f"\tStandard deviation: {stdev(ph_vals):.2f}")


