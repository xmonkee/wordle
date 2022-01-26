from test import test
import random


def test_wordlist(listname, wordlist, testlist):
    outcomes = [test(testword, wordlist) for testword in testlist]
    print(listname + ": "  + str(sum(outcomes)/len(outcomes)))


if __name__ == '__main__':
    testlist = []
    with open('./wordsets/words_freq') as f:
        testlist = f.read().splitlines()
    testlist = testlist[:3000]
    random.shuffle(testlist)
    testlist = testlist[:200]
    worldlist=[]
    for wordlistfile in ['words_alph', 'words_freq', 'words_comm']:
        with open('./wordsets/'+wordlistfile) as f:
            wordlist = f.read().splitlines()
            test_wordlist(wordlistfile, wordlist, testlist)
    random.shuffle(wordlist)
    test_wordlist("words_rand", wordlist, testlist)


