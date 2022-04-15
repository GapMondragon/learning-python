#Step 1 

word_list = ["dog", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

# Choose random word from list
chosen_word = random.choice(word_list)
print(f"{chosen_word}\n")

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
