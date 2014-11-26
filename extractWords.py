import sys
import json

def findWords(candidates, remainingLength, currentPrefix, dictionary, prefixSet):
    if remainingLength == 0:
        if currentPrefix.upper() in dictionary:
            return [currentPrefix]
        else:
            return []
    possibleWords = set()
    for idx, letter in enumerate(candidates):
        remainingLetters = candidates[:idx] + candidates[idx + 1 :]
        if not (currentPrefix+letter).upper() in prefixSet:
            continue
        currentWords = findWords(remainingLetters, remainingLength-1, currentPrefix+letter, dictionary, prefixSet)
        for currentWord in currentWords:
            if currentWord.upper() in dictionary:
                possibleWords.add(currentWord)
    return possibleWords

def build_prefix_set(dictionary):
    prefixes = set()
    for word in dictionary:
        for i in range(len(word)):
            prefixes.add(word[:i+1])
    # with open('preset.txt', 'w+') as outPut:
    #     for item in prefixes:
    #         outPut.write("%s\n" % item)
    return prefixes


from pprint import pprint
json_data=open('dictionary.json')
dictionary = json.load(json_data)
json_data.close()

allWords = dictionary.keys()
prefixes = build_prefix_set(allWords)

if len(sys.argv) < 3:
    print "Please specify words and length"
    sys.exit(1)

candidates = sys.argv[1]
candidateChar = [c for c in candidates]
expectedLength = int(sys.argv[2])

print "processing: " + candidates

possibleWords = findWords(candidateChar, expectedLength, '', dictionary, prefixes)

print "Answer:\n"
for word in possibleWords:
    defination = dictionary[word.upper()]
    print "%(key)s: %(val)s\n" % {'key': word, 'val': defination}