# ISM2411 Lab 12 — Read a Sales CSV, Write a Cleaned Report
# Name: Audra
# REFLECTION

# 1. Python ETL vs. Excel:
# Excel is easier for quickly viewing data, making charts, and doing simple calculations.
# Python is better for automating repetitive tasks, processing large amounts of data,
# and creating reports without having to do everything manually.

# 2. Append Mode:
# A business could use an append-mode log to track daily sales transactions.
# Append mode is useful because it adds new information without deleting previous records.
import csv
from datetime import datetime

# EXERCISE 1: Setup
# Check that the sales CSV file can be opened.

# EXERCISE 2: Read and print raw rows

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        # EXERCISE 3: Skip the header

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("\nHeader:")
    print(header)

    print("\nData rows:")

    for row in reader:
        print(row)
        # EXERCISE 4: Compute totals

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity

        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")
# EXERCISE 5: Filter and write

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)

    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                cleaned_count += 1

print("\nExercise 5 Results:")
print(f"Original rows: {original_count}")
print(f"Cleaned rows: {cleaned_count}")
print("Created data/cleaned.csv")
# EXERCISE 6: csv.DictReader

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"\nTotal Revenue using DictReader: ${dict_total_revenue:.2f}")

# csv.reader uses column positions (indexes) to access information.
# csv.DictReader uses column names, making the code easier to understand.
# EXERCISE 7: Sales summary by product

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nExercise 7: Sales Summary")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
    # EXERCISE 8: Append mode log

current_time = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{current_time} - Total Revenue: ${total_revenue:.2f}\n")

print("\nExercise 8: Run Log Updated!")
print("Date and time:", current_time)
print(f"Total Revenue: ${total_revenue:.2f}")