import emoji
print("Game of Rock",emoji.emojize(":rock:"),",", "Paper",emoji.emojize(":page_facing_up:"),",","Scissors",emoji.emojize(":scissors:"))

# getpass lets inputs given by the players to remain hiden on screen
print()
from getpass import getpass as input

print("R - ",emoji.emojize(":rock:"))
print("P - ",emoji.emojize(":page_facing_up:"))
print("S - ",emoji.emojize(":scissors:"))
print()

print("Select your move(R, P or S)")
print()


player_1=input("Choose your move, Player 1: ")
player_2=input("Choose your move, Player 2: ")

print()

if player_1=='R':
    if player_2=='R':
      print("Tie.This is a day for do-overs!!")
    elif player_2=='P':
      print("Player 1 is smothered by Player 2's paper!")
    elif player_2=='S':
      print("Player 1 smashes Player 2's scissors to smithereens")
    else:
      print("Entry not recognised!")

elif player_1 =='P':
   if player_2=='P':
      print("Tie.This is a day for do-overs!!")
   elif player_2=='R':
      print("Player 1's paper smotheres Player 2's rock!")
   elif player_2=='S':
      print("Player 1's rock smashes Player 2's scissors to smithereens")
   else:
      print("Entry not recognised!")

elif player_1 =='S': 
   if player_2=='S':
      print("Tie.This is a day for do-overs!!")
   elif player_2=='R':
      print("Player 1's scissors gets demolished by Player 2's rock!")
   elif player_2=='P':
    print("Player 1 cuts Player 2's paper to itty, bitty pieces!!")
   else:
      print("Entry not recognised!")

else:
 print("Entry not recognised!!")

 
  



















