import csv
r = None

words = None
with open('./inputs/words_engl') as f:
    words = f.readlines()
    words = [w.lower() for w in words if len(w) == 5]

word_freq = None
with open('./inputs/unigram_freq.csv') as f:
    r = csv.reader(f)
    word_freq = {l[0]:int(l[1]) for l in r if len(l[0]) == 5}


words.sort(key=lambda w: -word_freq.get(w, 0))
with open('./wordsets/words_freq', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

with open('./wordsets/words_test', 'w') as f:
    for word in words[:5000]:
        f.write(word)
        f.write("\n")

letter_count = {}
for word in words:
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

words.sort(key=lambda w: -sum(letter_count[l] for l in set(w)))
with open('./wordsets/words_comm', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

words.sort()
with open('./wordsets/words_alph', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

