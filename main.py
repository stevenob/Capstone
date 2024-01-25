import time
import random
import os

def createLetterList(word):
        char_list = []
        for c in word:
            char_list.append(c)
        return char_list
    
def Main():
    # Setting variables for new round
    active_guess = "_ _ _ _ _"
    active_guess = active_guess.split(" ")
    win = False
    strikes = 0
    guesses = []

    # Reading from words.txt and setting mystery word
    print("Generating word...")
    with open('words.txt', 'r') as file:
        data = file.read()
    word_list = data.split("\n")
    word = word_list[random.randint(0,len(word_list))]
    time.sleep(2.5)

    # Starting Game Loop
    while not win and strikes != 5:
        os.system('cls')
        print(f"{active_guess}\nstrikes: {strikes} \nguesses: {guesses}")
        guess = input()
        if len(guess) == 5:
            if guess == word:
                win = True
                print(f"\n\n*****\You\nWin!\n*****")
                input()
                
            # Checking per character 
            guessCheck = createLetterList(guess)
            for i in range(0, len(guessCheck)):
                if guessCheck[i] == word[i]:
                    active_guess[i] = word[i]
                            
            # Updating strikes and guesses list
            strikes += 1
            guesses.append(guess)
            os.system('cls')
        else:
            os.system('cls')
            print("Guess should be 5 letters!")
            time.sleep(1.5)
    print(f'Loser...\nWord: {word}')
            

os.system('cls')
Main()