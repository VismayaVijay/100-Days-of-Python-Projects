print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")
print()

while True:
  blank=input('Never going to ------ you.\n')

  if blank=='forget':
    print("Finally!!")
    break
   
  else:
    print("Nope, try again!")
    print()
   
------------------------------------------------------------------------------------

print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")
print()

counter=1
while True:
  blank=input('Never going to ------ you.\n')

  if blank=='forget' or blank=='Forget':
    print("Finally!!")
    
  else:
    print("Nope, try again!")
    print()
    counter+=1
  if blank=="forget" or blank=="forget":
    break
    
print("Thanks for playing!")    
print()
print('You got the correct lyrics in', counter,"attempt(s).")






