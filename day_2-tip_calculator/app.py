#!/usr/env/python3

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))
tip_amount = (tip_percentage / 100) * total_bill
total_amount = total_bill + tip_amount
amount_per_person = total_amount / people_count
final_amount = round(amount_per_person, 3)
print(f"Each person should pay: ${final_amount}")