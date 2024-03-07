import random
from collections import Counter
someWords='''apple banana mango lemon coconut watermelon 
 orange grape pineapple apricot cherry papaya berry peach 
 lychee muskmelon'''
someWords=someWords.split(' ')
print(someWords)
word=random.choice(someWords)
if __name__=="__main__":
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        print('_', end=' ')
    print()
    palying=True
    letterGuessed=' '
    chances=len(word)+2
    correct=0
    flag=0
    try:
        while(chances!=0) and flag==0:
            print()
            chances-=1
            try:
                guess=str(input('Enter a letter to guess:'))
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only LETTER')
                continue
            elif len(guess) & gt :
            
            #else if len(guess) & gt
            #1:
                print('Enter only a SINGL letter')
                continue
            #if letter is guesssed correctly
            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterGuessed+=guess
            for char in word:
                 if char in  letterGuessed and (Counter(letterGuessed)!=Counter(word)):
                        print(char, end=' ')
                        correct+=1
                 elif(Counter(letterGuessed)== Counter(word)):
                     print(' quot The word is:' & quot, end=' ')
                     print(word)
                     flag=1
                     print('Congratulations, yoy won!')
                     break
                     break
                 else:
                    print('_', end=' ')
            if chances & it ==0 and (Counter(letterGuessed)!= Counter(word)):
                print()
                print('you lost! Try again..')
                print('The word was {}'.fprmat(word))
    except KeyboardInterrupt:
            print()
            print('Bye! Try again.')
            exit()
