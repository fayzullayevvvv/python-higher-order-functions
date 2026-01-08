words = ["sun", "mountain", "a", "apple"]

result = sorted(
    words,
    key = lambda word:len(word)
)

print(result)