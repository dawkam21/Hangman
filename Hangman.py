import sys


number_of_tries = 5
word = "małżeństwo"
category = "Miłość"
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(f"Category: {category}")
    print(user_word)
    print(f"{number_of_tries} Tries left: ")
    print(f"Letters used: {used_letters}")
    print()

for _ in word:
    user_word.append("_")

while True:
    show_state_of_game()
    letter = input("Pick a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print()
        print("Word doesn't have this letter!")
        number_of_tries -= 1

        if number_of_tries == 0:
            print("Game over!")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter


        if "".join(user_word) == word:
            print("This is the word!")
            print(word)
            sys.exit(0)

