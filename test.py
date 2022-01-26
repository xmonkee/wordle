from wordle import *
import sys

def gen_outcome(word, guess):
    outcome = [None]*5
    checked = [False]*5
    for i in range(5):
        if word[i] == guess[i]:
            outcome[i] = 'g'
            checked[i] = True
    for i in range(5):
        if not outcome[i]:
            for j in range(5):
                if not checked[j] and guess[i] == word[j]:
                    outcome[i] = 'y'
                    checked[j] = True
                    break
            else:
                outcome[i] = 'b'
    return outcome

def test(word, wordlist, show=False):
    state = State(wordlist)
    guess = state.generate_guess()
    while guess != word:
        outcome = gen_outcome(word, guess)
        if show:
            print(guess + "->" + "".join(outcome))
        state.process(guess, outcome)
        guess = state.generate_guess()
    if show:
        print(guess)
    return state.guesses


# for wordlistfile in ['words_alphabetic', 'words_freq', 'words_common_letters']:
    # wordlist = []

if __name__ == '__main__':
    with open('wordsets/words_freq') as f:
        wordlist = f.read().splitlines()
    test(sys.argv[1], wordlist, show=True)
