import random


wordList = ["word", "answer", "balloon", "chocolate", "brooklyn"]
maxChances = len(wordList) - 2;
wordAnswer = wordList[random.randint(0, len(wordList))]


print("\nYour job here is to guess the word. \n\
The List contains {0} entries and you have {1} chances to guess the correct word.\n"\
    .format(len(wordList), maxChances))


for i in range(maxChances):
    ans = input("Enter your {} guess: ".format(i+1))
    if(ans == wordAnswer):
        print("You guessed the word right in {1} tries and the guess was {0}"\
            .format(wordAnswer, maxChances))
        break
    else:
        maxChances -= 1
        print("Your guess was not correct, try again. \nYou have {} tries left\n\n"\
            .format(maxChances))

if (maxChances == 0):
    print("The correct guess was: " + wordAnswer + "\n\n\n")