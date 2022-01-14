import csv
r = None
word_freq = None
with open('./unigram_freq.csv') as f:
    r = csv.reader(f)
    word_freq = {l[0]:int(l[1]) for l in r if len(l[0]) == 5}

words = list(word_freq.keys())

words.sort(key=lambda w: -word_freq[w])
with open('./words_freq', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

letter_count = {}
for word in words:
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

words.sort(key=lambda w: -sum(letter_count[l] for l in set(w)))
with open('./words_common_letters', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

words.sort()
with open('./words_alphabetic', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")

