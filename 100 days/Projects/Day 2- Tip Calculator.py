print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? \
12, 15, or 20? "))
tip_as_percent = tip / 100
total_bill = round(bill + (bill * tip_as_percent), 2)
people = int(input("How many people will split the bill? "))
person_pays = total_bill / people
final_bill = "{:.2f}".format(person_pays)
print(f"Each person should pay: ${final_bill}")
