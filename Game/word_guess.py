import random
name=input("What is your name?")
print("Good luck !",name)
word=['rainbow','computer','science','programming',
      'python','mathmatics','player','condition',
      'reverse','water','board','geeks']
print("Guess the characters")
guesses=''
turns=12
while turns>0:
  
  failed=0
  for char in word:
   if char in guesses:
    print(char, end='')
   else:
    print('_')
    failed+=1
  if failed==0:
    print('you win')
    print("The word is:",word)
  break
print()
guess=input("guess a character:")
guesses+=guess
if guess not in word:
 turns-=1
 print("Wrong")
 print("you have", + turns, "more guesses")
 if turns==0:
  print("you Loose")

