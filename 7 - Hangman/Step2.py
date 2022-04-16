#Step 1 

word_list = ["dog", "baboon", "camel"]

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

import random

# Choose random word from list
chosen_word = random.choice(word_list)
print(f"{chosen_word}\n")

display = []
for eachletter in chosen_word:
    display.append("_")
print(display)
# ask for a letter then convert to lowercase
guess = input("Guess a letter: ").lower()
print("\n")

# No need to convert string to list
# it will convert the chosen string into a list when using for
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

print("\n")
