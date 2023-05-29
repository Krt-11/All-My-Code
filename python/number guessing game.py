import random

rndNum = random.randint(1,5)

for i in range(5):
    ans = int(input("guess the number between 1 to 5: \n"))
    if(ans == rndNum):
        print("you guessed it right")
        break
    else:
        print("keep trying")