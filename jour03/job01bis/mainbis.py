import re

f = open("domains.xml", "r")
lines = f.readlines()
f.close()
count = 0


for line in lines:
    # print(line)
    m = re.search(r'(\S+?([^/.]+\.[^/]+)\S+)', line)
    if m != None:
        count += 1

print(count)