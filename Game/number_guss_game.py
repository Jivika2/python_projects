import random
import math
#take a input
lower= int(input("Enter lowrt bound :-"))
upper=int(input("Enter upper bond:-"))
#generate random number between lower and upper
x= random.randint(lower,upper)
print("\n\t you've only",
      round(math.log(upper-lower+1,2)),
      "chances to guess the integer!\n")
count=0
while count<math.log(upper-lower+1,2):
  count+=1
  guess=int(input("Guess a number:-"))
  if x==guess:
    print("congratulations you did it in ",count, "try")
  elif x>guess:
    print('You guessed too small!')
  elif x<guess:
    print('You Guessed too high!')
if count>=math.log(upper-lower+1,2):
  print("\nThe number is %d" %x)
  print("\tBetter Luck Next time!")