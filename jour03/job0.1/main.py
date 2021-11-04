text = input("Entrer votre phrase : ")
print(text)

f = open('output.txt', 'w')
f.write(text)
f.close