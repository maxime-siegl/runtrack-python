import re

count = 0
with open('data.txt') as f:
    for line in f:
        for mot in line.split(" "):
            wordwithoutpunctuation = re.sub(r'[^\w\s]', '', mot)
            match = re.search(r'(\S[a-zA-Z]*\S)', wordwithoutpunctuation)
            if match != None:
                count += 1


print(count)
f.close()
