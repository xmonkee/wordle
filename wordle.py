class State:
    def __init__(self):
        # letters that cannot be in word
        self.blacks = set()
        # if l is in yellow then l is present in word
        # l cannot be in positions yellow[l]
        self.yellows = {}
        # greens[i] is a letter that must be at position i
        self.greens = {}

    def process(self, guess, outcome):
        if len(outcome) != 5 or len(set(outcome)-set("byg")) > 0:
            raise Exception(outcome)
        for i,o in enumerate(outcome):
            l = guess[i]
            if o == 'b':
                self.blacks.add(l)
            elif o == 'y':
                self.yellows[l] = self.yellows.get(l, []) + [i]
            else:  # o == 'g'
                self.greens[i] = l

    def is_allowed(self, word):
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

    def generate_guess(self, wordlist):
        for word in wordlist:
            if self.is_allowed(word):
                return word
        return "not found"


def main(wordlist):
    done = False
    state = State()
    while not done:
        guess = state.generate_guess(wordlist)
        if guess == "not found":
            print("Not Found")
            return

        print("Guess: " + guess)
        outcome = input("Output: ")

        if outcome == "ggggg":
            return "done"

        state.process(guess, outcome)


if __name__ == "__main__":
    words = []
    with open('words') as f:
        words = f.read().split("\n")
    main(words)
