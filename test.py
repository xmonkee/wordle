from wordle import *
import sys

def gen_output(word, guess):
    for i,l in enumerate(guess):
        if l not in word:
            yield 'b'
        elif word[i] == l:
            yield 'g'
        else: yield 'y'

def test(word, wordlist, show=False):
    state = State(wordlist)
    guess = state.generate_guess()
    while guess != word:
        output = list(gen_output(word, guess))
        if show:
            print(guess + "->" + "".join(output))
        state.process(guess, output)
        guess = state.generate_guess()
    if show:
        print(guess)
    return state.guesses


# for wordlistfile in ['words_alphabetic', 'words_freq', 'words_common_letters']:
    # wordlist = []

if __name__ == '__main__':
    with open('words') as f:
        wordlist = f.readlines()
    test(sys.argv[1], wordlist, show=True)
