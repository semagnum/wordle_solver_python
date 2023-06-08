from config import WORD_SIZE, FREQUENCY
from wordle import parse_guess, initialize_dictionary

if __name__ == '__main__':
    wordle_dictionary = initialize_dictionary('dictionary.txt', WORD_SIZE)
    print(f'{len(wordle_dictionary)} words added to dictionary.')

    print('Sorting...', end='')
    wordle_dictionary.sort(key=lambda word: min(FREQUENCY.index(letter) for letter in word))
    print('done')

    print('Welcome to Wordle Helper!')

    tries = 0
    while True:
        tries += 1
        if len(wordle_dictionary) == 0:
            print('No possible words available.')
            break

        guess = ''
        while len(guess) != WORD_SIZE:
            guess = input('Enter your guess: ')

        finish_resp = input('Did you answer correctly? (y/N) ')

        if finish_resp.strip()[0].lower() == 'y':
            print(f'Yay, good job! We did it in {"1 try." if tries == 1 else (str(tries) + " tries.")}')
            break

        print()

        wordle_dictionary = parse_guess(wordle_dictionary, guess)

        print(f"{len(wordle_dictionary)} words remaining: {', '.join(wordle_dictionary[:15])}...")
