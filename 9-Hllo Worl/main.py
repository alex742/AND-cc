import timeit

with open('words.txt') as f:
    words = f.read().splitlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = "hewsda"
for letter in letters:
  alphabet = alphabet.replace(letter, '')

def sortLast():
  valid_words = []
  for word in words:
    valid = True
    for letter in alphabet:
      if letter in word:
        valid = False
    if valid:
      valid_words.append(word)

  valid_words.sort(key=len, reverse=True)

  return valid_words[0]

def sortFirst():
  words.sort(key=len, reverse=True)
  for word in words:
    valid = True
    for letter in alphabet:
      if letter in word:
        valid = False
    if valid:
      return word

def sortFirstBreak():
  words.sort(key=len, reverse=True)
  for word in words:
    valid = True
    for letter in alphabet:
      if letter in word:
        valid = False
        break
    if valid:
      return word

def sortFirstCheckLetters():
  words.sort(key=len, reverse=True)
  for word in words:
    valid = True
    for letter in word:
      if letter not in letters:
        valid = False
        break
    if valid:
      return word

# 1.27s
print("#####\nsortLast\n", sortLast())
print(timeit.timeit(sortLast, number=10))

# 0.48s
print("#####\nsortFirst\n", sortFirst())
print(timeit.timeit(sortFirst, number=10))

# 0.17s
print("#####\nsortFirstBreak\n", sortFirstBreak())
print(timeit.timeit(sortFirstBreak, number=10))

# 0.15s
print("#####\nsortFirstCheckLetters\n", sortFirstCheckLetters())
print(timeit.timeit(sortFirstCheckLetters, number=10))
