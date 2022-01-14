from test import test
import random


def test_wordlist(wordlistfile, testlist):
    wordlist = []
    with open('./wordsets/'+wordlistfile) as f:
        wordlist = f.readlines()
    outcomes = [test(testword, wordlist) for testword in testlist]
    print(wordlistfile + ": "  + str(sum(outcomes)/len(outcomes)))


if __name__ == '__main__':
    testlist = []
    with open('./wordsets/words_freq') as f:
        testlist = f.readlines()
    testlist = testlist[:500]
    random.shuffle(testlist)
    for wordlistfile in ['words_alph', 'words_freq', 'words_comm']:
        test_wordlist(wordlistfile, testlist)

