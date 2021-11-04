import re

count = 0
numletterbyword = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
with open('data.txt') as f:
    for line in f:
        for mot in line.split(" "):
            wordwithoutpunctuation = re.sub(r'[^\w\s]', '', mot)
            wordtoint = len(wordwithoutpunctuation)
            wordtostring = str(wordtoint)
            for key in numletterbyword:
                for num in wordtostring:
                    if num == key:
                        numletterbyword[key] += 1


print(numletterbyword)
f.close()