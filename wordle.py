words = []
with open('words') as f:
    words = f.read().split("\n")


blacks = set() # letters that cannot be in word
yellows = {}  # if l in yellow then l is present ut cannot be in positions yellow[l]
greens = {}  # greens[i] is a letter that must be at position i


def is_allowed(word):
    if not all(y in word for y in yellows.keys()):
        return False
    for i,l in enumerate(word):
        if l in blacks:
            return False
        if l in yellows and i in yellows[l]:
            return False
        if i in greens and greens[i] != l:
            return False
    return True


def process(inp, output):
    if len(output) != 5 or len(set(output)-set("byg")) > 0:
        return "error"
    for i,o in enumerate(output):
        l = inp[i]
        if o == 'b':
            blacks.add(l)
        elif o == 'y':
            yellows[l] = (yellows.get(l) or []) + [i]
        else:  # o == 'g'
            greens[i] = l


def generate_guess():
    for word in words:
        if is_allowed(word):
            return word
    return "not found"


def run_guess(guess):
    print("Guess: " + guess)
    output = input("Output: ")
    if output == "ggggg":
        return "done"
    if process(guess, output) == "error":
        return run_guess(guess)
    return "continue"


def main():
    done = False
    while not done:
        guess = generate_guess()
        if guess == "not found":
            print("Not Found")
            return
        done = run_guess(guess) == "done"


if __name__ == "__main__":
    main()
