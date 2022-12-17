
# way to input your guess - limit to 6 guesses per round

# each guess should give you the correct v incorrect letters

num_guesses = 0

correct_word = "earth"

correct_list = list(correct_word)

while num_guesses < 6:

    word_guess = input("What do you think the word is?")

    if len(word_guess) > 5 or len(word_guess) < 5:
        print(f"Whoops, your guess isn't 5 characters long - it's {len(word_guess)} characters long. Try again.")
        continue

    word_list = list(word_guess)

    guess_string = ""

    for index, char in enumerate(word_list):

        if char in correct_list:
            if correct_list[index] == char:
                letter_colour = "🟩"
            else:
                letter_colour = "🟨"
        else:
            letter_colour = "⬜"

        guess_string += letter_colour

    guess_list = list(guess_string)

    for index, char in guess_list:
        if char == "🟨":
            count_char = guess_string.count(char)
            count_word_guess = word_guess.count(guess_list[index]) # eerie
            count_correct_string = correct_word.count(char) # earth

            if count_word_guess > count_correct_string:

                count_difference = count_word_guess - count_correct_string
                count_greens = 0

                for index_two, char_two in guess_list:
                    if char_two == guess_list[index]:
                        if index_two != index and guess_list[index_two] == "🟩":
                            count_greens += 1

                while count_difference > 0:




            #eerie
            #earth

            if count_char

    if guess_string == "🟩🟩🟩🟩🟩":
        print(f"Congratulations, you've gotten the answer in {num_guesses+1} guess(es)!")
        break
    else:
        print(f"Not quite right - here's your hint {guess_string}")

    num_guesses += 1




