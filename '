words = []
with open('words') as f:
    words = f.read().split("\n")
words = [w.lower() for w in words if len(w) == 5]

letters = "abcdefghijklmnopqrstuvwxyz"

letter_counts = {k:0 for k in letters}
for word in words:
    for letter in word:
        letter_counts[letter] += 1

word_scores = {}
for word in words:
    score = 0
    for letter in set(word):
        score += letter_counts[letter]
    word_scores[word] = score

words.sort(key=lambda w: -word_scores[w])

options = {k:range(5) for k in letters}

def is_allowed(word):
    for i,l in enumerate(word):
        if i not in options[l]:
            return False
    return True

def split(s):
    for i in range(0, len(s), 2):
        yield [s[i],s[i+1]]

def process(grays, greens, yellows):
    if grays:
        for l in grays:
            options[l] = []
    if greens:
        for l,p in split(greens):
            options[l] = [int(p)]
    if yellows:
        for l,p in split(yellows):
            options[l].remove(int(p))


while True:
    for word in words:
        if is_allowed(word):
            print(word)
            break

    grays = raw_input("Enter grays: ")
    greens = raw_input("Enter greens: ")
    yellows = raw_input("Enter yellows: ")
    process(grays, greens, yellows)


