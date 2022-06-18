#Guess The number Game
import random
import sys
myGuess=random.randint(1,20)
def checkGuess(guess):
        if guess > myGuess: 
            print('Too High')
        elif guess < myGuess:
            print('Too Low!')
        elif guess == myGuess:
            print('Wow, You\'re a mind reader')
            sys.exit()
            
name=input("What is your name?\n")
print('Well,'+name+' I am thinking of a number between 1 and 20\nTake a guess.')
count=0
for count in range(5):
    try:
        guess=int(input())
        checkGuess(guess)
    except ValueError:
        print('Not a valid Integer Try, again')

    count+=1
if(count>=5): print('Out of guesses!,' 'my Guess was',myGuess)