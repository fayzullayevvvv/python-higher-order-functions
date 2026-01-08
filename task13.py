sentence = "Functional programming in Python is very powerful and elegant"

result = sorted(
    sentence.split(),
    key = lambda word:len(word),
    reverse = True
)

print(result[:3])