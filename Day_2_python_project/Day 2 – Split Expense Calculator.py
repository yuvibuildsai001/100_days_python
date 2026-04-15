print("###   SPLIT EXPENSE CALCULATOR   ###")
print("Welcome to Split Expense Calculator")

# user input
bill = float(input("Please enter bill: "))

# ask for tip
ask_of_tip = input("Do you want to give a tip? (Y/N): ").upper()

if ask_of_tip == "Y":
    tip = int(input("Enter tip percentage: "))
else:
    tip = 0

# calculations
tip = tip / 100
total_tip = bill * tip
GST = 0.18 * bill
total_bill = bill + total_tip + GST

# printing
print(f"Tip = ₹{total_tip:.2f}")
print("GST = 18%")
print(f"Total Bill = ₹{total_bill:.2f}")

# split
ask_for_split = input("Do you want to split the bill? (Y/N): ").upper()

if ask_for_split == "Y":
    split = int(input("How many friends? : "))

    if split > 0:
        print(f"Each person should PAY = ₹{total_bill / split:.2f}")
    else:
        print("Invalid number of people ❌")
else:
    print(f"Your Total Bill is :> {total_bill}")
    print("Visit again 😊")