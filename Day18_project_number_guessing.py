print("One-Million-To-One")
print()

counter=0


while True:
 
  guess=int(input("Pick a number between 1 and 10,00,000:\n"))
  if guess==500000:
    print("Correct!")
    counter+=1
    break
    
  elif guess<=450000 and guess>=0:
    print("Too low!")
    counter+=1
    continue
    
  elif guess>=550000:
    print("Too high!")
    counter+=1
    continue
    
  elif guess <= 0:
  
    exit()
    
  else:
    print("You are getting close!")
    counter+=1
   
print("It took you",counter,"guess(es) to get it correct!")


