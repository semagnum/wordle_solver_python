from config import Correctness, WORD_SIZE


def initialize_dictionary(filename: str, word_size: int) -> list:
    """Retrieve dictionary to use as a reference for potential words.

    :param filename: text file containing words, separated by new lines
    :param word_size: size of words for Wordle
    :return: list of viable words
    """
    try:
        with open(filename, 'rt') as file:
            lines = file.read().split('\n')

            return list(dict.fromkeys(line
                                      for line in lines
                                      if len(line) == word_size))
    except (OSError, IOError) as e:
        print(f'File error: {e}')
        return []


def parse_guess(dictionary: list[str], guess: str):
    """Prompts user to process the guess and removes impossible words from the dictionary.

    :param dictionary: list of words
    :param guess: the user's guess
    :return: filtered dictionary of possible words
    """
    status = [0] * WORD_SIZE

    correctness_to_letter_to_count = {}
    for c_val in Correctness:
        correctness_to_letter_to_count.setdefault(c_val, {})

    for idx in range(WORD_SIZE):
        num_response = 4
        letter = guess[idx]

        while num_response >= 4:
            print(f"For the letter \"{letter}\", how correct is it?")
            print(f"\t{Correctness.CORRECT}. Correct letter, correct position")
            print(f"\t{Correctness.WRONG_POSITION}. Correct letter, incorrect position")
            print(f"\t{Correctness.WRONG_LETTER}. Incorrect letter")

            num_response = int(input(''))

        correctness_response = Correctness(num_response)
        status[idx] = correctness_response

        correctness_to_letter_to_count[correctness_response].setdefault(letter, 0)
        correctness_to_letter_to_count[correctness_response][letter] += 1

        if correctness_response == Correctness.CORRECT:
            dictionary = [word for word in dictionary if word[idx] == guess[idx]]
        else:
            dictionary = [word for word in dictionary if word[idx] != guess[idx]]

    correct_positions = correctness_to_letter_to_count[Correctness.CORRECT]
    wrong_positions = correctness_to_letter_to_count[Correctness.WRONG_POSITION]
    wrong_letters = correctness_to_letter_to_count[Correctness.WRONG_LETTER]

    for letter in list(wrong_letters):
        # if this letter is not in wrong_position, then it must not be in the true word at all!
        if letter not in wrong_positions and letter not in correct_positions:
            dictionary = [word for word in dictionary if letter not in word]

    for letter in list(wrong_positions):
        count = wrong_positions.get(letter, 0) + correct_positions.get(letter, 0)
        # if there is at least one of that letter in count and 0 instances of it in wrong_letter,
        # then at least `n` of that letter is in the true word
        if letter not in wrong_letters:
            dictionary = [word for word in dictionary if word.count(letter) >= count]
        else:
            # remove all words in dictionary with the incorrect count `n` of that letter
            dictionary = [word for word in dictionary if word.count(letter) != count]

    return dictionary
