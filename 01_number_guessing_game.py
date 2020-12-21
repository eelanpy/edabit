#01_number_guessing_game:
 
import random as rand

def guess_number():
    round = 1
    name = input("What is your name? ")
    #print(name)
    print("Welcome to round {}, {}".format(round, name))
    answer = rand.randint(0, 100)
    #print(answer)
    while True:
        user_guess = int(input("\nPick a number from 0 to 100:  "))
        if user_guess > answer:
            print("Your guess is too high!")
            round += 1
        elif user_guess < answer:
            print("Your guess is too low!")
            round += 1
        else:
            print("Your guess {} is correct after {} guesses!".format(user_guess, round))
            break

guess_number()    
