print("How many seconds in a year?")

seconds_normal= 60*60*24*365
seconds_leap=60*60*24*365*24*60*60

seconds_ =input("Is this a leap year?\n")

if seconds_ =="yes":
  print("The leap year has a total of",seconds_leap,"seconds.")
else:  
  print("Total number of seconds in a normal year is",seconds_normal,"seconds")


#seconds_normal= 60*60*24*365
  #seconds_leap=60*60*24*365*24*60*60
  #another method
# days =int(input("How many days in this year?\n"))
#print()
#if days==365:
# print("Total number of seconds in a normal year is",seconds_normal,"seconds"")
#else:
  
# print("Total number of seconds in a normal year is",seconds_normal,"seconds")
