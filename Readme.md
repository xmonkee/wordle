## words.py
Generate word list in descending order of freq

Needs unigram_freq.csv (from kaggle)

## test.py
Test any word

```
$ python test.py arise
about->gbbbb
again->gbyyb
alive->gbgbg
aside->gygbg
arise

$ python test.py query
about->bbbyb
music->bgbbb
fully->bgbbg
query
```

## wordle.py
Play wordle

Take the guess and enter into worlde website

Take the color ouput and enter back into program 

Example ⬜🟩⬜🟨⬜  would be "bgbyb"

```
$ python wordle.py
Guess: about
Output: bbbbb
Guess: which
Output: bbgbb
Guess: drive
Output: gggbb
Guess: drink
Output: ggggg
```
