#!/usr/bin/python3

WORDS = list()

def load_directory():
    with open('/usr/share/dict/words') as words:
        for w in words.readlines():
            WORDS.append(w.strip())

def guess_forever():
    guess = None
    round_counter = 1
    initial = int(len(WORDS) / 2)

    while True:
        if not guess:
            guess = initial
        print('Guess the word: {}'.format(WORDS[guess]))

        player = input('Did the opponent say their word is BEFORE (-), AFTER (+), or EXACTLY (0) the guess: ')

        if player == '0':
            guess = None
            round_counter = 1
        else:
            round_counter += 1
            delta = int(len(WORDS) / 2**round_counter)
            if player == '+':
                guess += delta
            else:
                guess -= delta
            if delta <= 1:
                print('last guesses: {}, {}, {}, {}'.format(WORDS[guess], WORDS[guess+1], WORDS[guess-1], WORDS[guess-2])) # check this logic
                guess = None
                round_counter = 1

if __name__ == "__main__":
    load_directory()
    guess_forever()
