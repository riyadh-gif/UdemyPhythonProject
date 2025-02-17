import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)



# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
placeholder = ["_"] * len(chosen_word)

while "_" in placeholder :
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
                if letter == guess:
                    placeholder[i] = guess
        print("Right")
    else:
            print("Wrong")

    print(" ".join(placeholder))

# print(chosen_word)






