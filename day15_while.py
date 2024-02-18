#Fix an infinite loop by adding:
#  variable +=1
#This is just saying "Count to 10 by 1 each time." to make the loop end.
#Don't forget, if your condition is a > then you might need to -=. This will subtract from the variable instead of adding to it.

import emoji
exit =""
while exit!='yes':
  print(emoji.emojize(":astonished_face:"))
  exit=input("Exit?:")

---------------------------------------------------------------------

exit=""
animal=""

while exit != "yes":  
   animal=input("What animal do you want?")
   
   if animal =="cow": 
     print("A cow goes moo")
   elif animal=="lemur":
     print("Umm..the Lemur goes awooga")
   else:
    print("Idk what sound",animal,"makes.")

   exit=input("Do you want to exit?")

-----------------------------------------------------------------------------

exit =''
while exit!='yes':
  print("yippee")
  exit=input("Do you wanna exit? ")

else:
  print('I hate seeing you leave, but I love seeing you walk away!')
  
 
