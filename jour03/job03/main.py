import re

tailleMot = int(input("Entrer un nombre de caractère : "))
count = 0
with open('data.txt') as f:
    for line in f:
        for mot in line.split(" "):
            wordwithoutpunctuation = re.sub(r'[^\w\s]', '', mot)

            if len(wordwithoutpunctuation) == tailleMot:
                match = re.search(r'(\S[a-zA-Z]*\S)', wordwithoutpunctuation)
                if match != None:
                    count += 1


print(tailleMot, count)
f.close()