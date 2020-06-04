import string
table =str.maketrans('', '', string.punctuation)

des = 'The be123low cod###e does these basic cleaning steps'

word = des

word = word.split()

word = [w.lower() for w in word]
print(word)

word = [w.translate(table) for w in word]
word = [w for w in word if w.isalpha()]
print(word)
