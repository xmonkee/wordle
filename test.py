from wordle import *
import sys

def test(word):
    def gen_output(guess):
        for i,l in enumerate(guess):
            if l not in word:
                yield 'b'
            elif word[i] == l:
                yield 'g'
            else: yield 'y'
    guess = generate_guess()
    while guess != word:
        output = list(gen_output(guess))
        print(guess + "->" + "".join(output))
        process(guess, output)
        guess = generate_guess()
    print(guess)


test(sys.argv[1])
