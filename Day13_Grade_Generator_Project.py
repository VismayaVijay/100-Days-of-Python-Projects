print("Grade Generator")
print()

test=input("Name of Exam :")
score_max=int(input("Maximum possible score: "))
score_received=int(input("Your score: "))

percentage=(score_received/score_max)*100
final_perc=round(float(percentage,2))

print(final_perc)
if percentage >=90 :
  print("You got",final_perc,"% which is an A+.")

elif percentage >=80 and percentage<=89:
  print("You got",final_perc,"% which .s an A-.")

elif percentage >=.70 and percentage<=.79:
  print("You got",final_perc,"% which is a B.")

elif percentage >=60 and percentage<=69:
  print("You got",final_perc,"% which is a C.")

elif percentage >=50 and percentage<=59:
  print("You got",final_perc,"% which is a D.")

elif percentage >=40 and percentage<=49:
  print("You got",final_perc,"% which is a U.")

else:
  print("You got",final_perc,"% which is a",'\033[31m',"Fail",'\033[30m','.')
