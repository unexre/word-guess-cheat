#!/usr/bin/env python3

WORDS = []

def load_directory():
    with open('/usr/share/dict/words') as words:
        for w in words.readlines():
            WORDS.append(w.strip())

def guess_forever():
    guess_index = None
    round_counter = 1
    initial_index = int(len(WORDS) / 2)

    while True:
        if not guess_index:
            print('** New game!')
            guess_index = initial_index
        print('Guess the word: {}'.format(WORDS[guess_index]))

        player_input = input('Did the opponent say their word is BEFORE (-), AFTER (+), or EXACTLY (0) the guess: ')

        if player_input.lower().startswith('q'):
            raise EOFError

        if player_input not in ['-', '+', '0']:
            continue

        if player_input == '0':
            # we "won", so start over
            guess_index = None
            round_counter = 1
        else:
            # binary search up or down
            round_counter += 1
            delta = int(len(WORDS) / 2**round_counter)
            if player_input == '+':
                # up
                guess_index += delta
            else:
                # down
                guess_index -= delta
            if delta <= 1:
                # search window has reduced us to 1-3 options, so print the neighbors and start over
                print('final guesses: {}, {}, {}, {}'.format(WORDS[guess_index], WORDS[guess_index+1], WORDS[guess_index-1], WORDS[guess_index-2]))
                guess_index = None
                round_counter = 1

if __name__ == "__main__":
    load_directory()
    try:
        guess_forever()
    except (KeyboardInterrupt, EOFError) as e:
        print('\nGoodbye!')
        exit()
