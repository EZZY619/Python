# Tip Calculator Program

print("Welcome to the Tip Calculator!")

# Step 1: Get the bill amount
bill = float(input("What was the total bill? $"))

# Step 2: Ask for tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Step 3: Ask how many people are splitting the bill
people = int(input("How many people to split the bill? "))

# Step 4: Calculate the tip and total per person
tip_amount = (tip_percent / 100) * bill
total_bill = bill + tip_amount
amount_per_person = total_bill / people

# Step 5: Round to 2 decimal places and show result
final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount}")
