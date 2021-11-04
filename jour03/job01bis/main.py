import re

count = 0
with open('domains.xml') as f:
    for line in f:
        match = re.search(r'(\S+?([^/.]+\.[^/]+)\S+)', line)
        if match != None:
            count += 1

print(count)
f.close()
