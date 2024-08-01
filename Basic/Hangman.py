import random
import hangmanwords as words
import hangmanart as art
print(art.logo)
print("")
print("Welcome to the Hangman Game!!!")

# words_list = ["Spotify", "Chair", "Hitler", "Camel", "Apple", "Books", "Looks", "Jam", "peanut"]

chosen_word = random.choice(words.word_list).lower()
# print(chosen_word)

display = []

for i in chosen_word:
    display.append("_")
print(display)

lives = 6
end_of_game = False
print(art.stages[-1])
while not end_of_game:
    guess = input("Guess the word:").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter in guess:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        print(art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("you lose")
            print(f"The Correct word was {chosen_word}")
            break
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you guessed the correct word")
