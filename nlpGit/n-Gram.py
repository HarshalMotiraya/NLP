
from nltk import ngrams

text = "I love natural language processing"
words = text.split()

print("sentence:", text)
print("words:", words)

bigram =list(ngrams(words, 2))
trigram = list(ngrams(words, 3))
drigram = list(ngrams(words, 4))

print("bigrams:", bigram)
print("trigrams:", trigram)
print("drigrams:", drigram)