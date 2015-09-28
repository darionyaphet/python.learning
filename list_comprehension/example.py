
words = "The quick brown fox jumps over the lazy dog".split()
tokens = [[word.upper(),word.lower(),len(word)] for word in words]
for token in tokens:print(token)

