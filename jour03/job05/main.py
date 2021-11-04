import re

count = 0
letterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
with open('data.txt') as f:
    for line in f:
        for mot in line.split(" "):
            wordwithoutpunctuation = re.sub(r'[^\w\s]', '', mot)
            wordLower = wordwithoutpunctuation.lower()
            for key in letterCount:
                for letter in wordLower:
                    if letter == key:
                        letterCount[key] += 1


print(letterCount)
f.close()