from random import randint
random = randint(1,20)
nguess = 0
name = input("Hello! What is your name?: ")
print("{}{}{}".format("Well, ",name,", I am Thinking of a number between 1 and 20"))
print("You have 5 guesses.")

for i in range(1, 6):
    guess = int(input("Take a guess: "))
    nguess +=1
    if guess > random:
        print("Your guess is too high")
    elif guess < random:
        print("Your guess is too low")
    elif guess == random and nguess == 1:
        print("{}{}{}{}{}".format("Good job, ",name,"! You guessed my number in ",nguess," guess."))
        break
    elif guess == random:
        print("{}{}{}{}{}".format("Good job, ",name,"! You guessed my number in ",nguess," guesses."))
        break
if guess!= random:
    print("{}{}".format("Nope. The number I was thinking of was ", random))