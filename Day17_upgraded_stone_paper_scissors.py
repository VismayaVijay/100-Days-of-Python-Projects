from getpass import getpass as input
import emoji
print("Rock(R)",emoji.emojize(":rock:"),(","), "Paper(P)",emoji.emojize(":page_facing_up:"),(","),"Scissors(S)",emoji.emojize(":scissors:"))
print()
print()
print("Select R,P or S")

player1_counter=0
player2_counter=0
print()

while True:
  player1=input("Player1's turn: ")
  player2=input("Player2's turn: ")
  print()

  if player1=="R":
    if player2=="R":
      print("It's a tie! Time for a do-over.")


    elif player2=="P":
      print("Player2's paper wraps Player1's rock into submission!")
      player2_counter+=1

    elif player2=="S":
      print("Player1 smashes Player2's scissors into smithereens!")
      player1_counter+=1
    else:
      print("Entry not recognized!")

  if player1=="P":
    if player2=="P":
      print("It's a tie! Time for a do-over.")


    elif player2=="R":
      print("Player1's paper wraps player2's rock into submission!")
      player1_counter+=1

    elif player2=="S":
      print("Player2's scissors makes confetti out of Player1's paper!")
      player2_counter+=1
    else:
      print("Entry not recognized!")

  if player1=="S":
    if player2=="S":
      print("It's a tie! Time for a do-over.")


    elif player2=="P":
      print("Player1's scissors makes confetti out of Player2's paper!")
      player1_counter+=1

    elif player2=="R":
      print("Player2's rock smashes Player1's scissors into smithereens!")
      player2_counter+=1

    else:
      print("Entry not recognized!")


  print()

  if player1_counter==3:
    print("Player1 wins")
    print("Player1 has",player1_counter,"points!")
    print("Player2 has",player2_counter,"points!")
    exit()
  elif player2_counter==3:
    print("Player2 wins")
    print("Player1 has",player1_counter,"points!")
    print("Player2 has",player2_counter,"points!")
    exit()
  else:
    continue

