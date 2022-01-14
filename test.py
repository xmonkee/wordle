from wordle import *
import sys

def gen_output(word, guess):
    for i,l in enumerate(guess):
        if l not in word:
            yield 'b'
        elif word[i] == l:
            yield 'g'
        else: yield 'y'

def test(word):
    guess = generate_guess()
    while guess != word:
        output = list(gen_output(word, guess))
        print(guess + "->" + "".join(output))
        process(guess, output)
        guess = generate_guess()
    print(guess)


test(sys.argv[1])
