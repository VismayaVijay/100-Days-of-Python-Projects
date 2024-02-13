print("Tip Calculator")
print()

bill=float(input("How much did you spend?\n"))
tip = float(input("What percentage do you want to tip?\n"))
people =int(input("How many people were there in your group?\n"))
tip_percentage= tip/100
bill_tip=tip_percentage*bill

total= bill_tip + bill

print()
print("Total bill amount including tip is ", total)
bill_each=total/people
bill_each=round(bill_each,2)

print("You each owe","$",bill_each)
