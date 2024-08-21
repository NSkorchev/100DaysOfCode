import random
from hangman_art import logo
from hangman_art import stages
print(logo)

words = []
placeholder = ""
game_over = False
correct_letters = []
hangman = 6

# Get the first word from the user
word = input("Type the first word for the hangman:\n")

while word != "end":
    words.append(word)
    word = input("Type next word for the hangman:\n")

chosen_word = random.choice(words)


for ch in range(len(chosen_word)):
    placeholder += "_"

while not game_over:
    user_input = input("Guess a letter from the word:\n").lower()
    display = ""
    if len(user_input) > 1:
        user_input = (input("Choose only one letter:\n"))

    for letter in chosen_word:
        if letter == user_input:
            display += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if user_input not in chosen_word:
        hangman -= 1
        if hangman == 0:
            game_over = True
            print("Game Over!")

    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[hangman])
    print(display)