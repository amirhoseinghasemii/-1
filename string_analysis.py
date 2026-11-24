text = input("Enter a text: ")
words = text.split()
print("Number of words:", len(words))
print("Number of characters:", len(text))
chars = {}
for char in text:
    if char != " ":
        chars[char] = chars.get(char, 0) + 1
if chars:
    most = max(chars, key=chars.get)
    print("Most repeated character:", most)
word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1
print("Word repetition:")
for word, count in word_count.items():
    print(word, ":", count)
