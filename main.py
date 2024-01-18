import time
import random

def main():
    active_guess = "_ _ _ _ _"
    word = ""
    win = False
    strikes = 0
    print("Generating word...")
    with open('words.txt', 'r') as file:
        data = file.read()
    word_list = data.split("\n")
    word = word_list[random.randint(0,len(word_list))]
    time.sleep(2.5)

    while not win and strikes != 3:
        print(f"{active_guess}\nword: {word} \nstrikes: {strikes}")
        guess = input()
        if guess == word:
            win = True
            print("Yes!")
        strikes += 1

main()