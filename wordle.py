class State:
    def __init__(self, wordlist):
        self.guesses = 0
        self.wordlist = wordlist
        # letters that cannot be in word
        self.blacks = set()
        # if l is in yellow then l is present in word
        # l cannot be in positions yellow[l]
        self.yellows = {}
        # greens[i] is a letter that must be at position i
        self.greens = {}
        # banned words are not in the wordle wordlist
        self.banned = set()

    def process(self, guess, outcome):
        if outcome == "banned":
            self.banned.add(guess)
            return
        if len(outcome) != 5:
            raise Exception(outcome)
        for i,o in enumerate(outcome):
            l = guess[i]
            if o == 'g':
                self.greens[i] = l
            elif o == 'y':
                self.yellows[l] = self.yellows.get(l, []) + [i]
            elif o == 'b':
                self.blacks.add(l)
            else:
                raise Exception(outcome)
        # There is a bug in wordle that will show a letter
        # as black AND green if it's entered more times than it's present
        self.blacks -= set(self.greens.values())
        self.blacks -= set(self.yellows.keys())

    def is_allowed(self, word):
        if word in self.banned:
            return False
        if not all(y in word for y in self.yellows.keys()):
            return False
        for i,l in enumerate(word):
            if l in self.blacks:
                return False
            if l in self.yellows and i in self.yellows[l]:
                return False
            if i in self.greens and self.greens[i] != l:
                return False
        return True

    def generate_guess(self):
        for word in self.wordlist:
            if self.is_allowed(word):
                self.guesses += 1
                return word
        return "not found"


def main(wordlist):
    done = False
    state = State(wordlist)
    while not done:
        guess = state.generate_guess()
        if guess == "not found":
            print("Not Found")
            return

        print("Guess: " + guess)
        outcome = input("Output: ")

        if outcome == "ggggg":
            return "done"

        state.process(guess, outcome)


if __name__ == "__main__":
    wordlist = []
    with open('./wordsets/words_freq') as f:
        wordlist = f.read().splitlines()
    main(wordlist)
