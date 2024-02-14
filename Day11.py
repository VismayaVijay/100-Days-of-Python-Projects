print("How many days in a month?")
print("------------------------")
print()

month=input("Give a month: \n")


if month == "january" or month=="January" or month=="march" or month=="March" or month=="may" or month=="May" or month=="july" or month=="July" or month=="august" or month=="August" or month=="october" or month=="October" or month=="December" or month== "december":
  print("The month you gave has 31 days")
elif month=="February" or month=="february":
  print("February can have 28 or 29 days")
  february_leap=input("Is this february a part of a leap year?\n")
  if february_leap=="yes":
    print("Then it has 29 days")
  else:
    print("Then it has 28 days")

else:
  print("The month you gave has 30 days")
