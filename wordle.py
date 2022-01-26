class State:
    def __init__(self, wordlist):
        self.guesses = 0
        self.wordlist = wordlist
        # letters that cannot be in word
        self.banned = set()
        # list of previous guesses and outcomes
        self.prev = list()

    def process(self, guess, outcome):
        if outcome == "banned":
            self.banned.add(guess)
            return
        if len(outcome) != 5:
            raise Exception(outcome)
        if len(set(outcome) - set('byg')) > 0:
            raise Exception(outcome)
        self.prev.append((guess, outcome))

    def is_allowed(self, word):
        if word in self.banned:
            return False
        for guess,outcome in self.prev:
            checked = [False]*5
            for i in range(5):
                if outcome[i] == 'g':
                    if word[i] != guess[i]: return False
                    checked[i] = True
            for i in range(5):
                if outcome[i] == 'y':
                    if word[i] == guess[i]: return False
                    for j in range(5):
                        if not checked[j] and i != j:
                            if word[j] == guess[i]:
                                checked[j] = True
                                break
                    else: # yellow letter not found
                        return False
            for i in range(5):
                if outcome[i] == 'b':
                    for j in range(5):
                        if not checked[j]:
                            if word[j] == guess[i]:
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
