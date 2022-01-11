import csv
r = None
word_freq = None
with open('./unigram_freq.csv') as f:
    r = csv.reader(f)
    word_freq = {l[0]:int(l[1]) for l in r if len(l[0]) == 5}

words = list(word_freq.keys())
words.sort(key=lambda w: -word_freq[w])
with open('./words2', 'w') as f:
    for word in words:
        f.write(word)
        f.write("\n")
